class Icinga:
    
    def __init__(self):
        
        self.service_dictionary = {
            "name":"",
            "service_description":"",
            "servicegroups":"",
            "use":"",
            "hostgroup_name":"",            
            "hostgroup":"",
            "notification_interval":"",
            "notification_options":"",
            "check_command":"",
            "display_name":"",
            "contact_groups":"",
        }

        self.start_delimiter = "define service"
        self.end_delimiter = "}"