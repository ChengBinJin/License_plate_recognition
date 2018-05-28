import os
import sys
import cv2
import argparse
from xml.etree.ElementTree import parse

parser = argparse.ArgumentParser(description='')
parser.add_argument('--dataset_name', dest='dataset_name', default='parking', help='cctv or parking dataset')
parser.add_argument('--resize_ratio', dest='resize_ratio', type=float, default=0.5, help='resize image')
parser.add_argument('--delay', dest='delay', type=int, default=1, help='interval between two frames')
args = parser.parse_args()


def main(color=(0, 51, 255), thickness=3):
    window_name = 'Show'
    cv2.namedWindow(window_name)
    cv2.moveWindow(window_name, 0, 0)

    # read image addresses
    filenames = []
    if args.dataset_name == 'cctv':
        filenames = [os.path.join(args.dataset_name, fname) for fname in os.listdir(args.dataset_name)
                     if fname.endswith('.png')]
        filenames = sorted(filenames)
    elif args.dataset_name == 'parking':
        for fold in os.listdir(args.dataset_name):
            for fname in os.listdir(os.path.join(args.dataset_name, fold)):
                if fname.endswith('.jpg'):
                    filenames.append(os.path.join(args.dataset_name, fold, fname))
    else:
        raise NotImplementedError

    for idx, filename in enumerate(filenames):
        print('Image name: {}'.format(filename))

        img = cv2.imread(filename)  # read image
        # resize image
        img = cv2.resize(img, (int(args.resize_ratio * img.shape[1]), int(args.resize_ratio * img.shape[0])))
        labels, boxes = read_data(filename, args.dataset_name, args.resize_ratio)  # load GT

        # draw bounding box
        if labels is not None:
            for sub_idx, label in enumerate(labels):
                print(label, boxes[sub_idx])
                cv2.rectangle(img, (boxes[sub_idx][0], boxes[sub_idx][1]),
                              (boxes[sub_idx][2], boxes[sub_idx][3]), color, thickness)

        cv2.imshow(window_name, img)  # show img

        if cv2.waitKey(args.delay) & 0XFF == 27:
            sys.exit('Esc clicked!')


def read_data(filename, dataset_name, resize_ratio):
    if dataset_name == 'cctv':
        if not os.path.isfile(filename[:-3]+'xml'):
            return None, None
        else:
            labels, boxes = [], []
            node = parse(filename[:-3]+'xml').getroot()

            elems = node.findall('object')
            for subelem in elems:
                # read label
                labels.append(subelem.find('name').text)
                # read bounding boxes
                box = []
                for idx, item in enumerate(['xmin', 'ymin', 'xmax', 'ymax']):
                    box.append(int(resize_ratio * int(subelem.find('bndbox').find(item).text)))  # x1, y1, x2, y2
                boxes.append(box)

            return labels, boxes
    elif dataset_name == 'parking':
        if not os.path.isfile(filename[:-3]+'txt'):
            return None, None
        else:
            labels, boxes = [], []
            with open(filename[:-3]+'txt', 'r', encoding='UHC') as f:
                box = [int(resize_ratio * int(data)) for data in f.readline().split()]  # x1, y1, w, h
                box[2], box[3] = box[0] + box[2], box[1] + box[3]   # x1, y1, x2, y2
                label = f.readline().split()

                boxes.append(box)
                labels.append(label[0])  # label is list, we wants to save string

            return labels, boxes


if __name__ == '__main__':
    main()
