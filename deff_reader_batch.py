"""

DEFF Batch Reader for DEFF Basic Unpacker

Copyright (C) 2022 DooMMetaL

"""
import pathlib

deff_header = (b'DEFF') # BYTE FORM OF THE HEADER TO COMPARE WITH THE FILE INPUT HEADER

class DeffReaderBatch:
    def __init__(self, reader_batch, batch_read_header):
        self.self = DeffReaderBatch
        self.batch_read = reader_batch
        self.read_head = batch_read_header
    
    def path_deff_files(self):
        global final_list_files
        global number_listed_files # USED FOR THE DEFF_WRITER_BATCH
        global path_user_input
        print("Input the path to search in...")
        path_user_input = input()
        path_user = pathlib.Path(path_user_input).rglob("*.bin")
        path_as_list = list(path_user)
        final_list_files = []
        for deff_files_path in path_as_list:
            with open(deff_files_path, 'rb') as one_file:
                file_head_check = one_file.read(4)
                if file_head_check == deff_header:
                    print("DEFF FILE FOUND...")
                    final_list_files.append(deff_files_path)
                else:
                    print("NOT A DEFF FILE...")
        number_listed_files = len(final_list_files) # THIS I WILL NEED FOR DOING SOME CHECKS IN ALL FILES DUMPED

    def read_headers(self):
        global read_files_numbers # THIS GOING TO BE USED TO CALCULATE THE LENGTH OF FILE LIST: MATH TELLS = NUMBER OF FILES * 8 [BYTE LENGTH] == LIST LENGTH; also this value will be used for the debug txt file
        global read_files_folders
        global read_files_subfolders
        global stored_deff

        read_files_numbers = []
        read_files_folders = []
        read_files_subfolders = []
        stored_deff = []

        for file_path in final_list_files:
            with open(file_path, 'rb') as deff_single_binary_file:
                deff_header_read = deff_single_binary_file.read(4) # I LEAVE HERE BECAUSE LATER I NEED TO RESET SEEK() PROPERLY
                                
                deff_length = len(deff_single_binary_file.read())
                deff_single_binary_file.seek(4)
                read_data = deff_single_binary_file.read(4)
                read_folders = int.from_bytes(read_data[0:1], 'little')
                read_subfolders = int.from_bytes(read_data[1:2], 'little')
                read_file_numbers = int.from_bytes(read_data[2:4], 'little')

                read_files_folders.append(read_folders)
                read_files_subfolders.append(read_subfolders)
                read_files_numbers.append(read_file_numbers)

                description_deff_file_list = []
                description_file_itself_list = []
                description_deff_file = f'This DEFF FILE CONTAINS: [{read_folders}] Folders - [{read_subfolders}] Sub-Folders - [{read_file_numbers}] Files'
                description_file_itself = f'This file is: {file_path}, have {deff_length} bytes long'
                description_deff_file_list.append(description_deff_file)
                description_file_itself_list.append(description_file_itself)

                deff_single_binary_file.seek(8)
                read_all_deff = deff_single_binary_file.read()
                stored_deff.append(read_all_deff)
        read_deff_quantity = len(stored_deff)

        if read_deff_quantity == number_listed_files:
            print("All DEFF have been read well...")
        
        else:
            print("WARNING!!: SOME FILES HAS BEEN OMITTED - Report this error as DEFF Read Jump")
