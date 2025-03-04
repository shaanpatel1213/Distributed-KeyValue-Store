# represents a single "block" in the log, which has a log index, term, and command
# NOTE - the log index and term are enough to uniquely identify this particular entry,
# but the command still needs to be known so that other replicas know what to do
class LogEntry:
    def __init__(self, log_index, term, command, committed=False):
        # TODO - include MID from client 
        self.log_index = log_index
        self.term = term
        self.command = command
        self.committed = committed
    
    # convert log entry into dictionary (this will be sent as the "entry" in append_entries)
    def to_dict(self):
        return {"log_index": self.log_index, "term": self.term, "command": self.command, "committed": self.committed}
    
    # converts dictionary to log entry (this will be used on the follower side to convert the entry in append_entries to )
    @staticmethod
    def from_dict(data):
        return LogEntry(log_index=data["log_index"], term=data["term"], command=data["command"], committed=data["committed"])