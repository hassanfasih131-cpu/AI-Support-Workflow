#Support Desk using Composition
#Description: This class can create, store, filter , and route the tickets
from services.router import supportdesk
class SupportD(supportdesk):
    def find_ticket_id(self,ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                return ticket
        return None
    def process_ticket(self,ticket):
        agent=self.routeTicket(ticket)
        if agent:
            print(f"\n{ticket.ticket_id} is assigned to {agent.name}")
            print("\nTicket Info:\n",ticket)
            print("\nAgent Info:",agent)
        else:
            print("No suitable agent for this ticket.")
    def filter_ticket(self,category=None,status=None,priority=None):
        filtered=[]
        for ticket in self.tickets:
            if category is not None and ticket.category != category:
                continue
            if status is not None and ticket._status != status:
                continue
            if priority is not None and ticket._priority != priority:
                continue
            filtered.append(ticket)
        return filtered
    def count(self):
        return len(self.tickets)
    def createTicket(self,ticket):
        self.tickets.append(ticket)
        return ticket

#TEST
#MAIN
from models.ticket import TechnicalTicket
from models.agent import  TechnicalAgent
ticket1=TechnicalTicket(7,"Ali","Null","High")
agent1=TechnicalAgent(301,"Ahmed")
support=SupportD()
t1=support.createTicket(ticket1)  #Creates a ticket
support.addAgent(agent1) #adds agent
ticket1.update_status("Resolved") #status is updated
#Routing
'''support.process_ticket(t1) #Routing Ticket to agent'''
#Finding
'''print("\n",support.find_ticket_id(7)) #finds ticket ID'''
#Filter
'''print(support.filter_ticket(category="Technical"))
print(support.filter_ticket(status="Resolved"))
print(support.filter_ticket(priority="High"))'''
#Count
'''print(support.count())'''