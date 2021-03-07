#!/usr/bin/env python
"""This program takes a filename as input and divides a portion of its contents into three separate files."""


import argparse
import random
from typing import Iterator, List


def read_tags(path: str) -> Iterator[List[List[str]]]:
    with open(path, "r") as source:
        lines = []
        for line in source:
            line = line.rstrip()
            if line:  # Line is contentful.
                lines.append(line.split())
            else:  # Line is blank.
                yield lines.copy()
                lines.clear()
    # Just in case someone forgets to put a blank line at the end...
    if lines:
        yield lines


def main(args: argparse.Namespace) -> None:
    random.seed(a=args.seed)
    sentence = read_tags(args.input)
    corpus = list(sentence)
    randomizedCorpus = random.shuffle(corpus)

    eightyPercent = int(len(corpus) * 0.8)
    tenPercent = int(len(corpus) * 0.1)

    trainFile = corpus[:eightyPercent]
    devFile = corpus[eightyPercent:eightyPercent+tenPercent]
    testFile = corpus[eightyPercent+tenPercent:]

    random.shuffle(trainFile)
    random.shuffle(devFile)
    random.shuffle(testFile)

    f = open(args.train, "w")
    for i in trainFile:
        f.write(str(i) + "\n")
        
    f = open(args.dev, "w")
    for i in devFile:
        f.write(str(i) + "\n")

    f = open(args.test, "w")
    for i in testFile:
        f.write(str(i) + "\n")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Enter file name for input.")
    parser.add_argument("--seed", type=int, required = True, help="Specify a seed.")
    parser.add_argument("train", help="Enter file name to output lines into (i.e. 'train.tag')")
    parser.add_argument("dev", help="Enter file name to output lines into (i.e. 'dev.tag')")
    parser.add_argument("test", help="Enter file name to output lines into (i.e. 'test.tag')")

    args = parser.parse_args()
    main(args)