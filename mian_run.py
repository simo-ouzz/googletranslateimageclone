import numpy as np
import cv2 as cv2
import easyosr as ez2
import trans_over as to


import tkinter as tk
from tkinter import filedialog

def select_image_path():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    image_path_entry.delete(0, tk.END)
    image_path_entry.insert(0, file_path)

def select_output_path():
    dir_path = filedialog.askdirectory()
    output_path_entry.delete(0, tk.END)
    output_path_entry.insert(0, dir_path)

def get_input_paths():
    image_path = image_path_entry.get()
    output_path = output_path_entry.get()
    return image_path, output_path

root = tk.Tk()
root.title("Image Processor")

image_path_label = tk.Label(root, text="Image Path:")
image_path_label.grid(row=0, column=0)
image_path_entry = tk.Entry(root, width=50)
image_path_entry.grid(row=0, column=1)
image_path_button = tk.Button(root, text="Browse", command=select_image_path)
image_path_button.grid(row=0, column=2)

output_path_label = tk.Label(root, text="Output Path:")
output_path_label.grid(row=1, column=0)
output_path_entry = tk.Entry(root, width=50)
output_path_entry.grid(row=1, column=1)
output_path_button = tk.Button(root, text="Browse", command=select_output_path)
output_path_button.grid(row=1, column=2)

process_button = tk.Button(root, text="Process", command=get_input_paths)  # Replace with your processing function
process_button.grid(row=2, column=1)
image_path, output_path = get_input_paths()
img = cv2.imread(image_path)
temp,p1,p2,t1,t2 = ez2.mask_maker(image_path)
mask = cv2.imread(temp, cv2.IMREAD_GRAYSCALE)
dst = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA) 
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite(output_path, dst)
to.over_text_bbox(output_path,output_path,p1,p2,t1,t2)
root.mainloop()