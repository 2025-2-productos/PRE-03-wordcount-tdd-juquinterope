import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Count Word in files.")
    parser.add_argument(
        "input", help="Path to the input folder containing files to process."
    )
    parser.add_argument(
        "output", help="Path to the output folder containing files to process."
    )

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output

def main():
    input_folder, output_folder = parse_args()
    print(f"input: {input_folder}")
    print(f"output: {output_folder}")