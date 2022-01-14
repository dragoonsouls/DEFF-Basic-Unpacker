"""

File Writer for DEFF Basic Unpacker

Copyright (C) 2022 DooMMetaL

"""
from itertools import zip_longest
import os
import deff_reader
import deff_chunker

class WriteEachFile:
    def __init__(self, read_folder, write_files):
        self.self = WriteEachFile
        self.read_f = read_folder
        self.write_f = write_files
    
    def read_path(self):
        global path_folder_complete
        global file_name
        path_folder = os.path.dirname(deff_reader.deff_file)
        path_noext = os.path.splitext(deff_reader.deff_file)[0]
        file_name = os.path.basename(path_noext)
        path_folder_complete = os.path.join(path_folder, file_name)
        try:
            os.makedirs(path_folder_complete, exist_ok=True)
        except OSError:
            print("Can't create the folder, permission denied")
    
    def file_unpacked(self):
        current_index = 0
        for file_id in deff_chunker.file_id_string:
            with open(os.path.join(path_folder_complete, file_id) + ".bin", 'wb') as write_deff_unpacked:
                data_block = deff_chunker.file_block[current_index]
                write_deff_unpacked.write(data_block)
            current_index += 1
