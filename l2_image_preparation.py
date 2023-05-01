# example of pixel normalization
import numpy
from numpy import asarray
from numpy import clip
from PIL import Image
import matplotlib.pyplot as plt

def print_array_stats(a: numpy.ndarray):
    min, max = pixels.min(), pixels.max()
    mean, std = pixels.mean(), pixels.std()
    print('Mean: %.3f, Standard Deviation: %.3f' % (mean, std))
    print('Min: %.3f, Max: %.3f' % (min, max))

def scale_image(a: numpy.ndarray):
    a = a.astype('float32')
    # normalize to the range 0-1
    a /= 255.0
    mean, std = a.mean(), a.std()
    # global standardization of pixels
    a = (a - mean) / std
    # clip pixel values to [-1,1]
    a = clip(a, -1.0, 1.0)
    # shift from [-1,1] to [0,1] with 0.5 mean
    a = (a + 1.0) / 2.0
    return a

# load image
image = Image.open('img/bondi_beach.jpg')
pixels = asarray(image)
# confirm pixel range is 0-255
print("Original image")
print('pixels Type: %s' % type(pixels))
print('Data Type: %s' % pixels.dtype)
print_array_stats(pixels)
plt.figure(100)
plt.imshow(pixels)

# convert from integers to floats
print("Normilized")
pixels = pixels.astype('float32')
# normalize to the range 0-1
pixels /= 255.0
# confirm the normalization
print_array_stats(pixels)
plt.figure(200)
plt.imshow(pixels)

# calculate global mean and standard deviation
print("Centered (Global mean to 0)")
mean, std = pixels.mean(), pixels.std()
# global centering of pixels
pixels = pixels - mean
# confirm it had the desired effect
print_array_stats(pixels)
plt.figure(300)
plt.imshow(pixels)

# calculate global mean and standard deviation
print("Standartized (mean to 0, variance to 1)")
mean, std = pixels.mean(), pixels.std()
# global standardization of pixels
pixels = (pixels - mean) / std
# confirm it had the desired effect
print_array_stats(pixels)
plt.figure(400)
plt.imshow(pixels)

# shift array values range from [-1:1] to [0:1]]
print("Clipped")
# clip pixel values to [-1,1]
pixels = clip(pixels, -1.0, 1.0)
# shift from [-1,1] to [0,1] with 0.5 mean
pixels = (pixels + 1.0) / 2.0
# confirm it had the desired effect
print_array_stats(pixels)
plt.figure(500)
plt.imshow(pixels)

print("All in one go")
image = Image.open('img/bondi_beach.jpg')
pixels = asarray(image)
print_array_stats(pixels)
pixels = scale_image(pixels)
print_array_stats(pixels)
plt.figure(600)
plt.imshow(pixels)
plt.show()