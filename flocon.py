# -*- coding: utf-8 -*-

import sys
import math
import tkinter as Tk


def main(argv):
    """
    program usage:
        python flocon.py <deepness_max>
    Where deepnass_max is the recursivity limit. 2 is good while
    you're developping, 3 or 4 is good to test. Then you can play
    as you want 'to see what happen'.

    Parameters
    ----------
    argv : list of string -- sys.argv
        argv is the vector of parameters passed to the programm,
        the first parameter (argv[0]) is always the name of the
        program. Here it is "flocon.py"

    Returns
    -------
    None.

    """

    # Here we define the tk window
    window = Tk.Tk()
    window.title("Un flocon de neige")

    window_height = 1000
    window_width = 1000
    window_center = (window_width / 2, window_height / 2)

    # The canvas
    canvas = Tk.Canvas(window,
                       bg='dark blue',
                       height=window_height,
                       width=window_width
                       )

    # We take care of the parameter here
    deepness_max = 4
    if (len(argv) > 1):
        deepness_max = int(argv[1])

    # Let's define the first triangle
    p0 = [100, 270]
    p1 = [900, 270]
    # TODO: /!\ it's your job to define the following function
    p2 = get_third_point_equilateral(p0, p1, [0, 1])

    # Then we we draw that triangle onto the canvas
    canvas.create_polygon([p0, p1, p2], fill='white')

    # Let's do the recursion! We will call the on each side of the triangle.
    # We'll need the vector p0_p2_direction_normed in order to know in which
    # direction to draw the third point (we want it to be turned in direction
    # of the exterior and not the interior).

    # /?\ note: the direction to draw the next point in the triangle is
    # given by the vector going from the opposite point of the current
    # triangle (p2) to the middle of p0p1.
    p0_p1_middle = [0, 0]  # TODO: that's your job to find those coordinates
    # TODO: write the function normalize_vector that gives the vector that
    # goes in the same direction as the input vector but of length 1.
    direction_p0_p1_side = normalize_vector(p2, p0_p1_middle)
    # TODO: complete the function flocon
    flocon(
        canvas,
        p0,
        p1,
        direction_p0_p1_side,
        0,
        deepness_max=deepness_max
    )

    # TODO: Congratz! you did the job for the first side of the triangle p0p1.
    # now you just have to do the same for the two other sides p1p2 and p2p0.
    # Most of the work is done, it should be easy.

    canvas.pack()

    window.mainloop()


def flocon(canvas, p0, p1, direction, deepness, deepness_max=4):
    """
    The recursive function that drows the snowflake.

    Parameters
    ----------
    canvas : tk.Canvas
        The canvas in which we draw.
    p0 : [x,y]
        x,y coordinates of the first point of the new triangle
    p1 : [x,y]
        x,y coordinates of the second point of the new triangle
    direction : [x,y]
        normalized vector giving the direction to draw the new triangle
    deepness : int
        current deepness for stop-condition.
    deepness_max : int, optional
        max deepness for the recursion, this is our stop-condition.
        The default is 0.

    Returns
    -------
    None.

    """
    # TODO: As this function is the heart of the logic of this prorgram it's
    # up to you to write it from a to z. Don't worry, if you are there you
    # should have an idea about what to do now. After all, you already did it
    # once! :-)

    # TODO: complete this function


def normalize_vector(p0, p1):
    """
    Compute the normalized vector of p0p1

    Parameters
    ----------
    p0 : [x,y]
        Coordinates of the first point
    p1 : [x,y]
        Coordinates of the second point

    Returns
    -------
    vector_normed : [x,y]
        The normalization of p0p1
    """
    # TODO: complete this function
    # You have two points that give you the start and the end of the initial
    # vector. Nevertheless, the length of that vector is not guaranted to be 1.
    # To normalize a vector you'll have to divide its coordinates by its own
    # length
    vector = (p1[0] - p0[0], p1[1] - p0[1])
    length = math.sqrt(vector[0]**2 + vector[1]**2)
    vector_normed = (vector[0]/length, vector[1]/length)
    return vector_normed


def get_third_point_equilateral(p0, p1, direction):
    """
    Get the third point to make an equilateral triangle.

    Parameters
    ----------
    p0 : [x,y]
        Coordinates of the first point
    p1 : [x,y]
        Coordinates of the second point
    direction : [x,y]
        The normalized vector that gives the direction of the third point

    Returns
    -------
    p2 : [x,y]
        Coordinates of the third point

    """
    p2 = [100, 470]  # This is obviously not the right coordinates
    # TODO: complete this function
    # You want to find the first point that makes an equilateral triangle with
    # p0 and p1, furthemore, actually there is 2 solutions, but you also have
    # the vector of length 1 that gives you the direction to the 3rd point from
    # the mid point of p0p1.
    length = math.sqrt((p1[0]-p0[0])**2 + (p1[1]-p0[1])**2)
    hop = math.sqrt(length**2 - (length/2)**2)
    middle_to_third_point = (direction[0]*hop, direction[1]*hop)
    middle = ((p0[0] + p1[0])/2, (p0[1] + p1[1])/2)
    p2 = (middle[0] + middle_to_third_point[0], middle[1] + middle_to_third_point[1])
    return p2


if __name__ == "__main__":
    main(sys.argv)
