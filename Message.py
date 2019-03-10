'''
Message is one message someone talked.
talkday is a class having Messages in some day and datetime is just datetime.
'''
class Message:
    def __init__(self, chatroom, talkday, person, datetime, content):
        self.chatroom = chatroom
        self.talkday = talkday
        self.person = person
        self.datetime = datetime
        self.content = content

'''
A Msgs is a collection of Messages by specific chatroom and talkday.
'''
class Msgs:
    def __init__(self, chatroom, talkday):
        self.chatroom = chatroom
        self.talkday = talkday
        self._msgs = []

    def append(self, Message):
        self._msgs.append(Message)
    
    def __len__(self):
        return len(self._msgs)

    def __getitem__(self, idx):
        return self._msgs[idx]
