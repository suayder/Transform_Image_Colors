import numpy as np
import cv2
import sys

def reduce(image, bitNumber):
    image[:,:,0] = np.bitwise_and(image[:,:,0], bitNumber)
    image[:,:,1] = np.bitwise_and(image[:,:,1], bitNumber)
    image[:,:,2] = np.bitwise_and(image[:,:,2], bitNumber)

    return image


def grayscale(x):
    pass
'''    mat = np.sum(np.multiply(image[:,:,0], 0.3), np.multiply(image[:,:,1], 0.59))
    mat - np.sum(mat, np.multiply(image[:,:,2], 0.11))
    for i in range(0,len(image[0,:])):
        for j in range(0,len(image[:,0])):
            image[i,j,0] = mat[i,j]
            image[i,j,1] = mat[i,j]
            image[i,j,2] = mat[i,j]'''

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv)>4:
        print("compile like this, python colorReducing.py 'option(1|2)' 'image path'")
        print("if option 1, compile like this, python colorReducing.py 1 'number color (16|8|4|2)' 'image path'")
    else:
        if(len(sys.argv)==2):
            if(sys.argv[1]=='2'):
                im = cv2.imread("/home/suayder/Pictures/Lenna.png", cv2.IMREAD_GRAYSCALE)
            else:
                print("wrong parameters")
                exit()

        elif(len(sys.argv)==3):
            if(sys.argv[1]=='1'):
                im = cv2.imread("/home/suayder/Pictures/Lenna.png", cv2.IMREAD_COLOR)
            elif sys.argv[1]=='2':
                im = cv2.imread(sys.argv[2], cv2.IMREAD_GRAYSCALE)
        else:
            if(len(sys.argv)==4 and sys.argv[1] == '2'):
                print("wrong parameters")
                exit()
            im = cv2.imread(sys.argv[3], cv2.IMREAD_COLOR)

        if(sys.argv[1]=='2'):
            #gui = Tk();
            #slider = Scale(gui, orient = HORIZONTAL).pack
            cv2.namedWindow('image')
            cv2.moveWindow('image', 400,0)
            cv2.createTrackbar("Track_Bar", 'image', 30, 255, grayscale)
            while True:
                k = cv2.waitKey(1)
                if(k==27):
                    break;

                scale = cv2.getTrackbarPos("Track_Bar", 'image')
                image = np.divide(im, scale+30);
                cv2.imshow('image', image);
            cv2.destroyAllWindows()

        else:
            if(sys.argv[2]=='0'):
                value = 255
            elif(sys.argv[2] == '2'):
                value = 128
            elif(sys.argv[2]=='4'):
                value = 192
            elif (sys.argv[2]=='8'):
                value = 224
            elif (sys.argv[2] == '16'):
                value = 240
            else:
                print("Invalid Argument")
                exit()
            im = reduce(im, value)        
            cv2.imshow("Result", im);
            cv2.waitKey(0);
            cv2.destroyAllWindows();