"""
args:
assign the var filname with the path of the image
result:
output a text file
"""
from os.path import splitext
import numpy as np
import matplotlib.image as mpimg
from PIL import Image


# import matplotlib.pyplot as plt
def rgb2gray(rgb):
    """
    args:
    a rgb png image
    result:
    rgb img on the grayscale as an array
    """
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])


filename = "pl2000015029.jpg"
img = Image.open(filename)
img.thumbnail((500, 500), Image.ANTIALIAS)
img.load()
IMG = mpimg.imread(filename)


gray = rgb2gray(np.asarray(img, dtype="int32"))


CHARS = np.asarray(list(' .,:;"*i|rsXA253hMHGS#9B&@'))  # too detailed
# CHARS = np.asarray(list(';irsXA253HG#B&@'))# less detail

CHAR2GRAY_TOLERANCE = [(d+1)/len(CHARS)*gray.max() for d in range(len(CHARS))]

arr = gray.flatten().tolist()

for num, char in enumerate(CHARS):
    if num == len(CHARS)-1:
        for indx, pixl in enumerate(arr):
            try:
                if pixl <= 1:
                    arr[indx] = char

            except Exception:
                pass
    else:
        for indx, pixl in enumerate(arr):
            try:
                if pixl <= CHAR2GRAY_TOLERANCE[num]:
                    arr[indx] = char

            except Exception:
                pass





arr = np.array(arr).reshape(gray.shape)



with open(splitext(filename)[0]+" ASCCIIFIED.txt", 'w') as f:
    f.write("\n".join("".join(row)for row in arr))



#arr=[   type(pix) if not (type(pix)==np.float64)  else"bye"
#  [CHARS[num] if pix <CHAR2GRAY_TOLERANCE[num] else pix][0]


 #for row in arr for pix in row
 #]


# for k in range(len(CHARS)):
#     print("starting with",k)
#     gray2 = np.minimum(gray2, CHAR2GRAY_TOLERANCE[k],CHARS[k])
#
#     # np.where(gray2 < CHAR2GRAY_TOLERANCE[k], CHARS[k], gray2)
#     print("done with {0} so {1} percent left".format(k, k/len(CHARS)))


# print(type(gray[0][0])==np.float64)
# plt.imshow(gray, cmap = plt.get_cmap('gray'))
# plt.show()
