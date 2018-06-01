# Functions for License Plate Recognition
This repository supplies some functions for License Plate Recognition (LPR) project.

## Directory Hierarchy
```
.
├── Document
├── cctv
│   ├── 03
│   │   ├── 000011.jpg
│   │   ├── 000011.xml
│   │   ├── ...
│   │   ├── 000369.jpg
│   │   ├── 000369.xml
│   ├── 04
│   │   └── ...
│   ├── 05
│   │   └── ...
│   ├── 07
│   │   └── ...
│   ├── ...
│   ├── 19
│   │   └── ...
│   └── 21
│   │   └── ...
├── parking
│   ├── img_gt_1
│   │   ├── 000181.jpg
│   │   ├── 000181.txt
│   │   ├── ...
│   │   ├── 000190.jpg
│   │   └── 000190.txt
│   ├── img_gt_2
│   │   └──...
│   ├── img_gt_3
│   │   └──...
│   ├── img_gt_4
│   ├── img_gt_5
│   │   └──...
│   ├── img_gt_6
│   │   └──...
├── read_xml.py
├── write_csv.py  
└── eval.py

```
**Document:** documentation files  
**cctv:** cctv data file  
**parking:** parking data file  
**read_xml.py** read image and GT file  
**write_csv.py** read GT and write it on csv file  

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

# eval.py
eval function helps you evaluate the accuracy of your model by comparing GT files with predicted csv. And the function prints evaluated results on the console window and writes on the dataset_analysis.csv file.  
```
python eval.py --dataset_name=[cctv|parking] --delay=<int> --avg_pt=<float>
```
**dataset_name:** dataset name [cctv|parking], default: parking  
**delay:** waiting time between two continuous frames, default: 1 (ms)  
**avg_pt:** average processing time of your model  
