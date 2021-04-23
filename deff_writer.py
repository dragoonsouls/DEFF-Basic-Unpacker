"""

File Writer for DEFF Basic Unpacker

Copyright (C) 2021 DooMMetaL

"""

import argparse
import os
import sys
from global_variables import *
from deff_chunker import *

def file_size(): # I need the total file size to compare
    file_length = os.path.getsize(single_file)
    return file_length

file_size_int = file_size()

print("File Size is: ", file_size_int, " Bytes")

def reverse_offset():
    offset_from_dict = []  # This is working just fine
    offsets_dict = deff_list.values()
    for element in offsets_dict:        
        rev_element = list(reversed(element)) # This reverse the values in the nested list
        offset_from_dict.append(rev_element) # This append the elements to the final list to work
    return offset_from_dict

reversed_offsets = reverse_offset()

reversed_offsets_f = list(reversed_offsets)


def list_to_hex():
    hex_list = []
    for elements in reversed_offsets_f: # This is working fine
        h_list = []
        for e in elements:
            result = hex(e)
            result_f = result[2:4].zfill(2) # Telling to displace the string two positions to avoid the 0x stuff and also filling with 0 as two bytes
            h_list.append(result_f)
        hex_list.append(h_list) # With this i can maintain the values in separated indexes
    return hex_list

hexadecimal_list_r = list_to_hex()

hexadecimal_list = list(hexadecimal_list_r)

        
def join_hex():
    merged_hex = []
    for elements in hexadecimal_list:
        merged_hex.append(''.join(elements[0:4]))
    return merged_hex

merged_hex_f = join_hex()

merged_hex = list(merged_hex_f)

def position_int():
    position = []
    for integers in merged_hex:
        str_to_int = int(integers,16) # This convert a string to a integer for later use in seek() function
        position.append(str_to_int)
    return position

for_seek_pos = position_int()

position_of_files = list(for_seek_pos)

dict_updated = dict(zip(deff_listed_names, position_of_files)) #I need this to work with a little flow in the file_writer()


def make_folder():
    folder = 'Unpacked_files'
    parent_dir = single_file[:-4]
    path_to_folder = os.path.join(parent_dir, folder)
    os.makedirs(path_to_folder)
    print('Folder made at: ', path_to_folder)
    return path_to_folder

path_folder = make_folder()




def size_each_file():
    start_positions = list(dict_updated.values())
    next_positions = list(dict_updated.values())[1::1] # This could count the next position in the previous values
    last_position = list(dict_updated.values())[-1:]
    file_size_each = [next_positions - start_positions for start_positions, next_positions in zip(start_positions, next_positions)]
    last_position_integer = last_position[0]
    last_file_size = file_size_int - last_position_integer
    file_size_each.append(last_file_size) # Here's the solution to adding the last position lenght previously not calculated

    return file_size_each, last_position, next_positions

file_size_each, last_position, next_positions = size_each_file()

file_size_each_l = file_size_each

last_position_int = last_position[0]

seek_read_list = zip(position_of_files, file_size_each)


def zip_three_values():
    container = zip(deff_listed_names, position_of_files, file_size_each_l)
    container_final = list(container)
    return container_final

container = zip_three_values()


def file_writer():                                              # Finally the writer working correctly!
    with open(single_file, 'rb') as read_only:
        for file_id_names_dict, pos_of_file, f_size in container:   
            with open(os.path.join(path_folder, "{}.bin".format(file_id_names_dict)), 'wb') as write_name:
                read_only.seek(pos_of_file)
                a = read_only.read(f_size)
                write_name.write(a)