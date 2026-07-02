# In this question, we decide to calculating area of some shapes for some specific arguments.
# But in this case, we give the names of shapes in a list to function "get_func" and then create a list
# that saves some other functions related to the names of shapes and then return it.
# We then use it to give argument/arguments to the elements of list (area calculator functions) and get 
# the areas of our specific shapes!

import math

def square(side):
    return side ** 2
def circle(radius):
    return math.pi * radius ** 2
def rectangle(length, width):
    return length * width
def triangle(base, height):
    return (base * height) / 2

def get_func(ls):
    funcs = {
        "square": square,
        "circle": circle,
        "rectangle": rectangle,
        "triangle": triangle
    }
    result = [funcs[shape] for shape in ls]
    return result
