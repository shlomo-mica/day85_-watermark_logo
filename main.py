# Import the required Libraries
##import tkinter as tk
from tkinter import Tk, Canvas, Button, filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

# Create an instance of tkinter frame
root = Tk()
root.withdraw()
root.geometry("500x500")
# select file name
select_file_name = filedialog.askopenfilename(initialdir='C:', title='select your file:')
start_button = Button(text="start", height=4, width=15, bg="#C0D850", command="start_timer")
start_button.grid(column=1, row=2)
open_picture = Button(text='b', height=4, width=15, bg='red', command='')
open_picture.grid(row=1, column=1)


def add_watermark(image, wm_text):
    opened_image = Image.open(image)
    image_width, image_height = opened_image.size

    draw = ImageDraw.Draw(opened_image)
    font_size = int(image_width / 8)
    font = ImageFont.truetype('arial.ttf', font_size)
    x, y = int(image_width / 2), int(image_height / 2)
    # add the watermark
    draw.text((x, y), wm_text, font=font, fill='#FFF', stroke_width=5, stroke_fill='#222', anchor='ms')
    # show the picture
    # opened_image.show()
    return opened_image


add_watermark(select_file_name, 'coding succeed')
load_pic = select_file_name
# get an image
with Image.open(load_pic).convert("RGBA") as base:
    # base.show()
    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

    # get a font
    # fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
    fnt = ImageFont.truetype(r'c:\windows\fonts\arial.ttf', 90)

    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text((102, 102), "Hello", fill=(255, 255, 255, 128))
    # draw text, full opacity
    d.text((102, 602), "World", fill=(255, 255, 255, 255))

    # test line from up function
    font_size = int(base.width / 8)
    font = ImageFont.truetype('arial.ttf', font_size)
    d.text((111, 111), "test", font=font, fill='#FFF', stroke_width=5, stroke_fill='#222', anchor='ms')

    out = Image.alpha_composite(base, txt)
    canvas = Canvas(root, width=350, height=350, bg='black')
    # canvas.pack()

    # im = Image.open(select_file_name)
    canvas.image = ImageTk.PhotoImage(out)
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')

    out.show()

# Assuming you have an existing PIL image (e.g., 'img2')
img = Image.open('IMG_20210427_105613.jpg')


def draw_water_mark(image_to_draw):
    draw = ImageDraw.Draw(image_to_draw)
    # Now you can use various drawing methods, such as:
    draw.line((11, 11, 11, 11), fill='green')
    # draw.rectangle((22, 22, x2, y2), outline=color, width=thickness)
    draw.text((44, 55), "Your text 101", fill='#FFF', font=fnt)

    # Example: Draw a red rectangle
    draw.rectangle((10, 10, 100, 100), outline="red", width=2)

    # Save or display the modified image
    img.save("modified_image100.jpg")

    print("Rectangle drawn on the image!")


# Remember to adjust coordinates, colors, and other parameters as needed.
draw_water_mark(img)

root.deiconify()
root.mainloop()

# try with PIL


# show the root again


# def open_my_picture():
#     with Image.open(select_file_name) as im:
#         # im.show()
#         im.rotate(45).show()

# Create a canvas

# canvas = Canvas(root, width=350, height=350)
# canvas.pack()
# im = Image.open(select_file_name)
# canvas.image = ImageTk.PhotoImage(im)
# canvas.create_image(0, 0, image=canvas.image, anchor='nw')

# canvas.grid(row=2, column=2)
# s="tomato.png"
# photo = tk.PhotoImage(file=s)
# canvas.create_image(300, 300, image=photo)
