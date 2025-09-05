#!/usr/bin/env python3
"""
Assignment 2 - Q3
Recursive Function Program - Create Geometric Pattern via Turtle

Functionality Explanation:

Firstly, the user inputs three variables:
- no of sides
- side length in px
- recursion depth

Lnegth divided into thirds with length /= 3.0

For each edge at depth d>0 the code completes the following steps:
1. divides the length by 3
2. draws lines of length as per step 1, turning the following angles between each 1/3 length line:
- left 60 degrees, right 120 degrees, left 60 degrees.
- However, if the depth=0, it draws a straight line.

"""
import turtle

def draw_koch_segment(t, length, depth):
    if depth == 0:
        t.forward(length)
        return
    length /= 3.0
    draw_koch_segment(t, length, depth-1)
    t.left(60)
    draw_koch_segment(t, length, depth-1)
    t.right(120)
    draw_koch_segment(t, length, depth-1)
    t.left(60)
    draw_koch_segment(t, length, depth-1)

def draw_polygonal_koch(sides, side_length, depth):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    screen = turtle.Screen()
    screen.title("Assignment 2 - Q3 Turtle Drawing")
    exterior_angle = 360.0 / sides
    t.up()
    t.goto(-side_length/2, side_length/3)
    t.down()
    for _ in range(sides):
        draw_koch_segment(t, side_length, depth)
        t.right(exterior_angle)
    turtle.done()

def main():
    try:
        sides = int(input("Please enter the number of sides (must be >=3): ").strip())
        side_length = float(input("Enter the side length (numbers only, >0): ").strip())
        depth = int(input("Please enter the recursion depth (must be >=0): ").strip())
    except Exception:
        print("Input is invalid. Values entered must be numeric values only.")
        return
    if sides < 3 or depth < 0 or side_length <= 0:
        print("Some or all of the input values are invalid. All values must be as follows: sides must be >=3, length must be >0 and depth must be >=0")
        return
    draw_polygonal_koch(sides, side_length, depth)

if __name__ == "__main__":
    main()
