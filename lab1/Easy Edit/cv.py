import numpy as np 
import imutils
import cv2
import platform
import datetime
import util

print(util.start)
img_path = 'img/'
initial = True
read = False
edited = False
saved = False
img = None
print(util.note)

while True:
    
    #Initial line: menu
    if initial:
        user_input = input(util.menu)
        initial = False
    else:
        user_input = input(">> ")

    #Get Help
    if user_input.strip().lower() == 'h':
        util.printHelp()

    #Save Image
    elif user_input.strip().lower() == 's':
        if read:
            user_input = input(util.enter_outfilename)
            cv2.imwrite(user_input, img)
        saved = True

    #Quit Program
    elif user_input.strip().lower() == 'q':
        user_input = input(util.quit_confirm)
        if user_input == 'y':
            break

    #Read an Image
    elif user_input.strip().lower() == 'read':
        try:
            user_input = input(util.enter_imgname)
            img = cv2.imread(img_path + user_input, 1)
            read = True
            print(img.shape)
            print(util.read_succeed)
            
        except:
            print(util.read_failed)
            print(util.read_failed_note)

    #Show Readed Image
    elif user_input.strip().lower() == 'show':
        if not read:
            print(util.show_failed)
        else:
            cv2.imshow('Image', img)
            cv2.waitKey()
    
    #Rotate Readed Image
    elif user_input.strip().lower() == 'rotate':
        if not read:
            print(util.show_failed)
        else:
            try: 
                user_input = input(util.enter_degree)
                img = util.rotate_image(img, int(user_input.strip()))
                edited = True
                saved = False
            except:
                print(util.rotate_failed)
                print(util.rotate_failed_note)

    #Write Text on Readed Image    
    elif user_input.strip().lower() == 'write':
        if not read:
            print(util.show_failed)
        else:
            try:
                text = input(util.enter_text)
                position = input(util.enter_position)
                color = input(util.select_color)
                cv2.putText(img, text, util.getPosition(position), util.font, 
                util.fontScale, util.getColor(color), util.thickness, cv2.LINE_AA)
                edited = True
                saved = False
            except:
                print(util.write_failed)
                print(util.write_failed_note)
    
    #Print Current Program Status
    elif user_input.strip().lower() == 'status':
        util.printStatus(read, edited, saved)

    #When user hits enter, print system & datetime
    elif user_input.strip().lower() == '':
        print(platform.platform(), datetime.datetime.now())
        print()
    
    #Anything else is unrecognized
    else:
        print('\n\'' + user_input + util.not_recognized)

print(util.program_quit)
print(util.quit_succeed)

