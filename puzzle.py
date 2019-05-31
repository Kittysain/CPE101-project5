#Project5
#Name: Kitty Zhuang and Branyt Williamson
#Instructor: Einakian
#Section: 1

################################################

import sys
args = sys.argv

# This is a function to group the RGB colors in a list.

def groups_of_3(list1):

    num_slices = int(len(list1))//3
    residual = int(len(list1))%3
    new_list = [list1[3*i : ((i+1)*3)] for i in range(num_slices)]
    if residual != 0:
        new_list.append(list1[num_slices*3:])
    return new_list

# Terminate the program for incorrect argument
if len(args) != 2:
    print('Please enter the image file name.')
    exit()

try:
    # This part is to re-organize the information stored in the image file into a list.
    fin = open(args[1])

    list_values = []
    for lines in fin:
        # The values after split would be in type str
        values = lines.split()
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

    # Separate the RBG values into groups for each pixel
    rgb_values = list_values[4:]
    rgb_group = groups_of_3(rgb_values)

    # Decode the color component
    new_image = []
    for pixel in rgb_group:

        pixel[0] *= 10
        if pixel[0] > 255:
            pixel[0] = '255'
        else:
            pixel[0] = str(pixel[0])
        pixel[1] = pixel [0]
        pixel[2] = pixel [0]
        new_image.append(pixel)
    fin.close()

    # Output the solved image
    fout = open('hidden.ppm', 'w')
    fout.write(str(header)+'\n'+str(width)+' '+str(height)+'\n'+str(maximum)+'\n')
    # Write the list formatted pixel to a string formatted.
    s = ''
    for pixel in new_image:
        for item in pixel:
            fout.write(str(item)+'\n')
    fout.close()

except:
    print('Unable to open',args[1])
