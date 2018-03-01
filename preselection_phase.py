import numpy as np


## Global variables
fa = 'a_example.in'
fb = 'b_should_be_easy.in'
fc = 'c_no_hurry.in'
fd = 'd_metropolis.in'
fe = 'e_high_bonus.in'

files = [fa, fb, fc, fd, fe]

def import_file(filename, separator = ' '):
    try:
        file = open(filename)
        file_info = [line.strip('\n').split(separator) for line in file.readlines()]
        file.close()

        return file_info
    except:
        print('Couldnt open file %s'%(filename))

        return None

def retrieve_info(file_line_object):
    # File format (check guidelines pdf file)
    # First line: R C F N B T
    # Subsequent lines: a, b, x, y, s, f

    # Retrive info from the first line
    general_city_info = {}
    first_line_IDS = ['R', 'C', 'F', 'N', 'B', 'T']

    # Retrieve rides info from the subsequent lines
    other_lines_IDs = ['a', 'b', 'x', 's', 'f']

def main():


    # Implement the pipeline for every file
    for file in files:
        pass


if __name__=="__main__":
    main()
