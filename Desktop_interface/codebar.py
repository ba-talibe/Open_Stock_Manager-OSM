"""
Module permettant a l'ineterface utilisateur d'utiliser
de recupererr les donnees de codebar 
"""
import cv2
import os
import numpy as np
from pyzbar.pyzbar import decode


"""
redimensionne par aggrandissements ou par retrecissement
les cpatures des codebar
"""
def rescaleFrame(frame, scale=0.75):
    [height, width] = (frame.shape[0], frame.shape[1])
    dimension = (int(width*scale), int(height*scale))
    return cv2.resize(frame, dimension, interpolation=cv2.INTER_AREA)


def BarcodeReader(image): 

    img = cv2.imread(image) 
    img = rescaleFrame(img, 2)
    detectedBarcodes = decode(img) 
    if not detectedBarcodes: 
        print("Barcode Not Detected or your barcode is blank/corrupted!") 
    else: 
 
        for barcode in detectedBarcodes:   
            (x, y, w, h) = barcode.rect 
            cv2.rectangle(img, (x-10, y-10), 
                          (x + w+10, y + h+10),  
                          (255, 0, 0), 2) 
            if barcode.data!="": 
 
                print(barcode.data) 
                print(barcode.type) 
                  
    
    cv2.imshow("Image", img) 
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 


def take__capture() -> tuple:
    camera = cv2.VideoCapture(0)

    return_value, image = camera.read() #type bool, numpy.ndarray
    return (return_value, image)


#redimensionnement d'image


BarcodeReader("b.jpeg")
