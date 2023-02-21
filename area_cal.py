from roboflow import Roboflow
import numpy as np
import cv2
from glob import glob
import matplotlib.pyplot as plt

rf = Roboflow(api_key="8FfUo7jcgTKpeZmdaK4O")
project = rf.workspace().project("house-uqbjx")
model = project.version(2).model

imgs = glob('google_earth_data/2014/*.jpg')
txtfile = "2014_v2.txt"

with open(txtfile, 'r') as f:
    lines = f.readlines()
    processed_imgs = []
    for line in lines:
        second_row = line.split()[1]
        processed_imgs.append(second_row)

i = len(processed_imgs) + 1


for img in imgs:
    if not img in processed_imgs:
        print("Process {} image in totally {} images".format(i,len(imgs)))
        mask = model.predict(img).num_pixels()
        mask[mask >0 ] = 255
        num_pixels = np.count_nonzero(model.predict(img).num_pixels())

        with open(txtfile, 'a') as f:
            f.write(f'{num_pixels}, {img}\n')
        f.close()

        i += 1
    # # Load two images
    # image = cv2.imread(img)

    # # Create a figure with two subplots
    # fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # # Display the first image in the first subplot
    # axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    # axs[0].set_title('Image')

    # # Display the second image in the second subplot
    # axs[1].imshow(mask)
    # axs[1].set_title('Mask')

    # # Show the figure
    # plt.show()

    





# print(np.count_nonzero(model.predict(img).num_pixels()))
