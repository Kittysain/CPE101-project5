#Project5
#Name: Kitty Zhuang and Branyt Williamson
#Instructor: Einakian
#Section: 1

################################################

import sys
args = sys.argv
import math

# This is a function to group the RGB colors in a list.

def groups_of_3(list1):

    num_slices = int(len(list1))//3
    residual = int(len(list1))%3
    new_list = [list1[3*i : ((i+1)*3)] for i in range(num_slices)]
    if residual != 0:
        new_list.append(list1[num_slices*3:])
    return new_list

# Terminate the program for incorrect argument

if len(args) != 5 or type(args[1]) != str or args[2].isdigit() != True or args[3].isdigit() != True or args[4].isdigit() != True:
   print('Usage: python3 fade.py <image> <row> <column> <radius>')
   exit()

try:
    # This part is to re-organize the information stored in the image file into a list.
    fin = open(args[1])
    list_values = []
    for lines in fin:
        values = lines.split() #values would be a list of strings
        for i in range(len(values)):
            if values[i].isdigit() == True:
                list_values.append(int(values[i]))
            else:
                list_values.append(values[i])

    # This part assigns variable names to the corresponding information
    header = list_values[0]
    width = list_values[1]
    height = list_values[2]
    maximum = list_values[3]

    row_x = int(args[2])
    col_y = int(args[3])
    radius = int(args[4])

    # Separate the RBG values into groups for each pixel
    rgb_values = list_values[4:]
    rgb_group = groups_of_3(rgb_values)

    new_image = []
    scale_list =[]
    for index in range(len(rgb_group)):
        row = index // width
        col = index % width
        #Calculate the distance each pixel has to the specified point(center of fade)
        distance = math.sqrt((row_x - row)**2 + (col_y - col)**2)
        scale = (radius - distance)/radius
        if scale < 0.2:
            scale = 0.2
        new_pixel = list(map(lambda x:int(x*scale),rgb_group[index]))
        new_image.append(new_pixel)

    fin.close()

    fout = open('fade.ppm','w')
    fout.write(str(header) + '\n' + str(width) + ' ' + str(height) + '\n' + str(maximum) + '\n')
    # Write the list formatted pixel to a string formatted.
    s = ''
    for pixel in new_image:
        for item in pixel:
            fout.write(str(item) + '\n')
    fout.close()

except:
    print('Unable to open'+args[1])
