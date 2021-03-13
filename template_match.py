import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('./files/unimed_boleto-nov.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('./files/template_unimed.png', 0)

height, width = template.shape[::]

res = cv2.matchTemplate(img_gray, template, cv2.TM_SQDIFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = min_loc 
bottom_right = (top_left[0] + width, top_left[1] + height)
cv2.rectangle(img_rgb, top_left, bottom_right, (255, 0, 0), 2)

print('Open image...')
cv2.imshow("Matched image", img_rgb)
cv2.waitKey()
cv2.destroyAllWindows()
