import time
import numpy as np
import cv2
import mss
from PIL import Image

with mss.mss() as sct:
    fps_list=[]
    matrix_list = []
    monitor = {'top':0, 'left':0, 'width':2560, 'height':1440}
    timer = 0
    while timer <1000:
        last_time = time.time()

        #get raw pizels from screen and save to numpy array
        img = np.array(sct.grab(monitor))
        img=cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        #Display Image
        cv2.imshow('Normal', img)

        #press q to quit
        timer += 1
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

