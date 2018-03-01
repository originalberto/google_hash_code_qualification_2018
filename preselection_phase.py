import numpy as np
import math

#### Global variables
# File names
fa = 'in_files/a_example.in'
fb = 'in_files/b_should_be_easy.in'
fc = 'in_files/c_no_hurry.in'
fd = 'in_files/d_metropolis.in'
fe = 'in_files/e_high_bonus.in'

files = [fa, fb, fc, fd, fe]

def import_file(filename, separator = ' '):
    # Imports a file
    try:
        file = open(filename)
        file_info = [line.strip('\n').split(separator) for line in file.readlines()]
        file.close()

        return file_info
    except:
        print('Couldnt open file %s'%(filename))

        return Nones

        # Retrieves information from the input file, and return dictinaries
def retrieve_info(filename):
    file_info = import_file(filename)
    # File format (check guidelines pdf file)
    # First line: R C F N B T
    # Subsequent lines: a, b, x, y, s, f

    # Retrive info from the first line
    general_city_info = {}
    first_line_IDS = ['R', 'C', 'F', 'N', 'B', 'T']
    for i in range(len(first_line_IDS)):
        general_city_info[first_line_IDS[i]] = int(file_info[0][i])

    del file_info[0]

    # Retrieve rides info from the subsequent lines
    other_lines_IDs = ['a', 'b', 'x', 's', 'f']
    # Create list for appending rides info
    rides_info = []
    for ride_number in range(len(file_info)):
        specific_ride_info = {}
        for i in range(len(other_lines_IDs)):
            specific_ride_info[other_lines_IDs[i]] = int(file_info[0][i])
        rides_info.append(specific_ride_info)

    return general_city_info, rides_info

def initialize_city_map(general_city_info):
    # Initializes a city map matrix (shape RxC)
    city_matrix = np.zeros((general_city_info['R'], general_city_info['C']))
    return city_matrix

def compute_distance_intersections(inters_a, inters_b):
    # Computes distance between inters_a and inters_b
    distance = abs(inters_a[0] - inters_b[0]) + abs(inters_a[0] - inters_b[0])
    return distance

def main():

    file = fa
    general_city_info, rides_info = retrieve_info(file)
    print(general_city_info)
    print(rides_info)

    city_matrix = initialize_city_map(general_city_info)
    print(city_matrix)


    # Implement the pipeline for every file
    for file in files:
        pass


if __name__=="__main__":
    main()
