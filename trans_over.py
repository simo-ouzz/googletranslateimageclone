from deep_translator import GoogleTranslator
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
def calculate_X(points):
     x1 = (points[0][0] +points[2][0])/2
     x2 = (points[1][0] +points[3][0])/2
     X = (x1+x2)/2
     return points[0][0]

def calculate_Y(points):
     y1 = (points[0][1] +points[2][1])/2
     y2 = (points[1][1] +points[3][1]-90)/2
     Y = (y1+y2)/2
     return Y
def get_pixel_color(image_path, x, y):
    # Open the image file
    img = Image.open(image_path)
    
    # Convert image to RGB mode if not already
    img = img.convert('RGB')
    
    # Get the color of the pixel
    color = img.getpixel((x, y))
    
    return color
def translate(text):
    translated = GoogleTranslator(source='auto', target='ar').translate(text)
    return translated

def over_text_bbox(image_path,output_path,p1,p2,t1,t2):
    image = Image.open(image_path)

# Create a drawing context
    for i in range(0, len(p1)):
        draw = ImageDraw.Draw(image)
        if len(t1[0]) > 15 or len(t1[1]) < 15:
            font_size = 23
        else:
            font_size = 15
        font = ImageFont.truetype(r"C:\Users\Hp\Desktop\overlay\arabic_font.ttf", font_size)
        text = text = translate(t1[i])
        if get_pixel_color(image_path,1,1) == (255,255,255):    
            text_color = (0,0,0)
        else:
            text_color = (255, 255, 255) 
        position = (calculate_X(p1[i]), calculate_Y(p1[i])) 

# Add text to the image
        draw.text(position, text,fill = text_color, font=font)
    image = image.rotate(-90,expand=True)        
    for i in range(0, len(p2)):
        if i == 0:
            font_size = 23
        else:
            font_size = 15
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(r"C:\Users\Hp\Desktop\overlay\arabic_font.ttf", 19)
        text = translate(t2[i])
        if get_pixel_color(image_path,1,1) == (255,255,255):    
            text_color = (0,0,0)
        else:
            text_color = (255, 255, 255) 
        position = (calculate_X(p2[i]), calculate_Y(p2[i])) 

    
        draw.text(position, text,fill = text_color, font=font)

    image = image.rotate(-270,expand=True)
    image.save(output_path)
    print("image saved succefully")
