
import cv2
import numpy as np
import os,sys
import math as m
import pandas as pd

def showLinkedTracks(filename, start, frames, outputfilename):
    

    linkedDF = pd.read_csv('../link/output.csv') 
    
    
    

    
    cap = cv2.VideoCapture(filename)
    cap.set(cv2.CAP_PROP_POS_FRAMES,start)
 
    
    
    for tt in range(frames):
        # Capture frame-by-frame
        _, frame = cap.read()
        
        thisFrame = linkedDF.ix[linkedDF['frame']==tt]

        
        # draw detected objects and display
        sz=6
        
        for i, row in thisFrame.iterrows():
            cv2.putText(frame ,str(int(row['particle'])) ,((int(row['x'])+12, int(row['y'])+12)), cv2.FONT_HERSHEY_SIMPLEX, 0.8,255,2)
            cv2.rectangle(frame, ((int( row['x'])-sz, int( row['y'])-sz)),((int( row['x'])+sz, int( row['y'])+sz)),(0,0,0),2)
            
        cv2.imshow('frame',frame)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    

    cv2.destroyAllWindows()
    cap.release()

if __name__ == '__main__':
    FULLNAME = sys.argv[1]
    frameStart = 0
    frameLength = int(sys.argv[3])
    path, filename = os.path.split(FULLNAME)
    noext, ext = os.path.splitext(filename)
    allTransforms=np.zeros((frameLength,3))
    outputfilename = noext + '.csv' 
    showLinkedTracks(FULLNAME, frameStart, frameLength, outputfilename)