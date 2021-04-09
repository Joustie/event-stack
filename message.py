import json

class Message:

    def __init__(self, username, email):
        self.userName = username
        self.email = email
        #self.uuid": "",


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
