#The parent class for the services directories
class supportdesk:
    def __init__(self):
        self.tickets=[]
        self.agents=[]
    def addTicket(self,tickets):
        self.tickets.append(tickets)
    def addAgent(self,agents):
        self.agents.append(agents)
