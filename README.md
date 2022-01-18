# DEFF Basic Unpacker 0.3
DEFF Basic Unpacker is a tool designed to Unpack the DEFF files from The Legend of Dragoon,
since Alpha V0.3 can handle Batch processing mode.

This tool is designed to work with files dumped by:
## LoDModS by theflyingzamboni
***https://github.com/theflyingzamboni/lodmods***

Just open with Python (v 3.8.2 recommended) in a command prompt 
write the path to the file deff_basic_unpacker.py, and execute!.

With two commands to work with files:

**-s** (single file mode)
>Path_to_DEFF_file.

example: C:\loddump\deff.bin

**-b** (batch file mode)
>Path_to_folder_with_DEFF.

example: C:\loddump\

Single file mode:
The tool will provide some useful information about DEFF files printing on your screen. Such as size in Bytes, number of folders, subfolders and number of files!.
also it will create a folder in the same DEFF file folder, where the files are unpacked!.

Batch file mode:
The tool will check over the files and show to screen whenever a DEFF is found. Additional information will be dumped in a report file created in the Unpack folder.


i want to thanks a lot to this people who came my main inspiration to learn programming!:

***TheFlyingZamboni
Monoxide
Illeprih
Zychronix***

**and all the people from the TLoD Global Discord!. Cheers!.**


CHANGELOG

Version Alpha 0.1 (first release)

Version Alpha 0.2 (14 - 01 - 2022)
      Major refactoring of the code and logics, now have to be more consistent in the unpacking and less resource eater (lol)
      thanks a lot in this case to Illeprih, because of him i found a very odd bug in the 0.1 code.

Version Alpha 0.3 (18 - 01 - 2022)
      Some refactor to the code, Batch mode implemented.
