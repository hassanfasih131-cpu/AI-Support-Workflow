#Build Ticket Base Class and Encapsulation
#Ticket base class is created to store data
#Status and Priority are encapsulated using ._ to prevent random data
#Create Specialised ticket types
#Child classes
from models.__init__ import Ticket
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

#TEST


'''ticket1=TechnicalTicket(1,"Manahil","NULL","High") #creates a ticket
ticket1.update_status("Resolved") #status is updated 
ticket1.change_priority("Urgent") #Priority is updated
print(ticket1,"\n\n")

ticket1.update_status("nusnrfuw") #attempt to update status with incorrect data
ticket1.change_priority("DVNJISNV") #attempt to update priority with incorrect data
print(ticket1)'''