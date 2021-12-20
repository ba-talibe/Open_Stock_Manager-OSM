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
        if camera.isOpened():
            return_value, img = camera.read() #type bool, numpy.ndarray
            camera.release()
            img = rescaleFrame(img, 0.4)
            detectedBarcodes = decode(img)
            if not detectedBarcodes:
                print("code non dectecte")
            else:
                for barcode in detectedBarcodes:
                    (x, y, w, h) = barcode.rect 
                    cv2.rectangle(img, (x-10, y-10), 
                                (x + w+10, y + h+10),  
                                (255, 0, 0), 2)
                    if barcode.data!="": 
                        print("Codebar detecte")
                        while not fen.dispo:
                            time.sleep(1)
                        print("processing ....")
                        fen.procede((barcode.data, barcode.type))
        print("closing ..")

        
