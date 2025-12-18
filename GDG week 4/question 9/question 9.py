import json

from abc import ABC ,abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self):
        pass


class EmailNotification(Notification):
    def send(self):
         print("Sending Email Notification")

class SMSNotification(Notification):
    def send(self):
         print("Sending SMS Notification")



json_data = '''
[
  {"type": "email"},
  {"type": "SMS"}
]
'''

data= json.loads(json_data)

notification=[]

for item in data :
    if item["type"] == "email":
        notification.append(EmailNotification())

    elif item["type"] == "SMS":
        notification.append(SMSNotification())
           

for n in notification:
    n.send()
