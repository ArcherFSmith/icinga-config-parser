import os
from time import gmtime, strftime, time
import dictionaries

class Filter:

    def __init__(self):
        ### Dictionary Management ###
        self.reference_dictionary = dictionaries.Icinga().service_dictionary
        self.dictionaries = []

        ### Segment Management ###
        self.start_delimiter = dictionaries.Icinga().start_delimiter
        self.end_delimiter = dictionaries.Icinga().end_delimiter
        self.active_segment = False
        self.segment_number = -1

        ### File / Output Management ###
        self.output = ""
        self.base_path = os.getcwd()
        self.file_identifier = "_" + strftime("%d-%b-%Y-%H%M%S", gmtime(time()))
        self.file_extension = ".txt"
        self.output_delimiter = ","

    def get_user_input(self):
        self._get_file_name()
        self.file_path = self.base_path + "/" + self.file_path
        self.output_path = self.file_path.rstrip(".cfg") + self.file_identifier + self.file_extension

    def _get_file_name(self):
        print("\nPlease ensure that the config shares the directory with this program.")
        while True:
            self.file_path = input("Enter File Name: ")
            if os.path.exists(self.file_path): break
            else: print("No file titled '" + self.file_path + "' found. Please Try Again...")

    def read_file(self):
        with open(self.file_path) as read_file:
            file = read_file.readlines()
            for line in file:
                #line = line.strip().replace(",", "-")
                self._manage_segments(line)
            read_file.close()

    def _manage_segments(self, line):
        if line.startswith(self.start_delimiter): 
                    self.active_segment = True
                    self.segment_number += 1
                    self.dictionaries.append(self.reference_dictionary.copy())

        if line.startswith(self.end_delimiter): self.active_segment = False

        if self.active_segment: 
            for key in self.dictionaries[self.segment_number]: 
                if line.startswith(key): 
                    line = line.lstrip(key).strip()
                    self.dictionaries[self.segment_number].update({key:line})

    def write_to_output(self):
        with open(self.output_path, "w") as write_file:
            for key in self.reference_dictionary:
                self.output = self.output + key + self.output_delimiter
            self.output = self.output.rstrip(",")
            for dictionary in self.dictionaries:
                self.output = self.output + "\n"

                for key in dictionary:
                    self.output = self.output + dictionary.get(key) + self.output_delimiter

            write_file.writelines(self.output)

            print("\nOutput saved as " + self.output_path)

            write_file.close

    def run(self):
        self.get_user_input()
        self.read_file()
        self.write_to_output()

### Run Program ###
if __name__ == '__main__':
    program = Filter()
    program.run()