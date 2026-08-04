#Support Agent Hierarchy and Polymorphism
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
class BillingAgent(SupportAgent):
    def __init__(self,agentId,name):
        super().__init__(agentId,name,"Billing")
    def handle_ticket(self,ticket):
        ticket.addnote("Handled by Billing Agent")
        ticket.update_status("Assigned")
class TechnicalAgent(SupportAgent):
    def __init__(self,agentId,name):
        super().__init__(agentId,name,"Technical")
    def handle_ticket(self,ticket):
        ticket.addnote("Handled by Technical Agent")
        ticket.update_status("In Progress")
class AccountAgent(SupportAgent):
    def __init__(self,agentId,name):
        super().__init__(agentId,name,"Account")
    def handle_ticket(self,ticket):
        ticket.addnote("Handled by Account Agent")
        ticket.update_status("Assigned")
class GeneralAgent(SupportAgent):
    def __init__(self,agentId,name):
        super().__init__(agentId,name,"General")
    def handle_ticket(self,ticket):
        ticket.addnote("Handled by General Agent")
        ticket.update_status("Resolved")

#Testing
'''from models import agent
from models.ticket import AccountTicket, BillingTicket, TechnicalTicket, GeneralTicket
from models.agent import AccountAgent, BillingAgent, TechnicalAgent, GeneralAgent
ticket1 = AccountTicket(1,"Hassan","none","High")
agent1=AccountAgent(29,"Ali")
agent1.handle_ticket(ticket1)
print(ticket1)'''
#All of the Agent and Tickets were tested one by one to confirm if the status changes or not