import os
import json



annotations = {
    "licenses": [
      {
        "name": "",
        "id": 0,
        "url": ""
      }
    ],
    "info": {
      "contributor": "",
      "date_created": "",
      "description": "",
      "url": "",
      "version": "",
      "year": ""
    },
    "categories": [
      {
        "id": 1,
        "name": "person",
        "supercategory": ""
      }
    ],
    "images": [],
    "annotations": []
}


image_id = 1
annotation_id = 1
width = 1920
height = 1080

def norm2actual(value):
    return

for root, dirs, files in os.walk("C:\\Users\\Alidar\\hte\\yolov5\\runs\\detect\\exp\\labels"):
    for file in files[::-1]:
        with open(os.path.join(root, file), 'r', encoding="utf-8") as f:
            for line in f.readlines():
                values = list(map(float, line.strip().split(' ')))
                #category_id = values[0]
                category_id, x, y, w, h = values
                x = round(width*(x-w/2))
                y = round(height*(y-h/2))
                w = round(width*w)
                h = round(height*h)
                bbox = [x, y, w, h]
                area = float(w * h)
                #print(values)
                if x + w > width:
                   print(file, image_id, x, w, x+w, width)
                if y + h > height:
                   print(file, image_id, y, h, y+h, height)
                if category_id == 0:
                    annotations["images"].append({
                        "id": image_id,
                        "width": 1920,
                        "height": 1080,
                        "file_name": file.replace(".txt", ".jpg"),
                        "license": 0,
                        "flickr_url": "",
                        "coco_url": "",
                        "date_captured": 0
                    })

                    annotations["annotations"].append({
                        "id": annotation_id,
                        "image_id": image_id,
                        "category_id": 1,
                        "segmentation": [],
                        "area": area,
                        "bbox": bbox,
                        "iscrowd": 0,
                        "attributes": {
                          "occluded": False
                        }
                    })
                    annotation_id += 1
        image_id += 1

#print(annotations)
with open("coco_test_annotations.json", "w") as outfile:
    json.dump(annotations, outfile)

