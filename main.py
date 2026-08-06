#Command line Interface
#Description: The menu is created to submit,view,search,filter Tickets, update status, add notes
#Route Tickets, View Report
from models.ticket import BillingTicket, TechnicalTicket, AccountTicket, GeneralTicket
from support_desk import SupportD
from services.storage import Storage
support=SupportD()
Store=Storage()

import json

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
                support.createTicket(ticket)
                Store.addTicket(ticket)
                Store.SaveTicket(support.tickets)
            except ValueError:
                print("Please enter a valid ticket ID: Value Error")
            except Exception as e:
                print("Unable to Create Ticket: ",e)

        elif choice==2:
            loads = Store.LoadTickets()
            if not loads:
                print("\nNo Tickets Found\n")
            else:
                for ticket in loads:
                    print(f"\nTicket ID: {ticket['Ticket ID']}\n"
                          f"Customer: {ticket['Customer']}\n"
                          f"Message: {ticket['Message']}\n"
                          f"Category: {ticket['Category']}\n"
                          f"Priority: {ticket['Priority']}\n"
                          f"Status: {ticket['Status']}\n"
                          f"Creation Time: {ticket['Creation Time']}\n"
                          f"Notes: {ticket['Notes']}\n ")
        elif choice == 3:
            try:
                search_id = int(input("\nEnter the Ticket ID to search: "))
                data = Store.LoadTickets()
                support.tickets = []
                for i in data:
                    t_shell = GeneralTicket(i['Ticket ID'], i['Customer'], i['Message'],
                                            i['Priority'])
                    t_shell._status = i['Status']
                    t_shell.notes = i['Notes']
                    support.tickets.append(t_shell)
                found_ticket = support.find_ticket_id(search_id)
                if found_ticket:
                    print(f"Ticket ID: {found_ticket.ticket_id}")
                    print(f"Customer:  {found_ticket.customer_name}")
                    print(f"Message:   {found_ticket.message}")
                    print(f"Priority:  {found_ticket._priority}")
                    print(f"Status:    {found_ticket._status}")
                    print(f"Notes:     {found_ticket.notes}\n")
                else:
                    print(f"\nTicket ID {search_id} not found in records.\n")

            except ValueError:
                print("Please enter a valid numeric Ticket ID.")
menu()