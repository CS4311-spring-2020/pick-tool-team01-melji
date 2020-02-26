#############################################################################
##  This is a log
##  Thanks - Micheal 2/25/20
#############################################################################

class Log:
    def init(self,log_id, log_name, timestamp, discription, reporter, event_team, location, icon_location, origin_document, vector_list):
        self.log_id = log_id
        self.log_name = log_name
        self.timestamp = timestamp
        self.discription = discription
        self.reporter = reporter
        self.event_team = event_team
        self.location = location
        self.icon_location = icon_location
        self.origin_document = origin_document
        self.vector_list = vector_list #this contains a list of the id's of the vectors the log is accociated to
        #to use do
        #p = Log(logid, logname, timestamp, discription, reporter, eventteam, iconlocation, origindocument, vectorlist)
        #then do p.returnitem("itemname") to access any of the 9 items
        #elif what_to_return == "":
            #self.value = self.
    def return_item(self,what_to_return):
        self.value = ""
        if what_to_return == "log_id":
            self.value = self.log_id
        elif what_to_return == "log_name":
            self.value = self.log_name
        elif what_to_return == "timestamp":
            self.value = self.timestamp
        elif what_to_return == "discription":
            self.value = self.discription
        elif what_to_return == "reporter":
            self.value = self.reporter
        elif what_to_return == "event_team":
            self.value = self.event_team
        elif what_to_return == "icon_location":
            self.value = self.icon_location
        elif what_to_return == "origin_document":
            self.value = self.origin_document
        elif what_to_return == "vector_list":
            self.value = self.vector_list
        return self.value
    def edit_item(self,what_to_change,value):
        if what_to_change == "log_id":
            self.log_id = value 
        elif what_to_change == "log_name":
            self.log_name = value
        elif what_to_change == "timestamp":
            self.timestamp = value
        elif what_to_change == "discription":
            self.discription = value
        elif what_to_change == "reporter":
            self.reporter = value
        elif what_to_change == "event_team":
            self.event_team = value
        elif what_to_change == "icon_location":
            self.icon_location = value
        elif what_to_change == "origin_document":
            self.origin_document = value
        elif what_to_change == "vector_list":
            self.vector_list = value
        return self.value
    def add_vector(self,vector_id):
        self.vector_list.append(vector_id)