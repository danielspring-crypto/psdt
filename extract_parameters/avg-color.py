import cv2
import numpy
import glob
import pandas as pd
path = "images/*.jpg"
images = {}
for fname in glob.glob(path):
    img = cv2.imread(fname)
    avg_row = numpy.average(img, axis=0)
    avg_color = numpy.uint8(numpy.average(avg_row, axis=0))
    images[fname] = avg_color.tolist()
img = pd.DataFrame.from_dict(data=images, orient='index')
img.columns = ['blue', 'green', 'red']
print(img.head())
print(img.describe())