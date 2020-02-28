from __future__ import division

from absl import logging
from keras.layers import Input
from ssd import SSD
from PIL import Image
import time
import cv2
import numpy as np
ssd = SSD()


if __name__ == '__main__':  
    vid = cv2.VideoCapture('/home/yajun/mywork/ssd-keras-master/img/1.mp4')
    out = None
    fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
    out = cv2.VideoWriter('/home/yajun/mywork/ssd-keras-master/img/12.mp4', fourcc, int(vid.get(cv2.CAP_PROP_FPS)), (int(vid.get(cv2.CAP_PROP_FRAME_WIDTH)), int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    while True:
        _, img = vid.read()

        if img is None:
            logging.warning("Empty Frame")
            time.sleep(0.1)
            continue
        start = time.time()
        img = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
        image = ssd.detect_image(img)
        img = cv2.cvtColor(np.asarray(image),cv2.COLOR_RGB2BGR)
        print(time.time()-start)
        out.write(img)
        #cv2.imshow('output', img)
        #if cv2.waitKey(1) == ord('q'):
            #break
    cv2.destroyAllWindows()
    
    
