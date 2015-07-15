# program template for Spaceship
# http://www.codeskulptor.org/#user16_237V3zKqJn_1.py

import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0.5
started = False
MISSILE_LIFESPAN = 50

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, MISSILE_LIFESPAN)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
soundtrack.set_volume(.5)
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

def group_collide(group, other_object):
    members_to_remove = set([])
    for member in group:
        if (member.collide(other_object)):
            members_to_remove.add(member)
            
    group.difference_update(members_to_remove)

    for sprite_to_remove in members_to_remove:
        #def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None, age = 0):
        explosion_group.add(Sprite(sprite_to_remove.get_position(), [0, 0], 0, 0, explosion_image, explosion_info, explosion_sound))

    
    return len(members_to_remove)

def group_group_collide(group_one, group_two):
    group_one_delete = set([])
    
    group_one_copy = set(group_one)
    
    for group_one_member in group_one:
        if (group_collide(group_two, group_one_member) > 0):
            group_one_delete.add(group_one_member)
            
    group_one.difference_update(group_one_delete)
    
    return len(group_one_delete)
        

SHIP_FRICTION_CONSTANT = 0.1
MISSILE_VELOCITY_CONSTANT = 5

# game rules
ROCKS_MAX_NUMBER = 12


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.ANGULAR_VEL_CHANGE = 0.10
        self.info = info
        
        self.ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
        self.ship_thrust_sound.set_volume(1)
        
        self.friction_constant = SHIP_FRICTION_CONSTANT

    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
    
    def draw(self,canvas):
        canvas.draw_image(self.image, self.info.get_center(), self.image_size, self.pos, self.image_size, self.angle)
        
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        self.pos[0] = self.pos[0] % WIDTH
        self.pos[1] = self.pos[1] % HEIGHT
        
        self.angle += self.angle_vel
        
        forward = [math.cos(self.angle), math.sin(self.angle)]
        #forward = angle_to_vector(self.angle)
        if (self.thrust):
            #forward = [math.cos(self.angle), math.sin(self.angle)]
            self.vel[0] += forward[0]
            self.vel[1] += forward[1]
            
        self.vel[0] = (1 - self.friction_constant) * self.vel[0]
        self.vel[1] = (1 - self.friction_constant) * self.vel[1]
        
    def turn_right(self):
        self.angle_vel += self.ANGULAR_VEL_CHANGE
    
    def turn_left(self):
        self.angle_vel -= self.ANGULAR_VEL_CHANGE
        
    def stop_turn(self):
        self.angle_vel = 0
        
    def turn_thrusters_on(self):
        self.thrust = True
        self.info.get_center()[0] = 135
        self.ship_thrust_sound.play()
        
    def turn_thrusters_off(self):
        self.thrust = False
        self.info.get_center()[0] = 45
        self.ship_thrust_sound.rewind()
        
    def shoot(self):
        global missile_group
        forward = [math.cos(self.angle), math.sin(self.angle)]
        a_missile_pos = [self.pos[0] + forward[0]*self.radius, self.pos[1] + forward[1]*self.radius]
        a_missile_velocity = [self.vel[0] + forward[0]*MISSILE_VELOCITY_CONSTANT, self.vel[1] + forward[1]*MISSILE_VELOCITY_CONSTANT]
        missile_group.add(Sprite(a_missile_pos, a_missile_velocity, 0, 0, missile_image, missile_info, missile_sound))
        
    def collide(self, other_object):
        if (dist(self.get_position(), other_object.get_position()) < self.get_radius() + other_object.get_radius()):
            return True
        else:
            return False
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None, age = 0):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = age
        self.info = info
        if sound:
            sound.rewind()
            sound.play()
            
    def get_position(self):
        return self.pos
    
    def get_radius(self):
        return self.radius
   
    def draw(self, canvas):
        if (self.animated):
            canvas.draw_image(self.image, [self.info.get_center()[0] + self.age*self.image_size[0], self.info.get_center()[1]], self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.info.get_center(), self.image_size, self.pos, self.image_size, self.angle)
     
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        self.pos[0] = self.pos[0] % WIDTH
        self.pos[1] = self.pos[1] % HEIGHT
      
        self.angle += self.angle_vel
        
        self.age += 1
        
        if (self.age >= self.lifespan):
            return True
        else:
            return False
        
    def collide(self, other_object):
        if (dist(self.get_position(), other_object.get_position()) < self.get_radius() + other_object.get_radius()):
            return True
        else:
            return False
        
        

