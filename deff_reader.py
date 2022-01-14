"""

DEFF Reader for DEFF Basic Unpacker

Copyright (C) 2022 DooMMetaL

"""

deff_header = (b'DEFF') # BYTE FORM OF THE HEADER TO COMPARE WITH THE FILE INPUT HEADER

class DeffReader:
    def __init__(self, file_path , read_header):
        self.self = DeffReader
        self.read_file_path = file_path
        self.read_head = read_header
    
    def path_deff_file(self):
        global deff_file
        print("Input the full path to the DEFF file to be unpacked:")
        deff_file = input()

    def read_header(self):
        with open(deff_file, 'rb') as deff_binary_file:
            deff_header_read = deff_binary_file.read(4)
            if deff_header_read == deff_header:
                print("This is a DEFF file")
            else:
                print("This is NOT a DEFF file")
                exit()
            
            global read_file_numbers # THIS GOING TO BE USED TO CALCULATE THE LENGTH OF FILE LIST: MATH TELLS = NUMBER OF FILES * 8 [BYTE LENGTH] == LIST LENGTH; also this value will be used for the debug txt file
            global read_folders
            global read_subfolders
            deff_binary_file.seek(4)
            read_data = deff_binary_file.read(4)
            read_folders = int.from_bytes(read_data[0:1], 'little')
            read_subfolders = int.from_bytes(read_data[1:2], 'little')
            read_file_numbers = int.from_bytes(read_data[2:4], 'little')

            description_deff_file = f'This DEFF FILE CONTAINS: [{read_folders}] Folders - [{read_subfolders}] Sub-Folders - [{read_file_numbers}] Files'
            print(description_deff_file)

            deff_binary_file.seek(8)
            global read_all_deff
            read_all_deff = deff_binary_file.read()
