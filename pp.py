import numpy as np
import cv2 as cv2
import easyosr as ez2
import trans_over as to
img = cv2.imread('pp.png') # here put the path of your picture example : r"C:\Users\Hp\Desktop\overlay\rot\cleaned.png"
temp,p1,p2,t1,t2 = ez2.mask_maker('pp.png') # here aswell
mask = cv2.imread(temp, cv2.IMREAD_GRAYSCALE)
dst = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA) 
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("output_path", dst) # here put the path of your output folder where to stock everything
to.over_text_bbox("output_path","output_path",p1,p2,t1,t2) # here put the path of your output folder where to stock everything