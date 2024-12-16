import argparse
import os
from unittest.mock import inplace


def ret_index(path):
    return int(path.split('_')[-1].split('.')[0])

def find_group_files(path):
    files = os.listdir(path)
    depth = [file for file in files if 'depth' in file]
    depth.sort(key=ret_index)
    image = [file for file in files if 'image' in file]
    image.sort(key=ret_index)
    assert len(depth) == len(image), 'Number of images and depth do not match'
    return zip(image, depth)

def write_filenames_to_txt(output_dir, dataset_name, filenames, focal=None):
    with open(os.path.join(output_dir, dataset_name + '_train_files_with_gt.txt'), 'w') as f:
        for image, depth in filenames:
            if focal is not None:
                f.write(f'{image} {depth} {focal}\n')
            else:
                f.write(f'{image} {depth}\n')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_dir", type=str, default='/home/sil/code/Depth-Anything/metric_depth/train_test_inputs')
    parser.add_argument("-i", "--input_dir", type=str,default='/home/sil/data/oranges/splits/train')
    parser.add_argument("-d", "--dataset_name", type=str,default='oranges')
    parser.add_argument("-f", "--focal", type=float, default=527.559)
    parser.add_argument("-s", "--seed", type=int, default=42)
    args, unknown_args = parser.parse_known_args()
    print(f'Creating files list for {args.dataset_name} from {args.input_dir}')
    image_depth_files = find_group_files(args.input_dir)
    write_filenames_to_txt(args.output_dir, args.dataset_name, image_depth_files, args.focal)
    print(f'File list for {args.dataset_name} created in {args.output_dir}')

if __name__ == '__main__':
    main()