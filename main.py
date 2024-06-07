from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont

# loading Python Imaging Library


# To get the dialog box to open when required
from tkinter import filedialog


def open_img():
    global x, img
    # Select the Imagename  from a folder
    x = openfilename()

    # opens the image
    img = Image.open(x)

    # resize the image and apply a high-quality down sampling filter
    img = img.resize((550, 550), Image.LANCZOS)

    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)

    print(type(img))

    # create a label
    panel = Label(root, image=img, text="root1")

    # set the image as img
    panel.image = img
    panel.grid(row=2)


def openfilename():
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    filename = filedialog.askopenfilename(title='OPEN')
    return filename


def add():
    pic = Image.open(x)
    return draw_water_mark(pic)


fnt = ImageFont.truetype(r'c:\windows\fonts\arial.ttf', 90)
# img_new = Image.open(r'C:\Users\shlom\PycharmProjects\day85_-watermark_logo\IMG_20210427_105613.jpg')
# img_new.show()


# "C:\Users\shlom\PycharmProjects\day85_-watermark_logo\modified_image100.jpg"
def draw_water_mark(pic):
    draw = ImageDraw.Draw(pic)
    # Now you can use various drawing methods, such as:
    draw.line((11, 11, 11, 11), fill='green')
    # draw.rectangle((22, 22, x2, y2), outline=color, width=thickness)
    draw.text((44, 55), "Your text 103", fill='#FFF', font=fnt)

    # Example: Draw a red rectangle
    draw.rectangle((10, 10, 100, 100), outline="red", width=2)

    # Save or display the modified image
    pic.save(r'C:\Users\shlom\PycharmProjects\day85_-watermark_logo\modified_image105.jpg')

    print("Rectangle drawn on the image!")


# test function without usig the add button
#draw_water_mark(img_new)
# Create a window
root = Tk()

# Set Title as Image Loader
root.title("Image Loader")

# Set the resolution of window
root.geometry('900x700')

# Allow Window to be resizable
root.resizable(width=True, height=True)

# Create a button and place it into the window using grid layout

Button(root, text='add water mark', command=add).grid(row=1, column=1)
Button(root, text='open image', command=open_img).grid(row=1, column=2)
root.mainloop()
