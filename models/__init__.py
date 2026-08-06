#Parent class of ticket.py
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

#parent class of agent.py
class SupportAgent():
    def __init__(self,agentId,name,specialization):
        self.agentId = agentId
        self.name = name
        self.specialization = specialization
        self.assigned_tickets=[]
    def __str__(self):
        return (f"Agent: {self.agentId}\n" f"Name: {self.name}\n" 
                f"Specialization: {self.specialization}\n" 
                f"Assigned tickets: {self.assigned_tickets}")
    def assign_ticket(self,ticket):
        self.assigned_tickets.append(ticket)