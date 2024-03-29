# program template for Spaceship
# http://www.codeskulptor.org/#user16_cq3knjBBbK_3.py
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
ANGLE_VEL = .06
ACC = .2
score = 0
lives = 3
time = 0.5

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
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.sound = sound
        self.friction = .97
        
    def shoot(self):
        global a_missile
        orient = angle_to_vector(self.angle)
        cannon = [self.pos[0] + self.radius * orient[0],
                  self.pos[1] + self.radius * orient[1]]
        missile_vel = [self.vel[0] * 2, self.vel[1] * 2]
        #print self.vel[0], self.vel[1]
        #missile_vel[0] = self.vel[0] + dist(self.vel[0], self.vel[1])
        #missile_vel[1] = self.vel[1] + dist(self.vel[0], self.vel[1])
        
        a_missile = Sprite(cannon, missile_vel, 
                           0, 0, missile_image, missile_info, missile_sound)
        
        
        
    def draw(self,canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "White", "White")
        # 1. Prints ship on canvas with Ship.pos, Ship.angle
        canvas.draw_image(self.image, self.image_center,
                          self.image_size, self.pos, self.image_size,
                          self.angle)
        # 2. Update Ship's position depending on velocity
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        # friction
        self.vel[0] *= self.friction
        self.vel[1] *= self.friction
        
        # 3. Increment angle by its angular velocity
        self.angle += self.angle_vel
        
        # 8. Helper function to work out direction thrust
        vector = angle_to_vector(self.angle)
        
        # 9. Acceleration
        if self.thrust:
            self.vel[0] += ACC * vector[0]
            self.vel[1] += ACC * vector[1]
        
        # 10. Wrap around code
#        if self.pos[0] < 0:
#            self.pos = [(self.pos[0] + self.radius) % WIDTH,
#                        (self.pos[1] + self.radius) % HEIGHT]
        if self.pos[0] < 0:
            self.pos[0] = self.pos[0] % WIDTH + self.radius
        elif self.pos[0] > WIDTH + self.radius:
            self.pos[0] =  0
          
        if self.pos[1] < 0:
            self.pos[1] = self.pos[1] % HEIGHT + self.radius
        elif self.pos[1] > HEIGHT + self.radius:
            self.pos[1] =  0
#        
    # 5 toggle thrust method
    def toggle_thrust(self):
        if self.thrust:
            self.thrust = False
            #6. Thrust image update
            self.image_center[0] -= self.image_size[0]
            #7. Thrust Sound rewind
            self.sound.rewind()
        else:
            self.thrust = True
            self.image_center[0] += self.image_size[0]
            #7. Thrust sound play
            self.sound.play()
            
        
    
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
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
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        # wrap around
        if self.pos[0] < 0:
            self.pos[0] = self.pos[0] % WIDTH + self.radius
        elif self.pos[0] > WIDTH + self.radius:
            self.pos[0] =  0

        if self.pos[1] < 0:
            self.pos[1] = self.pos[1] % HEIGHT + self.radius
        elif self.pos[1] > HEIGHT + self.radius:
            self.pos[1] =  0        

           
def draw(canvas):
    global time
    
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
    a_rock.draw(canvas)
    a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()
    
    #lives and score
    canvas.draw_text("Lives: " + str(lives), (50,50), 12, "Red")
    canvas.draw_text("Score: " + str(score), (700,50), 12, "White")
    
            
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    rand_vel = [0,0]
    lower = -2
    upper = 2
    range_width = upper - lower
    rand_vel[0] = random.random() * range_width + lower
    rand_vel[1] = random.random() * range_width + lower
   
    rand_ang = random.random() * range_width + lower
    rand_ang_vel = random.random() * .1 - .05
    
    a_rock = Sprite([WIDTH / 3, HEIGHT / 3], rand_vel, rand_ang, rand_ang_vel, asteroid_image, asteroid_info)
    

# 4. keyboard handlers
# Dictionary for keys
kb_inputs = {"left": -ANGLE_VEL,
             "right": ANGLE_VEL,
             "up": 0}

def key_helper(key, info = None):
    for k in kb_inputs:
        if key == simplegui.KEY_MAP[k]:
            if k == "left" or k == "right":
                my_ship.angle_vel += kb_inputs[k]
            else:
                # 5 Ship Thrust toggle
                my_ship.toggle_thrust()
    if key == simplegui.KEY_MAP['space']:
        my_ship.shoot()
            
def keydown(key):
    key_helper(key)
    
def keyup(key):
    my_ship.angle_vel = 0
    # 5 Ship Thrust toggle
    if key == simplegui.KEY_MAP['up']:
        my_ship.toggle_thrust()
    
 
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info, ship_thrust_sound)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [0, 0], 0, 0, asteroid_image, asteroid_info)
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)

# 4. register keyboard handlers
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
