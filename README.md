# Icinga Services Config Parser

A basic python program to parse Icinga Service Configuration files. Requires no external modules, it only uses Time & OS.

I tried to make the code as readable as possible. I also set it up so that I can use this to make a CLI util or something else at a later point.

In order to run the program, run 'filter.py'. It will request the name of the file that you are parsing.

Within the variables section at the top of 'filter.py', there are places to change the delimiter of the output file, the extension, and even the output file name.
The output name is currently set to append with GMT. You can also replace the extension with .txt, .cfg, .csv, etc... just make sure that if you use csv, you set the output delimiter to a comma &
uncomment '#line = line.strip().replace(",", "-")'.

Within 'dictionaries.py' you can modify the dict for icinga to look for specific headers / information. You can also change the delimiters of the parsed file.
