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

print("DEFF Basic Unpacker, a simple commandline tool to unpack DEFF Files")

deff_reader.DeffReader.path_deff_file(deff_reader.DeffReader.path_deff_file) # THIS IS USED IN GLOBAL SCOPE TO KNOW THE FILE
deff_reader.DeffReader.read_header(deff_reader.DeffReader.read_header) # THIS READ DATA FROM THE HEADER TO KNOW IF A DEFF FILE OR NOT AND NUMBERS OF FILES
deff_chunker.DeffSplit.list_of_files(deff_chunker.DeffSplit.list_of_files) # THIS READ THE LIST OF FILES INSIDE THE DEFF
deff_chunker.DeffSplit.deff_split(deff_chunker.DeffSplit.deff_split) # THIS SPLIT THE DEFF FILE INTO SMALLER FILES
deff_writer.WriteEachFile.read_path(deff_writer.WriteEachFile.read_path) # THIS READ AND GENERATES THE PROPER PATHS TO DUMP THE FILES
deff_writer.WriteEachFile.file_unpacked(deff_writer.WriteEachFile.file_unpacked) # WRITE EACH FILE FROM THE DEFF INTO BINARY FILES
