import numpy as np 
import cv2

start = 'Initializing Program ...  \n'
program_quit = '\nProgram Exiting ...\n'
quit_succeed = 'Exit Succeed\n'
note = '*NOTE: All image are in the img folder, input should be in format of img_name.img_type.\n'
menu = '[h] Help, [s] Save, [q] Quit \n\n'
quit_confirm = '\nSure to Quit? All unsaved changes will be lost. Enter: [y] Yes, [n] No \n\n'
enter_imgname = '\nEnter Image Name: \n\n'
enter_outfilename = '\nEnter Output Image Name: \n\n'
enter_text = '\nEnter text: \n\n'
enter_position = '\nEnter position: \n\n'
enter_degree = '\nEnter rotation degree: \n\n'
select_color = '\nSelect color: [Red] [Green] [Blue]\n\n'
read_succeed = '\nImage Successfully Read\n'
read_failed = '\nImage Failed to Read'
show_failed = '\nNo Image Read \n'
write_failed = '\nFailed to Write Text on Read Image\n'
rotate_failed = '\nImage Failed to Rotate'
rotate_failed_note = '*NOTE: Please Double Check the Rotate Degree entered, and Re-enter \'rotate\' Command. The Value Should be type of int.\n'
read_failed_note = '*NOTE: Please Double Check Image Name and Type entered, and Re-enter \'read\' Command \n'
write_failed_note = '*NOTE: Please Double Check the Position entered, and Re-enter \'write\' Command. The Value Should be 2 Integer [int, int].'
not_recognized = '\' Is Not Recognized. Type \'h\' for Help \n'
help_read = 'Enter \'read\' to read an image'
help_show = 'Enter \'show\' to show the read image'
help_write = 'Enter \'write\' to write text on the read image'
help_rotate = 'Enter \'rotate\' to rotate the read image'
help_status = 'Enter \'status\' to show the current program state'
help = [help_read, help_show, help_write, help_rotate, help_status]

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
red = (0,0,255)
green = (0,255,0)
blue = (255,0,0)
thickness = 2

def printHelp():
    print()
    for h in help:
        print(h)
    print()

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

def getPosition(position):
    xy = position.split(',')
    return (int(xy[0].strip()), int(xy[1].strip()))

def getColor(color):
    if color.strip().lower() == 'red':
        return red
    elif color.strip().lower() == 'green':
        return green
    elif color.strip().lower() == 'blue':
        return blue
    else:
        return (0,0,0)

def printStatus(read, edited, saved):
    if read:
        if edited:
            if saved:
                print('\nImage is Read, Image Has Been Modified, All Change(s) Saved\n')
            else:
                print('\nImage Readed, Image Has Been Modified, Change(s) are not Saved\n')
        else:
            print('\nImage Readed, Image Has Not Been Modified.\n')
    else:
        print('\nNo Image is Read\n')