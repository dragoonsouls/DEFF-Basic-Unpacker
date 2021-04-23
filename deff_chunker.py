"""

DEFF chunker for DEFF Basic Unpacker

Copyright (C) 2021 DooMMetaL

"""

import os
import re
from global_variables import *

def list_dict(): # List to Dict
    with open(single_file, 'rb') as list_d:
        list_d.seek(8) # Reading offset to jump the first 8 bytes
        first_id = list_d.read(4)
        first_id_list = list(first_id)
        list_d.seek(8) # This reset the read offset
        file_to_list = list_d.read()
        count = file_to_list.count(first_id) # Counting the times that first FILE appears and the second one
        index_num = file_to_list.rindex(first_id) # Offset where of next ocurrence
        file_2_list = list(file_to_list)
        file_index = file_2_list[0:index_num] # The index of all files in the DEFF in list mode
    return file_index, index_num # the List and the number of index to use later
    

list_to_dict, indexnumeral = list_dict() # Multiple assign to the List and to the Int



def fileid_counter(): # This function right here calculate the number of start/end of each FILE ID index in list
    start_id =[]
    finish_id = []
    for startid in range(0, indexnumeral + 4, 8):
        start_id.append(startid)
    for finishid in range(4, indexnumeral + 8, 8):
        finish_id.append(finishid)
    return start_id, finish_id


start_file_id, finish_file_id = fileid_counter() # Multiple assign to the list of FILE ID Counter

range_fileid = zip(start_file_id, finish_file_id) # Zip the values to obtain the Tuple
range_fileid_unzipped = list(range_fileid) # Unzziping to get the List



def offset_counter(): # This function right here calculate the start/end of each offset in the index of the list
    start_offset =[]
    finish_offset = []
    for startoffset in range(4, indexnumeral + 8, 8):
        start_offset.append(startoffset)
    for finishoffset in range(8, indexnumeral + 12, 8):
        finish_offset.append(finishoffset)
    return start_offset, finish_offset


start_file_offset, finish_file_offset = offset_counter() # Multiple assign to the list of OFFSET Counter

range_file_offset = zip(start_file_offset, finish_file_offset)

range_file_offset_unzipped = list(range_file_offset)

number_of_files = indexnumeral / 2 / 4 # This is the number of files calculated through the indexnum

print("Number of files: ", number_of_files)

def file_id():
    file_id_names_rep = []   
    for start_id, end_id in range_fileid_unzipped:
        start_id, end_id
        for id_names in list_to_dict:
            file_id_names_ex = list_to_dict[start_id:end_id]
            if end_id >= indexnumeral:
                break
            file_id_names_rep.append(file_id_names_ex)
    final_id_names = []
    f_id_names = [i for n, i in enumerate(file_id_names_rep) if i not in file_id_names_rep[:n]]
    final_id_names.append(f_id_names)
    return final_id_names

final_id_names = file_id()



def offset_id():
    offset_id_rep = []   
    for start_offset_id, end_offset_id in range_file_offset_unzipped:
        start_offset_id, end_offset_id
        for id_offsets in list_to_dict:
            offset_id_ex = list_to_dict[start_offset_id:end_offset_id]
            if end_offset_id > indexnumeral: # Here the condition to reach the last offset must be greater than, because reach the end of the list
                break
            offset_id_rep.append(offset_id_ex)
    final_id_offset = []
    f_id_offset = [i for n, i in enumerate(offset_id_rep) if i not in offset_id_rep[:n]]
    final_id_offset.append(f_id_offset)
    return final_id_offset

final_id_offset = offset_id()


def deff_final_dict_name():
    listed_names = []
    for final_names in final_id_names:
        for names in final_names:
            listed_names.append(str(names)) # With this convert the list-int to a single string chain
    return listed_names

deff_listed_names = deff_final_dict_name()


def deff_final_dict_offset():
    listed_offsets = []
    for final_offsets in final_id_offset:
        for offsets in final_offsets:
            listed_offsets.append(offsets)
    return listed_offsets

deff_listed_offsets = deff_final_dict_offset()

deff_list = dict(zip(deff_listed_names, deff_listed_offsets)) # this build the dictionary in a simple way, because File ID and Offsets have the same number of objects



