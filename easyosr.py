import easyocr as ez
import marking as mk
import re
def list_to_tuple(list_of_lists):
    return [tuple(sublist) for sublist in list_of_lists]
def is_string_free_of_numbers(s: str) -> bool:
    # Check if there are any digits in the string
    return not any(char.isdigit() for char in s)

   
def mask_maker(image_path):
    read = ez.Reader(['en'])
    result = read.readtext(image_path)  
    points = []
    text1 = []
    print(result)
    for (bbox, text,prob) in result:
            
        if is_string_free_of_numbers(text):
            
            points.append(list_to_tuple(bbox))
            text1.append(text)
    print(points)
    mk.rotate_image_clockwise(image_path)
    result2 = read.readtext("output_path") # here please when downloading the repo change to the exact paths you have in your machine
    points2 = []
    text2 = []
    for (bbox, text,prob) in result2:    
        print(text)
        if is_string_free_of_numbers(text):
            
            points2.append(list_to_tuple(bbox))

            text2.append(text)
    print(points2)
    color = (255, 255, 255)
    mk.draw_quadrilateral_on_image(image_path,points,points2,color)
    return "output_path",points ,points2,text1,text2
