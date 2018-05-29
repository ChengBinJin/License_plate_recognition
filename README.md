# Functions for License Plate Recognition
This repository supplies some functions for License Plate Recognition (LPR) project.

## Directory Hierarchy
```
.
├── cctv
│   ├── 00_00030_0000030.png
│   ├── 00_00030_0000030.xml
│   ├── 00_01020_0001020.png
│   ├── 00_01020_0001020.xml
│   ├── ...
│   ├── 00_08310_0008310.png
│   └── 00_08310_0008310.xml
├── parking
│   ├── img_gt_1
│   │   ├── 000181.jpg
│   │   ├── 000181.txt
│   │   ├── ...
│   │   ├── 000190.jpg
│   │   └── 000190.txt
│   ├── img_gt_2
│   │   ├── 000021.jpg
│   │   ├── 000021.txt
│   │   ├── ...
│   │   ├── 000030.jpg
│   │   └── 000030.txt
│   ├── img_gt_3
│   │   ├── 000021.jpg
│   │   ├── 000021.txt
│   │   ├── ...
│   │   ├── 000030.jpg
│   │   └── 000030.txt
│   ├── img_gt_4
│   ├── img_gt_5
│   │   ├── 000011.jpg
│   │   ├── 000011.txt
│   │   ├── ...
│   │   ├── 000020.jpg
│   │   └── 000020.txt
│   ├── img_gt_6
│   │   ├── 000006.jpg
│   │   ├── 000006.txt
│   │   ├── ...
│   │   ├── 000010.jpg
│   │   └── 000010.txt
├── Annotation_manual_of_cctv_data.pdf
├── read_xml.py
└── write_csv.py  

```
**cctv:** cctv data file  
**parking:** parking data file  
**read_xml.py** read image and GT file  
**write_csv.py** read GT and write it on csv file  
**Annotation_manual_of_cctv_data.pdf:** Annotation Manual for CCTV data

# read_xml.py
read_xml function helps you read all of the images and the corresponding GT files in the dataset, and draws bounding box on the image and print license plate number on the console window. You can refer this function to read images and GT files to train your models.
```
python read_xml.py --dataset_name=[cctv|parking] --resize_ratio=<float> --delay=<int>
```  
**dataset_name:** dataset name [cctv|parking], default: parking    
**resize_ratio:** resize ratio of image when showing it, default: 0.5  
**delay:** waiting time between two continuous frames, default: 1 (ms)  

![test](https://user-images.githubusercontent.com/37034031/40618502-a25722d4-62cc-11e8-9688-8b487af2b4de.gif)

# write_csv.py
write_csv function reads GT files and writes them in the csv file which is considered as prediciton result. You can refer it and write your model outputs in the csv file. 
```
python write_csv.py --dataset_name=[cctv|parking]
```  
**dataset_name:** dataset name [cctv|parking], default: parking     
