from turtle import Turtle

class Screen:
    def __init__(self, t, w, h, down, up, left, right):
        self.turtle = t
        self.width = w
        self.height = h
        self.y_min = down
        self.y_max = up
        self.x_min = left
        self.x_max = right
        self.functions = [] 

    def draw_axes(self):
    # equation is y
        y_axis_offset = Screen.calculate_pixel_offset(self.width, self.x_min, self.x_max) 
        if abs(y_axis_offset) < self.width/2:
            self.turtle.home()
            self.turtle.teleport(y_axis_offset, self.height/2)
            self.turtle.goto(y_axis_offset, -self.height/2)
        x_axis_offset = Screen.calculate_pixel_offset(self.height, self.y_min, self.y_max)
    
        self.turtle.penup()

        if abs(x_axis_offset) < self.height/2:
            self.turtle.home()
            self.turtle.pendown()
            self.turtle.teleport(self.height/2, x_axis_offset)
            self.turtle.goto(-self.height/2, x_axis_offset)

# TODO: make it do the tick tolerances based on offset
    def draw_ticks(self, y_tick_scaling: float, x_tick_scaling: float, tick_size: int) -> None:
        """Draws ticks based on the width and height and scaling factors"""
        x_axis_offset = Screen.calculate_pixel_offset(self.height, self.y_min, self.y_max)
        x_per_pixel = (abs(self.x_max) + abs(self.x_min))/self.width
        for i in range(int(-self.width/2), int(self.width/2)):
            if abs(x_per_pixel * i - self.x_min) % x_tick_scaling < 0.034:
                self.turtle.penup()
                self.turtle.teleport(i, x_axis_offset+tick_size)
                self.turtle.pendown()
                self.turtle.goto(i, x_axis_offset-tick_size)
        y_axis_offset = Screen.calculate_pixel_offset(self.width, self.x_min, self.x_max) 
        y_per_pixel = (abs(self.y_max) + abs(self.y_min))/self.height
        for y in range(int(-self.height/2), int(self.height/2)):
            if abs(y_per_pixel * y - self.y_min) % y_tick_scaling < 0.034:
                self.turtle.penup()
                self.turtle.teleport(y_axis_offset+tick_size, y)
                self.turtle.pendown()
                self.turtle.goto(y_axis_offset-tick_size, y)

    def calculate_pixel_offset(width, lower_bound, upper_bound):
        new_center_x = (lower_bound+upper_bound)/2
        return -new_center_x/((abs(lower_bound) + abs(upper_bound))/width)
    
    def graph_function(self, function):
        is_offscreen = True
        actual_x = self.x_min
        x_per_pixel = abs(self.x_max-self.x_min)/self.width
        for display_x in range(-int(self.width/2), int(self.width/2)):
            actual_y = function(actual_x)
            actual_x += x_per_pixel
            if actual_y > self.y_max or actual_y < self.y_min:
                is_offscreen = True
                continue
            else:
                center_y = (self.y_max + self.y_min)/2
                offset = abs(self.y_max-self.y_min)/self.height
                display_y = (actual_y-center_y) / offset
                if is_offscreen:
                    self.turtle.penup()
                    is_offscreen = False
                else:
                    self.turtle.pendown()
                self.turtle.goto(display_x,display_y)

    def add_function(self,fn):
        self.functions.append(fn)

    def set_screen(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def render(self):
        self.turtle.reset()
        self.turtle.pensize(2)
        self.turtle.speed(0)
        self.draw_axes()
        self.draw_ticks(1,1,5)
        self.turtle.penup()
        self.turtle.pencolor("green")
        self.turtle.pendown()
        for f in self.functions:
            self.graph_function(f)


def num_derive(x:float, math_function) -> float:
    derive = (math_function(x+0.0000001)-math_function(x))/0.0000001

    return round_to_thousandths(derive)

def tangent_line(slope, x1, y1):
    def line_function(x): # y - y1 = slope(x-x1)
        # y = slopex-slopex1+y1
        return slope*x -x1*slope+y1
    
    return line_function
    
# we want to return a function with 1 parameter (x) for the graph_function method
def derivative_function(function):
    def derivative(x):
        return num_derive(x, function)
    
    return derivative

# gives net change
def calculate_integral(x_min, x_max, func):
    integral = 0
    x = x_min
    while x < x_max:
        y = func(x)
        integral += y * 0.00001
        x += 0.00001
    return round_to_thousandths(integral)

def round_to_thousandths(value):
    return round(value*1000)/1000