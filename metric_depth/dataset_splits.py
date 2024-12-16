import argparse
import splitfolders

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_dir", type=str, default='/home/sil/data/oranges data/splits')
    parser.add_argument("-i", "--input_dir", type=str,default='/home/sil/data/oranges data/classes/')
    parser.add_argument("-r", "--ratio", type=tuple, default=(.8, 0.1, 0.1))
    parser.add_argument("-s", "--seed", type=int, default=42)
    args, unknown_args = parser.parse_known_args()
    print(f'Splitting dataset from {args.input_dir}')
    splitfolders.ratio(input=args.input_dir, output=args.output_dir, seed=args.seed, ratio=args.ratio)
    print(f'Split dataset with ratio {args.ratio} created in {args.output_dir}')

if __name__ == '__main__':
    main()