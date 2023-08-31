from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageOps
image = watermark = is_watermarked = None


def open_image():
    global image, is_watermarked
    if image:
        is_watermarked = False
    path = filedialog.askopenfilename(initialdir='/Users/user/Downloads', title='Select Image',
                                      filetypes=(('Jpeg Files', '*.jpg'), ('Png files', '*.png'), ('All files', '*.*')))
    image = Image.open(path)


def open_watermark():
    global watermark, is_watermarked
    if watermark:
        is_watermarked = False
    path = filedialog.askopenfilename(initialdir='/Users/user/Downloads', title='Select Watermark',
                                      filetypes=(('Png files', '*.png'), ('Jpeg Files', '*.jpg'), ('All files', '*.*')))
    watermark = Image.open(path)


def watermark_image():
    global watermark, image, is_watermarked
    if not is_watermarked:
        image = ImageOps.exif_transpose(image)
        image = image.convert('RGBA')
        watermark = watermark.convert('RGBA')
        image_width, image_height = image.size
        watermark.thumbnail((image_width, image_height))
        image.paste(watermark, (0, 0), mask=watermark)
    image_window = Toplevel()
    if image.size[0] > image.size[1]:
        image.thumbnail((1000, 800))
        photo_image = ImageTk.PhotoImage(image)
        canvas = Canvas(master=image_window, width=1000, height=800)
        canvas.pack(fill=BOTH, expand=YES)
        canvas.create_image(500, 400, image=photo_image)
    else:
        image.thumbnail((500, 1000))
        photo_image = ImageTk.PhotoImage(image)
        canvas = Canvas(master=image_window, width=500, height=1000)
        canvas.pack(fill=BOTH, expand=YES)
        canvas.create_image(250, 500, image=photo_image)
    wants_to_save = messagebox.askyesno('Save Image', 'Would you like to save the image?')
    if wants_to_save:
        filename = filedialog.asksaveasfile(mode='w', defaultextension='.png')
        image.save(filename)
        image_window.mainloop()
    else:
        image_window.destroy()
    is_watermarked = True


window = Tk()
window.title('Image Watermarker')

title = Label(text='Image Watermarker', font=('Arial', 40, 'bold'))

title.pack()

image_upload = Button(text='Upload Image', command=open_image)

image_upload.pack()

watermark_upload = Button(text='Upload Watermark', command=open_watermark)

watermark_upload.pack()

show_button = Button(text='Show Watermarked Image', command=watermark_image)

show_button.pack()

window.mainloop()
