#############################################################################
##  This is a node
##  Thanks - Micheal 2/25/20
#############################################################################

class Node:
    def __init__(self,node_id, node_name, timestamp, discription, reporter, event_team, location, icon_location, origin_document, linked_to_list):
        self.node_id = node_id
        self.node_name = node_name
        self.timestamp = timestamp
        self.discription = discription
        self.reporter = reporter
        self.event_team = event_team
        self.location = location
        self.icon_location = icon_location
        self.origin_document = origin_document
        self.linked_to_list = linked_to_list #this contains a list of the id's of the vectors the node is accociated to
        #to use do
        #p = Node(nodeid, nodename, timestamp, discription, reporter, eventteam, iconlocation, origindocument, vectorlist)
        #then do p.returnitem("itemname") to access any of the 9 items
        #elif what_to_return == "":
            #self.value = self.
    def return_item(self,what_to_return):
        self.value = ""
        if what_to_return == "node_id":
            self.value = self.node_id
        elif what_to_return == "node_name":
            self.value = self.node_name
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
            self.value = self.linked_to_list
        return self.value
    def edit_item(self,what_to_change,value):
        if what_to_change == "node_id":
            self.node_id = value 
        elif what_to_change == "node_name":
            self.node_name = value
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
            self.linked_to_list = value
        return self.value