#### YoloV5 взят отсюда: https://github.com/ultralytics/yolov5

#### ОС: Windows 10
#### Датасет поместить в дирректорию с названием data
```data\train```
```data\test```

#### 1) чистим данные
```python data_cornerbox_cleaner.py```

#### 2) приводим данные к yolo-формату
```python general_json2yolo.py```

#### 3) создаём тренировачную и валидационную выборки
```python buil_img_pathes.py```

#### 4) запускаем тренировку
```python yolo\train.py --img 640 --data configs\data.yaml --weights yolov5x.pt --freeze 10 --batch 8 --workers 4 --adam```

#### 5) запускаем инференс
```python yolo\detect.py --source data\test\images\ --weights yolo\runs\train\exp\weights\best.pt --img 640 --save-txt```

#### 6) переводим в COCO-формат
```python yolo2coco.py```
