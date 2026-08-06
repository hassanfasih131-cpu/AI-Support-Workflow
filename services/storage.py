#Save and Load data using .json
#Description:Data is saved in the tickets.json file, it exists even when program is closed, or file doesn't exist
import json
from services.__init__ import supportdesk
from models.__init__ import Ticket
class Storage(supportdesk,Ticket):
    def __init__(self):
        super().__init__()
    def SaveTicket(self,ticket):
        data=[]
        for Ticket in self.tickets:
            data.append({"\nTicket ID":Ticket.ticket_id,"\nCustomer":Ticket.customer_name
                         ,"\nMessage":Ticket.message,"\nCategory":Ticket.category
                         ,"\nPriority":Ticket._priority,"\nStatus":Ticket._status,
                         "\nCreation Time":str(Ticket.creation_time),"\nNotes":Ticket.notes})

        try:
            with open("data/tickets.json","w") as f:
                json.dump(data,f,indent=4)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []