import argparse
import sys

from homework.src._internals.preprocess_lines import preprocess_lines
from homework.src._internals.read_all_lines import read_all_lines
from homework.src._internals.write_word_counts import write_word_counts


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


def split_into_words(line):
    return line.split()


def clean_word(word):
    return word.strip(".,!?;:()[]{}\"'-")


def count_words(words):
    counter = {}
    for word in words:
        cleaned = clean_word(word)
        if cleaned:  # Solo contar si queda algo después de limpiar
            counter[cleaned] = counter.get(cleaned, 0) + 1
    return counter


def main():
    input_folder, output_folder = parse_args()
    print(f"input: {input_folder}")
    print(f"output: {output_folder}")
    lines = read_all_lines(input_folder)
    preprocessed_lines = preprocess_lines(lines)
    all_words = []
    for line in preprocessed_lines:
        all_words.extend(split_into_words(line))
    word_counts = count_words(all_words)
    write_word_counts(output_folder, word_counts)
    