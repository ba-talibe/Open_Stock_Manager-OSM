"""
Module permettant a l'ineterface utilisateur d'utiliser
de recupererr les donnees de codebar 
"""

from pyzbar.pyzbar import decode
import cv2
import time

def rescaleFrame(frame, scale=0.75):
    [height, width] = (frame.shape[0], frame.shape[1])
    dimension = (int(width*scale), int(height*scale))
    return cv2.resize(frame, dimension, interpolation=cv2.INTER_AREA)


def BarcodeReader(fen): 
    while True:
        camera = cv2.VideoCapture(0)
        return_value, img = camera.read() #type bool, numpy.ndarray
        if return_value:
            img = rescaleFrame(img, 2)
            detectedBarcodes = decode(img) 
            if not detectedBarcodes: 
                pass 
            else: 
        
                for barcode in detectedBarcodes:
                    (x, y, w, h) = barcode.rect 
                    cv2.rectangle(img, (x-10, y-10), 
                                (x + w+10, y + h+10),  
                                (255, 0, 0), 2)
                    if barcode.data!="": 
                        print("Codebar detecté")
                        while not fen.dispo:
                            continue
                        print("processing ....")
                        fen.procede((barcode.data, barcode.type))

        #cv2.imshow("Image", img) 
        cv2.waitKey(0)
        cv2.destroyAllWindows() 
