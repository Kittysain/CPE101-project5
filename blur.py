
# Project5
# Name: Kitty Zhuang and Branyt Williamson
# Instructor: Einakian
# Section: 1

################################################

import sys
args = sys.argv

# This is a function to group the RGB colors in a list.
def blur_func():
    def groups_of_3(list1):
        num_slices = int(len(list1)) // 3
        residual = int(len(list1)) % 3
        new_list = [list1[3 * i: ((i + 1) * 3)] for i in range(num_slices)]
        if residual != 0:
            new_list.append(list1[num_slices * 3:])
        return new_list

# Terminate the program for incorrect argument

    if len(args) == 3 and (args[2].isdigit() == True):
        reach = int(args[2])
    elif len(args) == 3 and args[2].isdigit() != True:
        print('Usage: python3 blur.py <image> <blur reach>')
        exit()
    else:
        reach = 4

    try:
    # This part is to re-organize the information stored in the image file into a list.
        fin = open(args[1])
        list_values = []
        for lines in fin:
            values = lines.split()  # values would be a list of strings
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

    # Calculate the average color component value for each pixel.
        def index_list(reach,index,width,height):
            matrix_reach = []
            for x in range(-reach, reach + 1):
                for y in range(-reach, reach + 1):
                    matrix_reach.append([x, y])
            row = index//width
            col = index%width
            index_list = []
            for item in matrix_reach:
                n_row = row + item[0]
                n_col = col + item[1]
                if (n_row >= 0 and n_row < height) and (n_col >=0 and n_col < width):
                    new_index = n_row * width + n_col
                    index_list.append(new_index)
            return index_list



        new_image = []
        for i in range(len(rgb_group)):
            index_list_1 = index_list(reach,i,width,height)
            box = [rgb_group[x] for x in index_list_1]
            red = 0
            green = 0
            blue = 0
            for item in box:
                red += item[0]
                green += item[1]
                blue += item[2]
            r_ave = int(red / (len(box)))
            g_ave = int(green / (len(box)))
            b_ave = int(blue / (len(box)))
            new_pixel = [r_ave,g_ave,b_ave]
            new_image.append(new_pixel)

        fin.close()

    # Output the solved image
        fout = open('blur.ppm', 'w')
        fout.write(str(header)+'\n'+str(width)+' '+str(height)+'\n'+str(maximum)+'\n')
    # Write the list formatted pixel to a string formatted.

        for pixel in new_image:
            for item in pixel:
                fout.write(str(item)+'\n')
        fout.close()


    except:
        print('Unable to open ' + args[1])

