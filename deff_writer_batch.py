"""

File Batch Writer for DEFF Basic Unpacker

Copyright (C) 2022 DooMMetaL

"""

import os
import deff_reader_batch
import deff_chunker_batch
import datetime

class WriteEachFileBatch:
    def __init__(self, read_folder, write_files):
        self.self = WriteEachFileBatch
        self.read_f = read_folder
        self.write_f = write_files
    
    def read_path(self):
        global path_folders_complete
        global files_names
        global additional_folder

        path_folders_complete = []
        files_names = []
        for path_to_folder in deff_reader_batch.final_list_files:
            path_folder = os.path.dirname(path_to_folder)
            path_noext = os.path.splitext(path_to_folder)[0]
            file_name = os.path.basename(path_noext)
            additional_folder = f'{path_folder}\\DEFF_Unpacked\\'
            path_folder_complete = os.path.join(additional_folder, file_name)
            path_folders_complete.append(path_folder_complete)
            files_names.append(file_name)

            try:
                os.makedirs(path_folder_complete, exist_ok=True)
            except OSError:
                print("Can't create the folder, permission denied")
    
    def files_unpacked(self):
        current_index = 0
        for folders in path_folders_complete:
            file_ids = deff_chunker_batch.files_id_strings[current_index]
            file_blocks = deff_chunker_batch.files_blocks[current_index]
            current_id = 0
            for file_block in file_blocks:
                with open(os.path.join(path_folders_complete[current_index], file_ids[current_id]), 'wb') as single_file:
                    single_file.write(file_block)

                current_id += 1
            current_index += 1
    
    def report_writer(self):
        report_file_path = os.path.join(additional_folder, 'DEFF_Batch_Report.txt')
        with open(report_file_path, 'w') as report_file:
            report_header_text = f'Files has been Unpacked using, DooMMetaL DEFF Basic Unpacker' + '\n'+ '\n'+ '\n'
            total_deff_unpacked = f'Total DEFF Unpacked: {deff_reader_batch.number_listed_files}'+ '\n'
            number_of_files_unpacked = f'Total of Files Unpacked: {sum(deff_reader_batch.read_files_numbers)}'+ '\n'+ '\n'+ '\n'
            
            report_file.write(report_header_text)
            report_file.write(total_deff_unpacked)
            report_file.write(number_of_files_unpacked)
            
            current_deff_file = 0
            for file_deff_name in deff_reader_batch.final_list_files:
                actual_deff_unpacked = f'{file_deff_name} file, have the following properties:' + '\n' + '\n'
                actual_data_folders = deff_reader_batch.read_files_folders[current_deff_file]
                actual_data_subfolders = deff_reader_batch.read_files_subfolders[current_deff_file]
                actual_data_number_files = deff_reader_batch.read_files_numbers[current_deff_file]

                data_from_deff = f'Folders: [{actual_data_folders}] - SubFolders: [{actual_data_subfolders}] - Files: [{actual_data_number_files}]' + '\n' + '\n'

                report_file.write(actual_deff_unpacked)
                report_file.write(data_from_deff)
                
                for ids_files in deff_chunker_batch.files_id_strings[current_deff_file]:
                    #for id_file in ids_files:
                    id_file_name = f'Filename dumped: {ids_files}' + '\n'
                    report_file.write(id_file_name)
                
                space_next_data = '\n' + '\n'
                report_file.write(space_next_data)

                current_deff_file += 1

            time_now = f'Work finished at: {str(datetime.datetime.now())}'
            report_file.write(time_now)
