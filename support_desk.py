#Routing Rules
#Description: Implemented Routing rules, it matches the tickets with their specific agents automatically
class supportdesk:
    def __init__(self):
        self.tickets=[]
        self.agents=[]
    def addTicket(self,tickets):
        self.tickets.append(tickets)
    def addAgent(self,agents):
        self.agents.append(agents)
    def routeTicket(self,ticket):
        for agent in self.agents:
            if ticket.category == "Billing" and agent.specialization == "Billing":
                agent.handle_ticket(ticket)
                agent.assign_ticket(ticket)
                return agent
            elif ticket.category == "Technical" and agent.specialization == "Technical":
                agent.handle_ticket(ticket)
                agent.assign_ticket(ticket)
                return agent
            elif ticket.category == "Account" and agent.specialization == "Account":
                agent.handle_ticket(ticket)
                agent.assign_ticket(ticket)
                return agent
            elif ticket.category == "General" and agent.specialization == "General":
                agent.handle_ticket(ticket)
                agent.assign_ticket(ticket)
                return agent

#Test
#Technical agent and Technical ticket is created
'''from support_desk import supportdesk
from models.ticket import TechnicalTicket
from models.agent import TechnicalAgent
support=supportdesk()
agent1=TechnicalAgent(1,"Lisa") 
ticket1=TechnicalTicket(2,"Mona",
                        "Technical Issues","High")
support.addTicket(ticket1) #placing the ticket in support desk
agent2=TechnicalAgent(2,"Billing")
support.addAgent(agent1) #placing the agent in support desk
assigned_agent=support.routeTicket(ticket1) #routing the ticket to their specific agent
print("Ticket:\n",ticket1,"\n") #Outputs Ticket
print("Assigned Agent:\n",assigned_agent) #Outputs specific agent'''
