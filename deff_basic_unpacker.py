"""

DEFF Basic Unpacker, a simple commandline tool to unpack DEFF Files

what is a DEFF file?, The name stands from Dragoon EFFects, 
this files contains all the game effects on screen, 
such sparks, fire, brightness, darkness, explosions, vanishings, etc. 
But also contains 3D objects from each particle or character that use it. 

Copyright (C) 2021 DooMMetaL

"""

import argparse
import os
import sys
import deff_reader
import deff_writer
import deff_chunker
from global_variables import *

print("DEFF Basic Unpacker, a simple commandline tool to unpack DEFF Files")

#single_file() # Global Variable to open the file
deff_reader.h_file() # Header Reader
deff_reader.n_file() # Number of files
deff_chunker.list_dict() # List to dict
deff_chunker.fileid_counter() # Counting the Number of Files ID slice
deff_chunker.offset_counter() # Counting the Offset Number slice
deff_chunker.file_id() # File ID names
#deff_chunker.file_id_counter_list() # Testing zip working as intended but not used
deff_chunker.offset_id() # File ID Offsets
deff_chunker.deff_final_dict_name() # Unnesting the File ID names
deff_chunker.deff_final_dict_offset() # Unnesting the File ID Offsets
deff_writer.file_writer() # writing the files using the dict
deff_writer.file_size() # a simple file size calculator in bytes
deff_writer.reverse_offset() # An offset reverser needed to work with the seek() function later
deff_writer.list_to_hex() # convert the int inside the list to hex
deff_writer.join_hex() # Joining the Hex values into a single one element
deff_writer.position_int() # Transforming the hex joined into position for seek() function later
#deff_writer.make_folder() # This is not callable from here, if not, error will happen
deff_writer.size_each_file() # Simple file size calculator for read() function
deff_writer.zip_three_values() # This simple cointainer, do the work of store FILE ID, OFFSETS and the FILE SIZE to used in the File_Writer