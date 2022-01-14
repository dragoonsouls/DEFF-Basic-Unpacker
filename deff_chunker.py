"""

DEFF chunker for DEFF Basic Unpacker

Copyright (C) 2022 DooMMetaL

"""

from itertools import zip_longest
import deff_reader

class DeffSplit:
    def __init__(self, list_files, split_file):
        self.self = DeffSplit
        self.list_of_files = list_files
        self.split_the_file = split_file
    
    def list_of_files(self): # CONVERSION FROM THE LIST READEABLE DATA
        global file_complete
        file_complete = deff_reader.read_all_deff
        list_in_file = deff_reader.read_file_numbers * 8
        file_list = file_complete[:list_in_file]

        counter_files = deff_reader.read_file_numbers
        file_id_count = 0
        file_address_count = 4
        files_id = []
        files_address = []
        while counter_files > 0:
            id_file = file_list[file_id_count:file_address_count]
            address_file = file_list[file_address_count:(file_address_count + 4)]
            files_id.append(id_file)
            files_address.append(address_file)
            counter_files -= 1
            file_id_count += 8
            file_address_count += 8
        
        # FILE ID CONVERSION TO STRING
        global file_id_string
        file_id_string = []
        for id in files_id:
            id_1_value = int.from_bytes(id[0:1], 'little')
            id_2_value = int.from_bytes(id[1:2], 'little')
            id_3_value = int.from_bytes(id[2:3], 'little')
            id_4_value = int.from_bytes(id[3:4], 'little')
            id_string = f'[{id_1_value}_{id_2_value}_{id_3_value}_{id_4_value}]'
            file_id_string.append(id_string)
        
        # FILE ADDRESS CONVERSION TO INTEGER
        file_address_int = []
        for address in files_address:
            address_to_int = (int.from_bytes(address, 'little') - 8)
            file_address_int.append(address_to_int)
        
        # TOTAL LENGTH TO READ FOR EACH FILE

        length_list_address = len(file_address_int)
        count_address_start = 1
        next_address = []
        while length_list_address > 1 :
            next_file_address_int = file_address_int[count_address_start]
            length_list_address -= 1
            count_address_start += 1
            next_address.append(next_file_address_int)
        last_length = len(file_complete)
        next_address.append(last_length)
        
        # ZIP THE ADDRESS START AND TOTAL LENGTH OF DATA PER FILE
        global add_endadd_zip
        add_endadd_zip = zip(file_address_int, next_address)
    
    def deff_split(self):
        # SPLIT THE FILE BLOCKS, FOR PROCESSING
        global file_block
        file_block = []
        for address, end_add in add_endadd_zip:
            file_read_each = file_complete[address:end_add]
            file_block.append(file_read_each)
        if len(file_block) == deff_reader.read_file_numbers:
            print("DEFF File processing in progress")
        else:
            print("DEFF File processing interrupted, number of files do not match with number of file blocks... closing program.[REPORT THIS ERROR AS: DEFF_SPLIT DISAGREE]")
            exit()
