import os
import argparse
import csv
from xml.etree.ElementTree import parse

parser = argparse.ArgumentParser(description='')
parser.add_argument('--dataset_name', dest='dataset_name', default='parking', help='cctv or parking dataset')
args = parser.parse_args()


def main():
    # read image addresses
    filenames = []
    if args.dataset_name == 'cctv' or args.dataset_name == 'parking':
        for fold in os.listdir(args.dataset_name):
            for fname in os.listdir(os.path.join(args.dataset_name, fold)):
                if fname.endswith('.jpg'):
                    filenames.append(os.path.join(args.dataset_name, fold, fname))
        filenames = sorted(filenames)
    else:
        raise NotImplementedError

    # create csv file
    csvfile = open(args.dataset_name+'_pred.csv', 'w', newline='')
    csvwriter = csv.writer(csvfile, delimiter=',')

    for idx, filename in enumerate(filenames):
        print('Image name: {}'.format(filename))
        labels, boxes = read_data(filename, args.dataset_name)  # load GT

        # draw bounding box
        if labels is not None:
            for sub_idx, label in enumerate(labels):
                print(label, boxes[sub_idx])
                # write to csv file
                write_csv(csvwriter, args.dataset_name, filename, label, boxes[sub_idx])


def write_csv(csvwriter, dataset, filename, label, box):
    if dataset == 'cctv':
        csvwriter.writerow([filename, label[3:], box[0], box[1], box[2], box[3]])
    elif dataset == 'parking':
        csvwriter.writerow([filename, label, box[0], box[1], box[2], box[3]])
    else:
        raise NotImplementedError


def read_data(filename, dataset_name):
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
                    box.append(int(subelem.find('bndbox').find(item).text))  # x1, y1, x2, y2
                boxes.append(box)

            return labels, boxes
    elif dataset_name == 'parking':
        if not os.path.isfile(filename[:-3]+'txt'):
            return None, None
        else:
            labels, boxes = [], []
            with open(filename[:-3]+'txt', 'r', encoding='UHC') as f:
                box = [int(data) for data in f.readline().split()]  # x1, y1, w, h
                box[2], box[3] = box[0] + box[2], box[1] + box[3]   # x1, y1, x2, y2
                label = f.readline().split()

                boxes.append(box)
                labels.append(label[0])  # label is list, we wants to save string

            return labels, boxes


if __name__ == '__main__':
    main()