def key_down_handler(key):
    global my_ship
    if (key == simplegui.KEY_MAP["left"]):
        my_ship.turn_left()
    elif (key == simplegui.KEY_MAP["right"]):
        my_ship.turn_right()
    elif (key == simplegui.KEY_MAP["up"]):
        my_ship.turn_thrusters_on()
    elif (key == simplegui.KEY_MAP["space"]):
        my_ship.shoot()
        
def key_up_handler(key):
    global my_ship
    if (key == simplegui.KEY_MAP["left"] or key == simplegui.KEY_MAP["right"]):
        my_ship.stop_turn()
    elif (key == simplegui.KEY_MAP["up"]):
        my_ship.turn_thrusters_off()

def click_handler(pos):
    global started, lives, score
    lives = 3
    score = 0
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    
    if (not started) and inwidth and inheight:
        started = True
        soundtrack.rewind()
        soundtrack.play()

def process_sprite_group(sprite_set, canvas):
    global explosion_group
    sprites_to_remove = set([])
    for sprite in sprite_set:
        if (sprite.update()):
            sprites_to_remove.add(sprite)
        sprite.draw(canvas)
                
    sprite_set.difference_update(sprites_to_remove)
    
def draw(canvas):
    global time, lives, score, started, missile_group, rock_group, explosion_group
    
    # animiate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, [center[0] - wtime, center[1]], [size[0] - 2 * wtime, size[1]], 
                                [WIDTH / 2 + 1.25 * wtime, HEIGHT / 2], [WIDTH - 2.5 * wtime, HEIGHT])
    canvas.draw_image(debris_image, [size[0] - wtime, center[1]], [2 * wtime, size[1]], 
                                [1.25 * wtime, HEIGHT / 2], [2.5 * wtime, HEIGHT])

    # draw ship and sprites
    my_ship.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
  
    process_sprite_group(missile_group, canvas)
    process_sprite_group(rock_group, canvas)
    process_sprite_group(explosion_group, canvas)
    
    if (group_collide(rock_group, my_ship) > 0):
        lives -= 1
        
    if (lives == 0):
        stop_game()
        
    score += group_group_collide(missile_group, rock_group)
    
    canvas.draw_text("Lives: " + str(lives), (25, 25), 24, "White")
    canvas.draw_text("Score: " + str(score), (WIDTH - 150, 25), 24, "White")
    
    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())

def stop_game():
    global missile_group, rock_group, started
    
    started = False
    missile_group = set([])
    rock_group = set([])
    
# timer handler that spawns a rock    
def rock_spawner():
    global rock_group, started, my_ship
    
    if (started):
        width_divider = random.random() * random.randrange(0, WIDTH/100) + 1 
        height_divider = random.random() * random.randrange(0, HEIGHT/100) + 1
        
        velocity = [random.random() * random.randrange(0, 5) * random.choice([-1,1]), random.random() * random.randrange(0, 5) * random.choice([-1,1])]
        angular_velocity = random.random() / 4 * random.choice([-1,1])
        
        if (len(rock_group) < ROCKS_MAX_NUMBER):
            rock_pos = [WIDTH / width_divider, HEIGHT / height_divider]
            # never generate rock that's around 25 pixels around ship
            while ((my_ship.get_position()[0] - 25 < rock_pos[0] < my_ship.get_position()[0] + 25) or (my_ship.get_position()[1] - 25 < rock_pos[1] < my_ship.get_position()[1] + 25)):
                width_divider = random.random() * random.randrange(0, WIDTH/100) + 1 
                height_divider = random.random() * random.randrange(0, HEIGHT/100) + 1
                rock_pos = [WIDTH / width_divider, HEIGHT / height_divider]
            rock = Sprite(rock_pos, velocity, 0, angular_velocity, asteroid_image, asteroid_info)
            rock_group.add(rock)
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
rock_group = set ([])
missile_group = set ([])
explosion_group = set ([])

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(key_down_handler)
frame.set_keyup_handler(key_up_handler)

frame.set_mouseclick_handler(click_handler)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
