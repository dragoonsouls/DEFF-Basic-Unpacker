"""

DEFF Basic Unpacker, a simple commandline tool to unpack DEFF Files

what is a DEFF file?, The name stands from Dragoon EFFects, 
this files contains all the game effects on screen, 
such sparks, fire, brightness, darkness, explosions, vanishings, etc. 
But also contains 3D objects from each particle or character that use it. 

Copyright (C) 2022 DooMMetaL

"""
import deff_reader
import deff_chunker
import deff_writer
import deff_reader_batch
import deff_chunker_batch
import deff_writer_batch

print("DEFF Basic Unpacker, a simple commandline tool to unpack DEFF Files")
print("Choose your working method, possible options are: \nsingle mode: -s or batch mode: -b")

user_choose = input()

try:
    if user_choose == "-s":
        print("Working as Single File method...")
        try:
            deff_reader.DeffReader.path_deff_file(deff_reader.DeffReader.path_deff_file) # THIS IS USED IN GLOBAL SCOPE TO KNOW THE FILE
            deff_reader.DeffReader.read_header(deff_reader.DeffReader.read_header) # THIS READ DATA FROM THE HEADER TO KNOW IF A DEFF FILE OR NOT AND NUMBERS OF FILES
            deff_chunker.DeffSplit.list_of_files(deff_chunker.DeffSplit.list_of_files) # THIS READ THE LIST OF FILES INSIDE THE DEFF
            deff_chunker.DeffSplit.deff_split(deff_chunker.DeffSplit.deff_split) # THIS SPLIT THE DEFF FILE INTO SMALLER FILES
            deff_writer.WriteEachFile.read_path(deff_writer.WriteEachFile.read_path) # THIS READ AND GENERATES THE PROPER PATHS TO DUMP THE FILES
            deff_writer.WriteEachFile.file_unpacked(deff_writer.WriteEachFile.file_unpacked) # WRITE EACH FILE FROM THE DEFF INTO BINARY FILES
        except OSError:
            print("This is not a valid path, exiting...")
            exit()
    
    elif user_choose == "-b": # THIS FUNCTION WILL COMPILE ALL THE FILES FOUND AND LATER WILL BE PROCESSED BY THE READER
        print("Working as Batch Files method...")
        try:
            deff_reader_batch.DeffReaderBatch.path_deff_files(deff_reader_batch.DeffReaderBatch.path_deff_files)
            deff_reader_batch.DeffReaderBatch.read_headers(deff_reader_batch.DeffReaderBatch.read_headers)
            deff_chunker_batch.DeffSplitBatch.list_of_files(deff_chunker_batch.DeffSplitBatch.list_of_files)
            deff_chunker_batch.DeffSplitBatch.deffs_split(deff_chunker_batch.DeffSplitBatch.deffs_split)
            deff_writer_batch.WriteEachFileBatch.read_path(deff_writer_batch.WriteEachFileBatch.read_path)
            deff_writer_batch.WriteEachFileBatch.files_unpacked(deff_writer_batch.WriteEachFileBatch.files_unpacked)
            deff_writer_batch.WriteEachFileBatch.report_writer(deff_writer_batch.WriteEachFileBatch.report_writer)

        except OSError:
            print("This is not a valid path, exiting...")
            exit()

    else:
        print("Not a valid command")
        exit()

except KeyboardInterrupt:
    exit()
