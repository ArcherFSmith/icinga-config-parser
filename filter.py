import os

from time import gmtime, strftime, time

class Filter:

    def __init__(self):
        ### Used to detect & temp store data based on headers. ###
        self.name = ["name"]
        self.service_description = ["service_description"]
        self.servicegroups = ["servicegroups"]
        self.use = ["use"]
        self.hostgroup = ["hostgroup"]
        self.hostgroup_name = ["hostgroup_name"]
        self.notification_interval = ["notification_interval"]
        self.notification_options = ["notification_options"]
        self.check_command = ["check_command"]
        self.display_name = ["display_name"]
        self.contact_groups = ["contact_groups"]
        self.arrays = [self.name, self.service_description, self.servicegroups, self.use, self.hostgroup, self.hostgroup_name, self.notification_interval, self.notification_options, self.check_command, self.display_name, self.contact_groups]

        ### Stores data until output is written to the file. ###
        self.output = []
        self.string = ""
        self.string_delimiter = ";"

        ### Defines delimiters when parsing the file ###
        self.start_delimiter = "define service "
        self.end_delimiter = "}"
        self.active_segment = False

        ### Sets current path ###
        self.base_path = os.getcwd()

    def run(self):
        self.get_user_input()
        self.read_file()
        self.write_to_output()

    def get_user_input(self):
        ### User Input ###
        print("Please ensure that the config shares the directory with this program.\nEnter File Name:\n")
        self.file_name=input()

    def read_file(self):
        ### Reads file ###
        with open(self.base_path + "/" + self.file_name) as read_file:

            file = read_file.readlines()
    
            for line in file:

                line = line.strip()

                ### Determines if a new segment is found. ###
                if line.startswith(self.start_delimiter): self.active_segment = True, print("Start Segment")

                ### Generates a new line for the data and then pops it when the segment of data ends. ###
                if line.startswith(self.end_delimiter): 

                    self.active_segment = False
                    print("End Segment")

                    for element in self.arrays:

                        ### Uses the length of each element to determine if the data was picked out. ###
                        if len(element) > 1:
                            self.string = self.string + element.pop() + self.string_delimiter
                        else:
                            self.string = self.string + "No Element Found" + self.string_delimiter

            
                    ### Adds a line to the output of the file & strips the last delimiter ###
                    self.output.append(self.string.rstrip(self.string_delimiter))
                    self.string = "\n"
                    print("Wrote to Output")
                
                if self.active_segment:
                    for element in self.arrays:
                        
                        ### Detects if the header of the data matches element[0] and then appends the data to the element. ###
                        if(line.startswith(element[0])): 
                            print("Line Detected")

                            line, x, y = line.partition(";")

                            ### Removes header from data, then due to both hostgroup & hostgroup_name it may have to remove _name. ###
                            element.append(line.lstrip(element[0]).lstrip("_name").strip())

            read_file.close()

    def write_to_output(self):
        ### Writes to File ###
        output_file = self.base_path + "/" + self.file_name.rstrip(".cfg") + "_" + strftime("%d-%b-%Y-%H%M%S", gmtime(time())) + ".txt"

        with open(output_file, "w") as write_file:

            ### Each element of the output array is written to the textfile. ###
            write_file.writelines(self.output)
            print("Output written to " + output_file)
            input()
            write_file.close

if __name__ == '__main__':
    f = Filter()
    f.run()