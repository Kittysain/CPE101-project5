#Project5
#Name: Kitty Zhuang and Branyt Williamson
#Instructor: Einakian
#Section: 1

################################################
import sys
import puzzle
import fade
import blur
args = sys.argv

if len(args) == 2 and args[1] =='puzzle.ppm':
    puzzle.puzzle_func()

elif len(args) == 5:
    fade.fade_func()

elif len(args) == 3:
    blur.blur_func()

