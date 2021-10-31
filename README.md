#### YoloV5 ���� ������: https://github.com/ultralytics/yolov5

#### ��: Windows 10
#### ������� ��������� � ����������� � ��������� data
```data\train```
```data\test```

#### 1) ������ ������
```python data_cornerbox_cleaner.py```

#### 2) �������� ������ � yolo-�������
```python general_json2yolo.py```

#### 3) ������ ������������� � ������������� �������
```python buil_img_pathes.py```

#### 4) ��������� ����������
```python yolo\train.py --img 640 --data configs\data.yaml --weights yolov5x.pt --freeze 10 --batch 8 --workers 4 --adam```

#### 5) ��������� ��������
```python yolo\detect.py --source data\test\images\ --weights yolo\runs\train\exp\weights\best.pt --img 640 --save-txt```

#### 6) ��������� � COCO-������
```python yolo2coco.py```
