import fiftyone as fo

ds = fo.Dataset.from_dir(
    dataset_type=fo.types.COCODetectionDataset,
    data_path="C:\\Users\\Alidar\\hte\\evraz\\data\\train\\images",
    labels_path="C:\\Users\\Alidar\\hte\\evraz\\data\\train\\annotations\\COCO_json\\coco_annotations_train.json",
    include_id=True,
)

print(ds.default_classes)
print(ds)

session = fo.launch_app(ds)

while True:
    pass
