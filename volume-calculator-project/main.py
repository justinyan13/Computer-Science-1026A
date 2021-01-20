"""
Program Overview

Handle prompting and input for different shapes and subsequent output

Prompt user for shape
    Convert user input to all lowercase
    Ensure that input is valid; either first letter or full word
    Print error message and re-prompt if needed
    Continue to prompt user enters quit

Prompt user for necessary dimensions
    Assume that all values are positive floats
    Use correct function in volumes.py to compute the volume

Output message with computed volume
    Store shape and corresponding volume to list
    One list comprised of tuples
        (shape-name, volume)
            cube, pyramid, ellipsoid
        [(“cube”, 1.00), (“cube”,9.00)]

Sort list by low volume-high once user quits
        myList.sort(key = lambda myList: myList[1])
    Print sorted list
        Output: Volumes of shapes entered in sorted order:
            pyramid 42.67
            pyramid 768.00
            cube 1331.00
            ellipsoid 2111.15
        Volumes printed with 2 decimals
    If user quits before entering 1 shape
        Output: No shapes entered.

"""

# Justin Yan #
# jyan388 #
# 251150279 #
# Section 001 #

import volume

# Initialize variables #
shapes_and_volumes = []

# Prompt user for input #
user_shape = (input('Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): ')).lower()

# loops until user quits #
while user_shape not in ['quit', 'q']:
    # evaluates if user enters cube #
    if user_shape in ['cube', 'c']:
        cube_length = float(input('Enter length of side for the cube: '))
        cube_volume = volume.cube_volume_formula(cube_length)
        print('The volume of a cube with side {} is:  {:.2f}'.format(cube_length, cube_volume))
        shapes_and_volumes.append(('cube', cube_volume))

    # evaluates if user enters pyramid #
    elif user_shape in ['pyramid', 'p']:
        pyramid_base = float(input('Enter the base of the pyramid: '))
        pyramid_height = float(input('Enter the height of the pyramid: '))
        pyramid_volume = volume.pyramid_volume_formula(pyramid_base, pyramid_height)
        print('The volume of a pyramid with base {}and height {} is:   {:.2f}'.format(pyramid_base, pyramid_height,
                                                                                      pyramid_volume))
        shapes_and_volumes.append(('pyramid', pyramid_volume))

    # evaluates if user enters ellipsoid #
    elif user_shape in ['ellipsoid', 'e']:
        ellipsoid_r1 = float(input('Enter the first radius: '))
        ellipsoid_r2 = float(input('Enter the second radius: '))
        ellipsoid_r3 = float(input('Enter the third radius: '))
        ellipsoid_volume = volume.ellipsoid_volume_formula(ellipsoid_r1, ellipsoid_r2, ellipsoid_r3)
        print('The volume of an ellipsoid with radii {} and {} and {} is:  {:.2f}'.format(ellipsoid_r1, ellipsoid_r2,
                                                                                          ellipsoid_r3,
                                                                                          ellipsoid_volume))
        shapes_and_volumes.append(('ellipsoid', ellipsoid_volume))
    # re prompt user if invalid input #
    else:
        print('      -- invalid input: enter (quit/q, cube/c, pyramid/p, ellipsoid/e')
        user_shape = input('Please enter shape: ').lower()
        continue

    # re-prompts user for input #
    user_shape = (input('Please enter shape (quit/q, cube/c, pyramid/p, ellipsoid/e): ')).lower()

else:
    if not shapes_and_volumes:
        print('Output: No shapes entered.')
    else:
        shapes_and_volumes.sort(key=lambda x: x[1])
        print('Output: Volumes of shapes entered in sorted order:')
        for x in shapes_and_volumes:
            print(x[0], format(x[1], '.2f'))
