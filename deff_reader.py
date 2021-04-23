"""

DEFF Reader for DEFF Basic Unpacker

Copyright (C) 2021 DooMMetaL

"""

import os
import re
from global_variables import *


deff_header = (b'DEFF')
deff_header = deff_header.decode("utf-8") # decoded DEFF header



def h_file(): # Function to read Magic Number    
    with open(single_file, 'rb') as sf:
            sf_contents = sf.read(4)
            sf_contents = sf_contents.decode("utf-8") # decoded file header
            if sf_contents == deff_header: # comparison time! yeah!
                print("This is a DEFF file")
            else:
                print("This is not a DEFF file")
                KeyboardInterrupt



def n_file(): # Function to read number of files folder/sub-folders
    with open(single_file, 'rb') as nf:
        nf_contents = nf.read(8)
        nf_each = list(nf_contents)
        nf_sub_each = nf_each[4:8] # Here the list of bytes become a redeable normal list of Int
        nff_each = nf_sub_each[0:1] # Number of folders
        nfsf_each = nf_sub_each[1:2] # Number of Sub-Folders
        nffn_each = nf_sub_each[2:3] # Number of Files          
        print("This DEFF File have: ", nff_each, "Folders", nfsf_each, "Sub-Folders", nffn_each, "Files")




