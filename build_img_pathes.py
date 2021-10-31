import os
import random

IMAGES_DIR = "data\\train\\images"
ft = open("data\\train\\train.txt", 'w')
fv = open("data\\train\\valid.txt", 'w')

for root, dirs, files in os.walk(IMAGES_DIR):
    for file in files:
        n = random.random()
        if n > 0.15:
            ft.write(os.path.abspath(os.path.join(root, file)) + '\n')
        else:
            fv.write(os.path.abspath(os.path.join(root, file)) + '\n')

ft.close()
fv.close()
