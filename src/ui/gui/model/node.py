class Node(object):

    def __init__(self, node_id, node_name, timestamp, description, log_entry_ref, log_creator, event_type, icon_type,
                 source, node_visibility):
        self.node_id = node_id
        self.node_name = node_name
        self.timestamp = timestamp
        self.description = description
        self.log_entry_ref = log_entry_ref
        self.log_creator = log_creator
        self.event_type = event_type
        self.icon_type = icon_type
        self.source = source
        self.node_visibility = node_visibility

    @property
    def node_id(self):
        return self.node_id

    @property
    def node_name(self):
        return self.node_name

    @node_name.setter
    def node_name(self, name):
        self.node_name = name

    @property
    def timestamp(self):
        return self.timestamp

    @property
    def description(self):
        return self.description

    @description.setter
    def description(self, description):
        self.description = description

    @property
    def log_entry_ref(self):
        return self.log_entry_ref

    @property
    def log_creator(self):
        return self.log_creator

    @property
    def event_type(self):
        return self.event_type

    @property
    def icon_type(self):
        return self.icon_type

    @icon_type.setter
    def icon_type(self, icon):
        self.icon_type = icon

    @property
    def source(self):
        return self.source

    @source.setter
    def source(self, source):
        self.source = source

    @property
    def node_name(self):
        return self.node_id

    @node_name.setter
    def node_name(self, name):
        self.node_name = name
