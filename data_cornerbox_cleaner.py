import json

# Opening JSON file
with open("data\\train\\annotations\\COCO_json\\coco_annotations_train.json", 'r') as f:
    annotations = json.load(f)

bad_images = [
    "oz_frame488.jpg",
    "oz_frame426.jpg",
    "oz_frame147.jpg",
    "oz_frame146.jpg",
    "oz_frame145.jpg",
    "oz_frame131.jpg",
    "oz_frame130.jpg",
    "oz_frame121.jpg",
    "oz_frame117.jpg",
    "oz_frame098.jpg",
    "oz_frame040.jpg",
    "oz_violation_frame478.jpg",
    "oz_violation_frame105.jpg",
    "oz_violation_frame104.jpg",
]

bad_ids = list()
for image in annotations["images"]:
    if image["file_name"] in bad_images:
        bad_ids.append(image["id"])


cleaned_annotations = [a for a in annotations["annotations"] if a["bbox"][0] > 20]
for i, a in enumerate(cleaned_annotations):
    a["id"] = i+1

annotations["annotations"] = cleaned_annotations

with open("data\\train\\coco_annotations_train.json", "w") as outfile:
    json.dump(annotations, outfile)

