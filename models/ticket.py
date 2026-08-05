#Build Ticket Base Class
from datetime import datetime
class Ticket: #blueprint
    def __init__(self, ticket_id,
                 customer_name, message, category,
                 priority):
        self.ticket_id = ticket_id
        self.customer_name = customer_name
        self.message=message
        self.category=category
        self.priority=priority
        self.status="Open"
        self.creation_time=datetime.now()
        self.notes=[]
    def __str__(self):
        return (f"Ticket ID: {self.ticket_id} \n" f"Customer Name: {self.customer_name}\n"
                f"Message: {self.message}\n" f"Category: {self.category}\n"
                f"Priority: {self.priority}\n" f"Status: {self.status}\n" 
                f"Creation Time: {self.creation_time}\n" f"Notes: {self.notes}")
    def addnote(self,note):
        self.notes.append(note)
    def update_status(self,status):
        allowed_status=["Open","Assigned","In Progress","Resolved"]
        if status not in allowed_status:
            print("Invalid Status")
        else:
            self.status = status
    def change_priority(self,priority):
        allowed_priority=["Urgent","High","Medium","Low"]
        if priority not in allowed_priority:
            print('Invalid Priority')
        else:
            self.priority = priority

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