# program template for Spaceship
# http://www.codeskulptor.org/#user16_yIqCmjNZxyfMP9o_0.py

import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score, prev_score, high_score = 0, 0, 0
lives = 3
time = 0.5
started = False

rock_group = set([])
missile_group = set([])
explosion_group = set([])

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False, tiles = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated
        self.tiles = tiles

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
    
    def get_tiles(self):
        return self.tiles

    
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
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot3.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True, [9, 1])
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_orange.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.ogg")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.ogg")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.ogg")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.ogg")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.thrust_vel = 0
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.missile = False
        
    def shoot(self):
        anglevec = angle_to_vector(self.angle)
        missile_pos = [None, None]
        for n in range(2):
            missile_pos[n] = self.pos[n] + self.radius * anglevec[n]
        missile_vel = [None, None]
        for n in range(2):
            missile_vel[n] = 5 * anglevec[n] + self.vel[n] 
        missile_group.add(Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound))

    def set_angle_vel(self, angle_vel):
        # set angle velocity in rads per second
        self.angle_vel = angle_vel / 60        
        
    def thrust_on(self, thrust = True):
        self.thrust = thrust
        if thrust:
            # set center to thrust image
            self.image_center[0] = self.image_size[0] * 1.5
            # play thrust sound
            ship_thrust_sound.play()
            # set velocity per second (I know, 0.5 would have done the trick as well)
            self.thrust_vel = 30 / 60
        else:
            # set center back to first (non-thrust) image
            self.image_center[0] = self.image_size[0] / 2
            ship_thrust_sound.rewind()
            self.thrust_vel = 0
            
    def get_radius(self):
        return self.radius
    
    def get_pos(self):
        return self.pos
            
    def draw(self,canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        
    def update(self):
        # update angle with velocity
        self.angle = (self.angle + self.angle_vel) % (2*math.pi)
        # store the current vector for the direction the ship is pointing
        anglevec = angle_to_vector(self.angle)
        for n in range(2):
            # reduce current velocity by friction and add the thrust in
            # the direction where the sip is currently pointing
            self.vel[n] = (1 - 0.02) * self.vel[n] + self.thrust_vel * anglevec[n]
        # update the position and wrap around
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

        if self.missile:
            self.missile.update()
    
# Sprite class
class Sprite:
#    def __init__(self, image):
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.vel = [0, 0]
        self.pos = pos
        self.angle = ang
        anglevec = angle_to_vector(self.angle)
        # sum up velocity and a constant multiple of the angle vector
        for n in range(2):
            self.vel[n] = vel[n] + 2 * anglevec[n]
        self.angle_vel = ang_vel

        if sound:
            sound.rewind()
            sound.play()
        self.spawned = False
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.tiles = info.get_tiles()
        self.age = 0

    def collide(self, other_object):
        oo_radius = other_object.get_radius()
        oo_pos = other_object.get_pos()
        distance = math.sqrt((self.pos[0] - oo_pos[0]) ** 2 + (self.pos[1] - oo_pos[1]) ** 2)
        if distance <= self.radius + oo_radius:
            return True
        else:
            return False
       
    def get_radius(self):
        return self.radius
    
    def get_pos(self):
        return self.pos            

    def draw(self, canvas):
        if self.animated:
            image_center = [self.image_center[0] +  self.image_size * self.time % self.tiles[0], self.image_center[1]
                            + self.image_size * (self.time // self.tiles[0]) % self.tiles[1]]
            canvas.draw_image(self.image, image_center, self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        self.angle = (self.angle + self.angle_vel) % (2*math.pi)
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        self.age += 1
        if self.age <= self.lifespan:
            return False
        else:
            return True

def process_sprite_group(group, canvas):
    for sprite in list(group):
        sprite.draw(canvas)
        # if update methode returns True objects lifespan expired
        if sprite.update():
            group.remove(sprite)
    for explosion in explosion_group:
        expl_pos = explosion.get_pos()
        image_center = explosion_info.get_center()
        image_size = explosion_info.get_size()
        tiles = explosion_info.get_tiles()
        image_center = [image_center[0] + image_size[0] * (explosion.age // 1 % tiles[0]), image_center[1]
                        + image_size[0] * (explosion.age // tiles[0] % tiles[1])]
        canvas.draw_image(explosion_image, image_center, image_size, expl_pos, image_size, 0)
        # update explosion age
        explosion.age += 1
        # if age reaches the sum of all tiles it means that all tiles were drawn, thus object should be removed
        if explosion.age >= tiles[0] * tiles[1]:
            explosion_group.remove(explosion)

def group_collide(group, other_object):
    count = 0
    for group_object in list(group):
        # check if objects are colliding and act accordingly
        if group_object.collide(other_object):
            explosion_sound.rewind()
            explosion_sound.play()
            # reset age of the object that will be removed to have an explosion object with age 0
            group_object.age = 0
            explosion_group.add(group_object)
            group.remove(group_object)
            count += 1
    return count
 
def group_group_collide(group, other_group):
    count = 0
    for group_object in list(group):
        count_helper = count
        count += group_collide(other_group, group_object)
        # if count was raised by group_collide then at least one collision occured
        # with this object => this object should be removed
        if count_helper < count:
            group.remove(group_object)
    return count

def empty_group(group):
    for group_object in list(group):
        group.remove(group_object)

# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        
def keydown(key):
    if key == simplegui.KEY_MAP['left']:
        # angle velcity in rads per second => 270° per second
        my_ship.set_angle_vel(-1.5 * math.pi)
    elif key == simplegui.KEY_MAP['right']:
        my_ship.set_angle_vel(1.5 * math.pi)
    elif key == simplegui.KEY_MAP['up']:
        # velocity in pixel per second²
        my_ship.thrust_on()
    elif key == simplegui.KEY_MAP['space']:
        my_ship.shoot()
    
def keyup(key):
    if key == simplegui.KEY_MAP['up']:
        my_ship.thrust_on(False)
    elif key == simplegui.KEY_MAP['left'] or key == simplegui.KEY_MAP['right']:
        my_ship.set_angle_vel(0)    
           
def draw(canvas):
    global time, lives, score, prev_score, high_score, started, my_ship
    if lives == 0:
        timer.stop()
        started = False
        empty_group(rock_group)
        empty_group(missile_group)
        empty_group(explosion_group)
        my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
        soundtrack.rewind()
        prev_score = score
        if score > high_score:
            high_score = score
        score = 0
        lives = 3
    
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
    canvas.draw_text("Score:" + str(score), [600, 50], 20, "Yellow")
    canvas.draw_text("Lives:" + str(lives), [50, 50], 20, "Yellow")


    # draw splash screen if not started
    if not started:
        canvas.draw_image(splash_image, splash_info.get_center(), 
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2], 
                          splash_info.get_size())
        canvas.draw_text("Last Score: " + str(prev_score), [WIDTH / 2 - 4 * len("Last Score: " + str(prev_score)), HEIGHT * 2/3], 20, "Yellow")
        canvas.draw_text("High Score: " + str(high_score), [WIDTH / 2 - 6 * len("High Score: " + str(high_score)), HEIGHT * 2/3 + 40], 30, "Yellow")
    else:
        if not timer.is_running():
            timer.start()
            soundtrack.play()
        # draw ship and sprites
        my_ship.draw(canvas)
        process_sprite_group(rock_group, canvas)
        process_sprite_group(missile_group, canvas)
        #check collitions
        lives -= group_collide(rock_group, my_ship)
        score += 100 * group_group_collide(rock_group, missile_group)
        # update ship
        my_ship.update()


# timer handler that spawns a rock    
def rock_spawner():
    if len(rock_group) < 12:
        # 100 pts = +0.5 pixel per second
        # 1000 pts = 1.5 pixel per second
        # 10000 pets = 5 pixel per second
        score_factor = math.sqrt(score) / 20
        pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
        # set random velocity of min 1 and max. 2 pixel per second
        vel = [(random.randrange(30, 61) + score_factor) / 60, (random.randrange(30, 61) + score_factor) / 60]
        # set random angle between 0 and 2 pi (360°)
        angle = random.random() * 2 * math.pi
        # set random angle velocity of max. +/-270° per second
        ang_vel = (random.random() * 2 -1) * 1.5 * math.pi / 60
        rock = Sprite(pos, vel, angle, ang_vel, asteroid_image, asteroid_info)
        if not rock.collide(my_ship):
            rock_group.add(rock)
        else:
            print "rock removed"
#        rock_group.add(Sprite(pos, vel, angle, ang_vel, asteroid_image, asteroid_info))
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
frame.start()
