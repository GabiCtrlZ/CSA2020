import numpy as np
import matplotlib.pyplot as plt

FRAMES_DIVISOR = 719 

with open('outfile.txt', 'r') as f:
    data = f.read()

image = []
i = 0
temp = []
for char in data:
    if i == FRAMES_DIVISOR:
        i = 0
        image.append(temp)
        temp = []
    i += 1
    temp.append(1 if char == '1' else 0)

plt.imshow(image)
plt.imshow(image, cmap='Greys',  interpolation='nearest')
plt.savefig('image.png')