from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from PIL import Image
def draw_quadrilateral_on_image(image_path, points,points2, color):
    with Image.open(image_path) as img:
        img = Image.new('RGB',img.size,(0,0,0))
        for i in range(0, len(points)):

            draw = ImageDraw.Draw(img)
        
            draw.polygon(points[i], outline=color, fill=color)
        img = img.rotate(-90,expand=True)
        
        for j in range(0, len(points2)):
            draw = ImageDraw.Draw(img)
            draw.polygon(points2[j],outline=color,fill=color)
        img = img.rotate(-270,expand=True)
        img.save("output_path")
        return "output_path"

