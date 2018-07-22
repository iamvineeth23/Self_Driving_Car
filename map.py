# Map for self driving car

# Importing the libraries
import numpy as np
from random import random, randint
import matplotlib.pyplot as plt
import time

# Importing the Kivy packages
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.config import Config
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

#Configuring mouse
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

#points for drawing map
last_x = 0
last_y = 0
n_points = 0
length = 0

# Initializing the map
first_update = True
def init():
    global sand
    global goal_x
    global goal_y
    sand = np.zeros((longuer, largeur))
    goal_x = 20 #x-coordinate of Upper-right corner of map
    goal_y = largeur-20 # y-coordinate of Upper-right corner of map
    first_update = False

last_distance = 0

class Car(Widget):
    
    angle = NumericProperty(0) #angle btw the x-axis of the map and the axis of the car
    rotation = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    sensor1_x = NumericProperty(0)
    sensor1_y = NumericProperty(0)
    sensor1 = ReferenceListProperty(sensor1_x, sensor1_y)
    sensor2_x = NumericProperty(0)
    sensor2_y = NumericProperty(0)
    sensor2 = ReferenceListProperty(sensor2_x, sensor2_y)
    sensor3_x = NumericProperty(0)
    sensor3_y = NumericProperty(0)
    sensor3 = ReferenceListProperty(sensor3_x, sensor3_y)
    signal1 = NumericProperty(0)
    signal2 = NumericProperty(0)
    signal3 = NumericProperty(0)
    
    def move(self, rotation):
        self.pos = Vector(*self.velocity) + self.pos #updating position acc. to last pos. and vel.
        self.rotation = rotation #getting roation of car
        self.angle = self.angle + self.rotation # updating the angle
        self.sensor1 = Vector(30,0).rotate(self.angle) + self.pos #updating pos. of sensor1
        self.sensor2 = Vector(30,0).rotate((self.angle+30)%360) + self.pos #updating pos. of sensor2
        self.sensor3 = Vector(30,0).rotate((self.angle-30)%360) + self.pos #updating pos. of sensor3
        
        self.signal1 = int(np.sum(sand[int(self.sensor1_x)-10:int(self.sensor1_x)+10, int(self.sensor1_y)-10:int(self.sensor1_y)+10]))/400.
        self.signal2 = int(np.sum(sand[int(self.sensor2_x)-10:int(self.sensor2_x)+10, int(self.sensor2_y)-10:int(self.sensor2_y)+10]))/400.
        self.signal3 = int(np.sum(sand[int(self.sensor3_x)-10:int(self.sensor3_x)+10, int(self.sensor3_y)-10:int(self.sensor3_y)+10]))/400.
        
        # Boundary Conditions
        if self.sensor1_x > longuer-10 or self.sensor1_x < 10 or self.sensor1_y > largeur-10 or self.sensor1_y < 10:
            self.signal1 = 1.
        if self.sensor2_x > longueur-10 or self.sensor2_x<10 or self.sensor2_y>largeur-10 or self.sensor2_y<10: 
            self.signal2 = 1.
        if self.sensor3_x > longueur-10 or self.sensor3_x<10 or self.sensor3_y>largeur-10 or self.sensor3_y<10:
            self.signal3 = 1. 
    
class Ball1(Widget):
    pass
class Ball2(Widget):
    pass
class Ball3(Widget):
    pass
    
    
    
    
    
    
    