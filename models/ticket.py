#Build Ticket Base Class and Encapsulation
#Ticket base class is created to store data
#Status and Priority are encapsulated using ._ to prevent random data
from datetime import datetime
class Ticket: #blueprint
    def __init__(self, ticket_id,
                 customer_name, message, category,
                 priority):
        self.ticket_id = ticket_id
        self.customer_name = customer_name
        self.message=message
        self.category=category
        self._priority=priority
        self._status="Open"
        self.creation_time=datetime.now()
        self.notes=[]
    def __str__(self):
        return (f"Ticket ID: {self.ticket_id} \n" f"Customer Name: {self.customer_name}\n"
                f"Message: {self.message}\n" f"Category: {self.category}\n"
                f"Priority: {self._priority}\n" f"Status: {self._status}\n" 
                f"Creation Time: {self.creation_time}\n" f"Notes: {self.notes}")
    #Adds a note in []
    def addnote(self,note):
        self.notes.append(note)
    #Updates the status of the ticket
    def update_status(self,status):
        allowed_status=["Open","Assigned","In Progress","Resolved","Escalated"]
        if status not in allowed_status:
            print("Invalid Status")
        else:
            self._status = status
    def change_priority(self,priority):
        allowed_priority=["Urgent","High","Medium","Low"]
        if priority not in allowed_priority:
            print('Invalid Priority')
        else:
            self._priority = priority

#Create Specialised ticket types
class BillingTicket(Ticket):
    def __init__(self,ticket_id,customer_name,message,priority):
        super().__init__(ticket_id,customer_name,message,"Billing",priority)

class TechnicalTicket(Ticket):
    def __init__(self,ticket_id,customer_name,message,priority):
        super().__init__(ticket_id,customer_name,message,"Technical",priority)

class AccountTicket(Ticket):
    def __init__(self,ticket_id,customer_name,message,priority):
        super().__init__(ticket_id,customer_name,message,"Account",priority)

class GeneralTicket(Ticket):
    def __init__(self,ticket_id,customer_name,message,priority):
        super().__init__(ticket_id,customer_name,message,"General",priority)

#TEST

'''from models.ticket import TechnicalTicket

ticket1=TechnicalTicket(1,"Manahil","NULL","High") #creates a ticket
ticket1.update_status("Resolved") #status is updated 
ticket1.change_priority("Urgent") #Priority is updated
print(ticket1,"\n\n")

ticket1.update_status("nusnrfuw") #attempt to update status with incorrect data
ticket1.change_priority("DVNJISNV") #attempt to update priority with incorrect data
print(ticket1)'''