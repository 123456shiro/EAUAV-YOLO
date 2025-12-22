import warnings, os


warnings.filterwarnings('ignore')
from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('/home/lighting/shiro_s/EAUAV-main/ultralytics/cfg/models/EAUAV.yaml')
    model.train(data='/home/lighting/shiro_s/EAUAV-main/ultralytics/cfg/datasets/VisDrone.yaml',    
                cache=False,
                imgsz=640,
                epochs=300,
                batch=32,
                close_mosaic=0, 
                workers=4, 
                device='0',
                optimizer='SGD', # using SGD
                conf = 0.02,
                # cls = 1.5,
                # patience=0, # set 0 to close earlystop.
                # resume=True, 
                amp=False, # close amp 
                # fraction=0.2,
                project='runs/train',
                name='exp',
                )
