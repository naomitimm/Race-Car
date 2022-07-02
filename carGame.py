import sys, pygame

import math
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# IMPORT OBJECT LOADER
from objloader1 import *
#from car import drawCar
pygame.init()
viewport = (1920,1080)
hx = viewport[0]/2
hy = viewport[1]/2
srf = pygame.display.set_mode(viewport, OPENGLBLIT | DOUBLEBUF)
glViewport(0,0,1920,1080)
glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 200, 100, 0.0))
glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.5, 0.5, 0.5, 1.0))
glEnable(GL_LIGHT0)
glEnable(GL_LIGHTING)
glEnable(GL_COLOR_MATERIAL)
glEnable(GL_DEPTH_TEST)
glShadeModel(GL_SMOOTH)                         
# LOAD OBJECT AFTER PYGAME INIT
#CARLASTTWO

#skyBoxfn4
glEnable(GL_DEPTH_TEST)
obj = OBJ("readableLast.obj")
#carImage=pygame.image.load('carExported.png').convert()
glDisable(GL_DEPTH_TEST)

clock = pygame.time.Clock()

glBindBuffer(GL_ARRAY_BUFFER,glGenBuffers(1))
glClear(GL_COLOR_BUFFER_BIT)
glClear(GL_DEPTH_BUFFER_BIT)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
width, height = viewport
gluPerspective(100.0, width/float(height), 1, 2000)
#gluLookAt(0,2,1,0,2,0,0,1,0)
glEnable(GL_DEPTH_TEST)
glMatrixMode(GL_MODELVIEW)
pygame.key.set_repeat()
rx, ry = (0,0)
tx, ty = (0,0)
zpos = 16
MOVEMENT=0
ROTATE=0
CAMERA=-2
ATCENTERX=0

ATCENTERZ=0
CHECK=0
CHECKCAMERA=0

def keyboard(key, x, y):
    key = key.decode("utf-8")
    global glutshape, solid
    if key == chr(27) or key == "q":
        sys.exit()
    try:
        if int(key) < 10:
            glutshape = int(key)
    except:
        pass
    if key == "w" or key == "s":
        solid = key
    glutPostRedisplay()
class car1():
    def __init__(self):
        self.obj2=OBJ("CARFINAL.obj")
        self.CHECK=0
        self.CHECKCAMERA=0
        self.ROTATECAMERA=0
        self.ROTATECAMERAZ=0
        self.ROTATE=0
        self.MOVEMENT=0
        self.CAMERA=-2
    def rotate(self):
        
        glRotate(self.ROTATE, 0, 1, 0)
        
        
        #
    def move(self):
        
        glTranslate(-self.CHECK, 0,-self.MOVEMENT )
        
        
class car2():
    def __init__(self):
        self.obj3=OBJ("CARFINAL2.obj")
        self.MOVEMENT=0
        self.CHECK=-10
        self.ROTATE=0
        
        
        
    def move(self):
        
            
        if(self.MOVEMENT<300):
            
            self.MOVEMENT=self.MOVEMENT+4
            glTranslate(-self.CHECK,0,-self.MOVEMENT)
            
        if(self.MOVEMENT>=300 and self.MOVEMENT<400):
             self.CHECK+=math.sin(math.radians(8))*4
                
             self.MOVEMENT+=math.cos(math.radians(8))*4
             
             glTranslate(-self.CHECK,0,-self.MOVEMENT)
        if(self.MOVEMENT>=400 and self.CHECK<100):
            self.CHECK+=math.sin(math.radians(45))*4
            self.MOVEMENT+=math.sin(math.radians(45))*4
        if(self.MOVEMENT>=450 and self.MOVEMENT<600):
            self.CHECK+=math.sin(math.radians(8))*4
            self.MOVEMENT+=math.sin(math.radians(8))*4
        if(self.MOVEMENT>=600 and self.CHECK<400):
            self.CHECK+=math.sin(math.radians(90))*4
            self.MOVEMENT+=math.cos(math.radians(90))*4
        if(self.MOVEMENT>=600 and self.CHECK>400):
            self.CHECK+=math.cos(math.radians(90))*4
            self.MOVEMENT-=math.sin(math.radians(90))*4
            
        
