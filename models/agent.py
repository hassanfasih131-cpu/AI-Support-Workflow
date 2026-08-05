#Support Agent Hierarchy and Polymorphism
#Description: Meaningful polymorphism was added by handle ticket() in all of the child classes
#Each agent performs different task, it updates notes and status depending on the agent and ticket used
from models.__init__ import SupportAgent
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
'''from models.ticket import AccountTicket, BillingTicket, TechnicalTicket, GeneralTicket
ticket1 = AccountTicket(1,"Hassan","none","High")
agent1=AccountAgent(29,"Ali")
agent1.handle_ticket(ticket1)
print(ticket1)'''
#All of the Agent and Tickets were tested one by one to confirm if the status changes or not