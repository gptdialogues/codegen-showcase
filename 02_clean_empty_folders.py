#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import argparse

def find_and_remove_empty_dirs(path, silent=False, output_file=None):
    for root, dirs, files in os.walk(path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):
                if not silent:
                    print(f"Removing empty directory: {dir_path}")
                if output_file:
                    with open(output_file, 'a') as f:
                        f.write(f"{dir_path}\n")
                subprocess.run(['rmdir', dir_path])

def main():
    parser = argparse.ArgumentParser(description="Recursively find and remove empty directories.")
    parser.add_argument("-p", "--path", default=".", help="Path to start searching for empty directories. Default is the current directory.")
    parser.add_argument("-o", "--output", help="Output file to store the paths of removed directories.")
    parser.add_argument("-s", "--silent", action="store_true", help="Run in silent mode without printing removed directories to stdout.")
    args = parser.parse_args()

    find_and_remove_empty_dirs(args.path, silent=args.silent, output_file=args.output)

if __name__ == "__main__":
    main()
