#############################################################################
##  This is a vector
##  Thanks - Micheal 2/25/20
#############################################################################

class Vector:
    def init(self,vector_id, vector_name, start_timestamp, end_timestamp, discription, node_list):
        self.vector_id = vector_id
        self.vector_name = vector_name
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp
        self.discription = discription
        self.node_list = node_list #this contains a list of the id's of the nodes accociated to a vector
        #do object_name.returnitem("item_name") to access any of the 9 items
    def return_item(self,what_to_return):
        self.value = ""
        if what_to_return == "vector_id":
            self.value = self.vector_id
        elif what_to_return == "vector_name":
            self.value = self.vector_name
        elif what_to_return == "start_timestamp":
            self.value = self.start_timestamp
        elif what_to_return == "end_timestamp":
            self.value = self.end_timestamp
        elif what_to_return == "discription":
            self.value = self.discription
        elif what_to_return == "node_list":
            self.value = self.node_list
        return self.value
    def edit_item(self,what_to_change,value):
        if what_to_change == "vector_id":
            self.vector_id = value 
        elif what_to_change == "vector_name":
            self.vector_name = value
        elif what_to_change == "start_timestamp":
            self.start_timestamp = value
        elif what_to_change == "end_timestamp":
            self.end_timestamp = value
        elif what_to_change == "discription":
            self.discription = value
        elif what_to_change == "node_list":
            self.node_list = value
        return self.value
    def add_node(self,node):
        self.node_list.append(node)