# http://www.codeskulptor.org/#user16_7BY7hy435a_16.py
#This game was designed to run in Chrome browser
# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
ROTATION_VEL = 0.2
FORWARD_VEL = 1
SPACE_DEBRIS_FRICTION = 0.925
score = 0
lives = 3
time = 0.5
launch = 0
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
# Randomly select debris color
debris_color = random.choice(['debris1_brown.png', 'debris2_brown.png', 'debris3_brown.png', 'debris4_brown.png',
                 'debris1_blue.png', 'debris2_blue.png', 'debris3_blue.png', 'debris4_blue.png', 'debris_blend.png'])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/" + debris_color)

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
# Randomly select nebula
nebula_color = random.choice(["nebula_brown.png", "nebula_blue.png"])

nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/" + nebula_color)

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
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = 0 
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.friction = SPACE_DEBRIS_FRICTION
        
    def draw(self,canvas):
        #Draw the ship image    
        #canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest, rotation)
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        
        
    def update(self):
        # control position and velocity update behavior
        self.angle += self.angle_vel
        
        #calculate thrust acceleration 
        if self.thrust:
            orient = angle_to_vector(self.angle)
            self.vel[0] += FORWARD_VEL * orient[0]
            self.vel[1] += FORWARD_VEL * orient[1]
            ship_thrust_sound.play() #play thruster sound
        else:
            ship_thrust_sound.rewind() #rewind thruster sound
        
        #velocity        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        #friction code
        self.vel[0] *= self.friction
        self.vel[1] *= self.friction
        
        # check boundaries and roll over
        self.pos[0] %= WIDTH
        self.pos[1] %= HEIGHT
        
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
        #canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest, rotation)
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        self.angle += self.angle_vel
        #velocity        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        # check boundaries and roll over
        self.pos[0] %= WIDTH
        self.pos[1] %= HEIGHT
        if self.lifespan > 0:
            self.lifespan -= 1
            
            
            
def missile_launch():
    global launch
    # on space bar launch missile
    if not launch:
        #Update launch position angle
        orient = angle_to_vector(my_ship.angle)
        #Launch missile from tip of ship.
        a_missile.pos = [my_ship.pos[0] + ship_info.size[0] / 2 * orient[0] , my_ship.pos[1] + ship_info.size[0] / 2 * orient[1] ]
    
        #set velocity vector    
        a_missile.vel = [ my_ship.vel[0] + 10 * orient[0],  my_ship.vel[1] + 10 * orient[1]]
        a_missile.lifespan = 60
        #setup sound
        missile_sound.rewind()
        missile_sound.play()
        launch = True
    else:
        launch = False
          
    
#purpose of this function is to toggle thrust on and off based on handler.    
def start_ship_thrust():
    if my_ship.thrust:
        my_ship.image_center[0] -= ship_info.size[0]
    else:
        my_ship.image_center[0] += ship_info.size[0]
    my_ship.thrust ^= 1 

def ship_left():
    if my_ship.angle_vel == 0:
        my_ship.angle_vel = -ROTATION_VEL
    else:
        my_ship.angle_vel = 0
        
def ship_right():
    if my_ship.angle_vel == 0:
        my_ship.angle_vel = +ROTATION_VEL
    else:
        my_ship.angle_vel = 0
  
inputs = {"space": missile_launch,
          "up": start_ship_thrust,
          "left": ship_left,
          "right": ship_right}

# define keyhandlers to control firing_angle
def keydown(key):
    for i in inputs:
        if key == simplegui.KEY_MAP[i]:
            inputs[i]()
    
def keyup(key):
    for i in inputs:
        if key == simplegui.KEY_MAP[i]:
            inputs[i]()

def draw(canvas):
    global time

    # animate background
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
    
    #draw Lives in the upper left
    canvas.draw_text("LIVES " + str(lives), (WIDTH * 0.05 , HEIGHT * 0.1), 20, "White", "serif")
 
    #draw Score in the upper right
    canvas.draw_text("SCORE " + str(score), (WIDTH * 0.85, HEIGHT * 0.1), 20, "White", "serif")
         
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    #create rock velocity
    random_rock_ang_vel = random.randint(-3,3) * 0.1
    random_velocity_vector = [random.randint(-10,10)* 0.1, random.randint(-10, 10)* 0.1]
    random_position = [random.randint(0,WIDTH), random.randint(0,HEIGHT)]
    a_rock = Sprite(random_position, random_velocity_vector, 1, random_rock_ang_vel, asteroid_image, asteroid_info)
 
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0, asteroid_image, asteroid_info)
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [0,0], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
