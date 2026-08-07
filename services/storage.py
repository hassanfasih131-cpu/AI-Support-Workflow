#Save and Load data using .json
#Description:Data is saved in the tickets.json file, it exists even when program is closed, or file doesn't exist
#Test in support_desk.py
import json
import os
from services.__init__ import supportdesk
from models.__init__ import Ticket
class Storage(supportdesk,Ticket):
    def __init__(self):
        super().__init__()
    def SaveTicket(self,ticket):
        data=[]
        for Ticket in ticket:
            data.append({"Ticket ID":Ticket.ticket_id,"Customer":Ticket.customer_name
                         ,"Message":Ticket.message,"Category":Ticket.category
                         ,"Priority":Ticket._priority,"Status":Ticket._status,
                         "Creation Time":str(Ticket.creation_time),"Notes":Ticket.notes})

        try:
            with open("data/tickets.json","w") as f:
                json.dump(data,f,indent=4)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def LoadTickets(self):
        if not os.path.exists("data/tickets.json"):
            return []
        try:
            with open("data/tickets.json", "r") as f:
                return json.load(f)  # Returns the list of dictionaries
        except (json.JSONDecodeError, FileNotFoundError):
            return []