def main():
    global CHECK
    global CHECKCAMERA
    global ATCENTERZ
    global ATCENTERX
    global ROTATE
    global MOVEMENT
    global CAMERA
    global zpos
    car=car1()
    CAR=car2()
   
    while 1:
        clock.tick(30)
        pygame.key.set_repeat(10,10)
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            elif e.type == KEYDOWN and e.key == K_ESCAPE:
                sys.exit()
            elif e.type == MOUSEBUTTONDOWN:
                if e.button == 4: zpos = max(1, zpos-1)
                elif e.button == 5: zpos += 1
                elif e.button == 1: rotate = True
                elif e.button == 3: move = True
            elif e.type == MOUSEBUTTONUP:
                if e.button == 1: rotate = False
                elif e.button == 3: move = False
            elif e.type == MOUSEMOTION:
                i, j = e.rel
    ##            if rotate:
    ##                rx += i
    ##                ry += j
    ##            if move:
    ##                tx += i
    ##                ty -= j
            
             
    ##            if e.key==pygame.k_a:
    ##                MOVEMENT+=5
    ##                CAMERA+=5
    ####        event=pygame.event.wait()
    ##        if event.type==pygame.KEYUP:
    ##            MOVEMENT+=5
    ##            CAMERA+=5
        
        pressed=pygame.key.get_pressed()
        if(pressed[K_UP]):
            
            
            if(math.cos(car.ROTATE)==1 or math.cos(car.ROTATE)==-1):
               car.MOVEMENT+=4
               #car.CAMERA+=4
               car.ROTATECAMERAZ+=4
            elif(math.cos(car.ROTATE)==0):
                car.CHECK+=4
                car.ROTATECAMERA+=4
              
            else:
                
                car.CHECK+=math.sin(math.radians(car.ROTATE))*4
                
                car.MOVEMENT+=math.cos(math.radians(car.ROTATE))*4
                car.ROTATECAMERA+=math.sin(math.radians(car.ROTATE))*4
                car.ROTATECAMERAZ+=math.cos(math.radians(car.ROTATE))*4
                #car.CHECKCAMERA+=math.sin(math.radians(car.ROTATE))*4
                #car.CAMERA+=math.cos(math.radians(car.ROTATE))*4
                
           
        if(pressed[K_DOWN]):
            if(math.cos(car.ROTATE)==1 or math.cos(car.ROTATE)==-1):
               car.MOVEMENT-=4
               #car.CAMERA-=4
               car.ROTATECAMERAZ-=4
            else:
                car.CHECK-=math.sin(math.radians(car.ROTATE))*4
                #car.ATCENTERZ-=math.cos(math.radians(car.ROTATE))*4
                #car.ATCENTERX-=math.sin(math.radians(car.ROTATE))*4
                car.MOVEMENT-=math.cos(math.radians(car.ROTATE))*4
                #car.CAMERA-=math.cos(math.radians(car.ROTATE))*4
                
                #car.CHECKCAMERA-=math.sin(math.radians(car.ROTATE))*4
            # print(CHECK)
            #print(MOVEMENT)
        if(pressed[K_RIGHT]):
            car.ROTATE-=90
            car.ROTATE=car.ROTATE%-360
            
    ##        
            #ROTATECAMERAZ-=4/100
            #print(ROTATE)
        if(pressed[K_LEFT]):
            
            car.ROTATE+=90
            
            car.ROTATE=car.ROTATE%360
            
            #CHECKCAMERA-=4/10
    ##        ROTATECAMERA+=4/100
    ##        ROTATECAMERAZ+=4/100     
            #print(ROTATE)
        if(car.ROTATE==-90 or car.ROTATE==270):
            car.ROTATECAMERAZ=car.MOVEMENT
            car.ROTATECAMERA=car.CHECK-4
        if(car.ROTATE==-180 or car.ROTATE==180):
            car.ROTATECAMERAZ=car.MOVEMENT-4
            car.ROTATECAMERA=car.CHECK
            
        if(car.ROTATE==-270 or car.ROTATE==90):
            car.ROTATECAMERAZ=car.MOVEMENT
            car.ROTATECAMERA=car.CHECK+4
        if(car.ROTATE==0):
            car.ROTATECAMERAZ=car.MOVEMENT+4
            car.ROTATECAMERA=car.CHECK
        
         
##        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
##        glMatrixMode(GL_MODELVIEW)
##        glLoadIdentity()
##        gluLookAt(-CHECKCAMERA,3,-CAMERA,-ATCENTERX,3,-ATCENTERZ,0,1,0)
        CAR.move()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(-car.CHECK,6,-car.MOVEMENT+0.1,-car.ROTATECAMERA,6,-car.ROTATECAMERAZ,0,1,0)
        #glRotatef(ROTATE, 0, 1, 0)
        
        # RENDER OBJECT
        
       # glTranslate(tx/20., ty/20., -zpos)
        #glRotate(ry, 1, 0, 0)
        #glRotate(rx, 0, 1, 0)
     
        #srf.blit(carImage,(8,0))
        
        glCallList(obj.gl_list)
        glPushMatrix()
        glTranslate(-CAR.CHECK, 0,-CAR.MOVEMENT )
        
        glCallList(CAR.obj3.gl_list)
        glPopMatrix()
##        glTranslate(-CHECK, 0,-MOVEMENT )
##        glRotate(ROTATE, 0, 1, 0)
##        
##        
##        glCallList(obj2.gl_list)
##        
        #car.drawCar()
        car.rotate()
       
        glCallList(car.obj2.gl_list)
       
        clock.tick(30)
        #obj.translate(0,0,-MOVEMENT)
       
        pygame.display.flip()

   
main()    
