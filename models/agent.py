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
class TechnicalAgent(SupportAgent):
    def __init__(self,agentId,name):
        super().__init__(agentId,name,"Technical")
    def handle_ticket(self,ticket):
        ticket.addnote("Handled by Technical Agent")
class AccountAgent(SupportAgent):
    def __init__(self,agentId,name):
        super().__init__(agentId,name,"Account")
    def handle_ticket(self,ticket):
        ticket.addnote("Handled by Account Agent")
class GeneralAgent(SupportAgent):
    def __init__(self,agentId,name):
        super().__init__(agentId,name,"General")
    def handle_ticket(self,ticket):
        ticket.addnote("Handled by General Agent")