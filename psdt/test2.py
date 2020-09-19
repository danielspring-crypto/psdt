import cv2
import numpy
import glob
import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter import Image
from PIL import ImageTk, Image
import os

root=Tk()
root.title("Currency Detection")


path = "images/500.jpg"
images = {}
for fname in glob.glob(path):
    img = cv2.imread(fname)
    avg_row = numpy.average(img, axis=0)
    avg_color = numpy.uint8(numpy.average(avg_row, axis=0))
    images[fname] = avg_color.tolist()
img = pd.DataFrame.from_dict(data=images, orient='index')
img.columns = ['blue', 'green', 'red']
print(img.head(), sum(images[fname]))
#print(img.describe())  

path = "images/500back.jpg"
images = {}
for fname in glob.glob(path):
    img = cv2.imread(fname)
    avg_row = numpy.average(img, axis=0)
    avg_color = numpy.uint8(numpy.average(avg_row, axis=0))
    images[fname] = avg_color.tolist()
img = pd.DataFrame.from_dict(data=images, orient='index')
img.columns = ['blue', 'green', 'red']
print(img.head(), sum(images[fname]))

path = "images/1000.jpg"
images = {}
for fname in glob.glob(path):
    img = cv2.imread(fname)
    avg_row = numpy.average(img, axis=0)
    avg_color = numpy.uint8(numpy.average(avg_row, axis=0))
    images[fname] = avg_color.tolist()
img = pd.DataFrame.from_dict(data=images, orient='index')
img.columns = ['blue', 'green', 'red']
print(img.head(), sum(images[fname]))  

path = "images/1000back.jpg"
images = {}
for fname in glob.glob(path):
    img = cv2.imread(fname)
    avg_row = numpy.average(img, axis=0)
    avg_color = numpy.uint8(numpy.average(avg_row, axis=0))
    images[fname] = avg_color.tolist()
img = pd.DataFrame.from_dict(data=images, orient='index')
img.columns = ['blue', 'green', 'red']
print(img.head(), sum(images[fname]))   

path = "images/5000.jpg"
images = {}
for fname in glob.glob(path):
    img = cv2.imread(fname)
    avg_row = numpy.average(img, axis=0)
    avg_color = numpy.uint8(numpy.average(avg_row, axis=0))
    images[fname] = avg_color.tolist()
img = pd.DataFrame.from_dict(data=images, orient='index')
img.columns = ['blue', 'green', 'red']
print(img.head(), sum(images[fname])) 

path = "images/5000back.jpg"
images = {}
for fname in glob.glob(path):
    img = cv2.imread(fname)
    avg_row = numpy.average(img, axis=0)
    avg_color = numpy.uint8(numpy.average(avg_row, axis=0))
    images[fname] = avg_color.tolist()
img = pd.DataFrame.from_dict(data=images, orient='index')
img.columns = ['blue', 'green', 'red']
print(img.head(), sum(images[fname])) 

label_text = Label(root, text='Enter Currency: ', width=20)
label_text.grid(row=0, column=0, pady=20)



def click():
    filename = filedialog.askopenfilename(initialdir='/images/', title='Searching', filetypes=(("jpg files", "*.jpg"), ("png files", "*.png")))
    path = filename
    images = {}
    for fname in glob.glob(path):
        img = cv2.imread(fname)
        avg_row = numpy.average(img, axis=0)
        avg_color = numpy.uint8(numpy.average(avg_row, axis=0))
        images[fname] = avg_color.tolist()
    img = pd.DataFrame.from_dict(data=images, orient='index')
    img.columns = ['blue', 'green', 'red']
    print(img.head(), sum(images[fname]))
    img = Image.open(filename)
    width, height = img.size
    img = img.resize((round(350/height*width) , round(350)))
    tkimage = ImageTk.PhotoImage(img)
    myvar= Label(root, image=tkimage)
    myvar.image = tkimage
    myvar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)




    if sum(images[fname]) >= 504 and sum(images[fname]) <= 512:
        label_result = Label(root, text="Result : 500 MMK")
        label_result.grid(row=3, column=0, columnspan=2, pady=20)

    elif sum(images[fname]) >= 466 and sum(images[fname]) <= 498:
        label_result = Label(root, text="Result : 1000 MMK")
        label_result.grid(row=3, column=0, columnspan=2)

    elif sum(images[fname]) >= 521 and sum(images[fname]) <= 582:
        label_result = Label(root, text="Result : 5000 MMK")
        label_result.grid(row=3, column=0, columnspan=2)

    else:
        label_result = Label(root, text="Not Found")
        label_result.grid(row=3, column=0, columnspan=2)

button = Button(root, text='Search ', command=click, width=20, bg='#123456')
button.grid(row=0, column=1, pady=20)

root.mainloop() 