#Command line Interface
#Description: The menu is created to submit,view,search,filter Tickets, update status, add notes
#Route Tickets, View Report
from models.ticket import BillingTicket, TechnicalTicket, AccountTicket, GeneralTicket
from support_desk import SupportD
from services.storage import Storage
support=SupportD()
Store=Storage()

def menu():
    while True:
        print("1: Submit Ticket\n"
              "2: View Ticket\n"
              "3: Search Ticket\n"
              "4: Filter Ticket\n"
              "5: Update Status\n"
              "6: Add Notes\n"
              "7: Route Tickets\n"
              "9: View Reports\n"
              "10: Exit\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            try:
                id=int(input("Enter your ticket ID: "))
                name=input("Enter the customer name: ").strip()
                message=input("Enter the customer message: ").strip().title()
                priority=input("Enter the priority:(Low/Medium/High/Urgent) ").strip().title()
                ticket = None
                A=True
                while A:
                    Type =int(input("What type of ticket do you want?:\n"
                                       "1: Billing Ticket\n"
                                       "2: Technical Ticket\n"
                                       "3: Account Ticket\n"
                                       "4: General Ticket\n"))
                    if Type == 1:
                        ticket=BillingTicket(id,name,message,priority)
                        break
                    elif Type == 2:
                        ticket=TechnicalTicket(id,name,message,priority)
                        break
                    elif Type == 3:
                        ticket=AccountTicket(id,name,message,priority)
                        break
                    elif Type == 4:
                        ticket=GeneralTicket(id,name,message,priority)
                        break
            except ValueError:
                print("Please enter a valid ticket ID: Value Error")
        try:
            support.createTicket(ticket)
            Store.addTicket(ticket)
            Store.SaveTicket(support.tickets)
        except:
            print("Unable to create ticket")

menu()