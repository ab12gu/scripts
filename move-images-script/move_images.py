###
# Name: move_images.py
#
# by: Abhay Gupta
#
# Description: move all images to a single folder
#
###

import os

def move_images():
    print("world")

    rootdir = './'
    directory = 'all_images/'
    os.mkdir(rootdir + directory)

    # iterate through directory and move images to single folder
    for subdir, dir, files in os.walk(rootdir):
        for file in files:
            if not file.endswith("json"):
                file_path = os.path.join(subdir,file)
                print(file_path)

                #os.rename(file_path, file_path.replace('all_images', ''))
                os.rename(file_path, directory + file)

if __name__ == "__main__":
    print("hello")

    move_images()
