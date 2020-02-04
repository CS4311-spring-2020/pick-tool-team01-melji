#############################################################################
##  This is a "data type" to allow the grid builder code to be more readable
##  Thanks - Micheal 2/1/20
#############################################################################

class LogInfo:
    def init(logid, logname, timestamp, discription, reporter, eventteam, iconlocation, origindocument, vectorlist):
        self.logid = logid
        self.logname = logname
        self.timestamp = timestamp
        self.discription = discription
        self.reporter = reporter
        self.eventteam = eventteam
        self.iconlocation = iconlocation
        self.origindocument = origindocument
        self.vectorlist = vectorlist
        #to use do
        #p = loginfo(logid, logname, timestamp, discription, reporter, eventteam, iconlocation, origindocument, vectorlist)
        #then do p.item to access any of the 9 items
        