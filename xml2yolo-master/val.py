# -*- coding: UTF-8 -*-
# '''=================================================
# @Project -> File :yolov8 -> val.py
# @IDE    :PyCharm
# @Version:
# @Author : Bochao Zheng
# @Time   : 2023-10-17 16:02
# @Email  : seu_zbc@hotmail.com
# @Desc   :
# '''=================================================
from ultralytics import YOLO

model=YOLO.load("/data2/zhengbochao/sunwin_project/climbing_detection/ultralytics-main/runs/detect/train9/weights/best.pt")

model =model.to(device="cuda")
model.val