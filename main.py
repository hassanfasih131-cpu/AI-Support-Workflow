#Command line Interface
#Description: The menu is created to submit,view,search,filter Tickets, update status, add notes
#Route Tickets, View Report
from builtins import len

from models.agent import BillingAgent, TechnicalAgent, AccountAgent, GeneralAgent
from models.ticket import BillingTicket, TechnicalTicket, AccountTicket, GeneralTicket
from support_desk import SupportD
from services.storage import Storage
support=SupportD()
Store=Storage()
AGENT1=BillingAgent(1,"Ali")
AGENT2=TechnicalAgent(2,"Ahmed")
AGENT3=AccountAgent(3,"Maryum")
AGENT4=GeneralAgent(4,"Sarah")
support.addAgent(AGENT1)
support.addAgent(AGENT2)
support.addAgent(AGENT3)
support.addAgent(AGENT4)
def menu():
    while True:
        try:
            print("\n1: Submit Ticket\n"
                  "2: View Ticket\n"
                  "3: Search Ticket\n"
                  "4: Filter Ticket\n"
                  "5: Update Status\n"
                  "6: Add Notes\n"
                  "7: Route Tickets\n"
                  "8: View Reports\n"
                  "9: Exit\n")
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
            elif choice == 4:
                try:
                    Filter = int(input("What do you want to filter?:\n"
                                       "1- Category\n"
                                       "2- Status\n"
                                       "3- Priority\n"))
                    datas = Store.LoadTickets()
                    if not datas:
                        print("\nNo tickets found.\n")
                        continue
                    support.tickets = []
                    for i in datas:
                        category_str = i.get('Category', 'General').strip().title()
                        if category_str == "Billing":
                            shell = BillingTicket(i['Ticket ID'], i['Customer'], i['Message'], i['Priority'])
                        elif category_str == "Technical":
                            shell = TechnicalTicket(i['Ticket ID'], i['Customer'], i['Message'], i['Priority'])
                        elif category_str == "Account":
                            shell = AccountTicket(i['Ticket ID'], i['Customer'], i['Message'], i['Priority'])
                        else:
                            shell = GeneralTicket(i['Ticket ID'], i['Customer'], i['Message'], i['Priority'])
                        shell._status = i['Status']
                        shell.notes = i['Notes']
                        shell.ticket_id = i['Ticket ID']
                        shell.customer_name = i['Customer']
                        shell._priority = i['Priority']
                        shell.category = category_str
                        support.tickets.append(shell)
                    filtered_results = []
                    if Filter == 1:
                        Category = int(input("Enter the category:\n"
                                             "1- Billing\n"
                                             "2- Technical\n"
                                             "3- Account\n"
                                             "4- General\n"))
                        if Category == 1:
                            filtered_results = support.filter_ticket(category="Billing")
                        elif Category == 2:
                            filtered_results = support.filter_ticket(category="Technical")
                        elif Category == 3:
                            filtered_results = support.filter_ticket(category="Account")
                        elif Category == 4:
                            filtered_results = support.filter_ticket(category="General")
                    elif Filter == 2:
                        Status = int(input("Enter the status:\n"
                                           "1- Open\n"
                                           "2- Assigned\n"
                                           "3- InProgress\n"
                                           "4- Resolved\n"
                                           "5- Escalated\n"))
                        status_map = {1: "Open", 2: "Assigned", 3: "In Progress", 4: "Resolved", 5: "Escalated"}
                        target_status = status_map.get(Status)
                        if target_status:
                            filtered_results = support.filter_ticket(status=target_status)
                    elif Filter == 3:
                        Priority = int(input("Enter the priority:\n"
                                             "1- Low\n"
                                             "2- Medium\n"
                                             "3- High\n"
                                             "4- Urgent\n"))
                        priority_map = {1: "Low", 2: "Medium", 3: "High", 4: "Urgent"}
                        target_priority = priority_map.get(Priority)
                        if target_priority:
                            filtered_results = support.filter_ticket(priority=target_priority)

                    if filtered_results:
                        for ticket in filtered_results:
                            print(f"Ticket ID: {ticket.ticket_id}\n"
                                  f"Customer: {ticket.customer_name}\n"
                                  f"Category: {ticket.category}\n"
                                  f"Priority: {ticket._priority}\n"
                                  f"Status: {ticket._status}\n"
                                  f"Notes: {ticket.notes}\n")
                    else:
                        print("\nNo tickets matched your filter criteria.\n")

                except ValueError:
                    print("\nPlease enter a valid numeric selection.\n")
                except Exception as e:
                    print(f"\nAn error occurred while filtering: {e}\n")
            elif choice == 5:
                try:
                    ID = int(input("Enter the ticket ID you want to update status for:\n"))
                    datas=Store.LoadTickets()
                    support.tickets=[]
                    if not datas:
                        print("No ticket was found")
                        continue
                    else:
                        for i in datas:
                            category_str = i.get('Category','General')
                            if category_str == "Billing":
                                shell = BillingTicket(i['Ticket ID'], i['Customer'], i['Message'], i['Priority'])
                            elif category_str == "Technical":
                                shell = TechnicalTicket(i['Ticket ID'], i['Customer'], i['Message'], i['Priority'])
                            elif category_str == "Account":
                                shell = AccountTicket(i['Ticket ID'], i['Customer'], i['Message'], i['Priority'])
                            else:
                                shell = GeneralTicket(i['Ticket ID'], i['Customer'], i['Message'], i['Priority'])
                            shell._status = i['Status']
                            shell.notes = i['Notes']
                            shell.ticket_id = i['Ticket ID']
                            shell.customer_name = i['Customer']
                            shell._priority = i['Priority']
                            shell.category = category_str
                            support.tickets.append(shell)
                        found_ticket=support.find_ticket_id(ID)
                        if found_ticket._status:
                            updstatus=input("Enter a new Status:(Open, Assigned, "
                                            "In Progress, Resolved, Escalated)\n")
                            oldstatus = found_ticket._status
                            found_ticket.update_status(updstatus)
                            if found_ticket._status != oldstatus:
                                Store.SaveTicket(support.tickets)
                                print(f"\nSuccessfully updated Ticket ID to: {found_ticket._status}\n")
                        else:
                            print("\nThe ticket ID was not found.\n")
                except ValueError:
                    print("\nPlease enter a valid numeric selection.\n")
                except Exception as e:
                    print(f"\nAn error occurred while updating status: {e}\n")
            elif choice == 6:
                try:
                    ID = int(input("Enter the ticket ID you want to add note for:\n"))
                    datas=Store.LoadTickets()
                    if not datas:
                        print("No ticket was found")
                        continue
                    else:
                        support.tickets = []
                        for i in datas:
                            category_str = i.get('Category','General')
                            if category_str == "Billing":
                                shell = BillingTicket(i['Ticket ID'], i['Customer'], i['Message'], i['Priority'])
                            elif category_str == "Technical":
                                shell = TechnicalTicket(i['Ticket ID'], i['Customer'], i['Message'], i['Priority'])
                            elif category_str == "Account":
                                shell = AccountTicket(i['Ticket ID'], i['Customer'], i['Message'], i['Priority'])
                            else:
                                shell = GeneralTicket(i['Ticket ID'], i['Customer'], i['Message'], i['Priority'])
                            shell._status = i['Status']
                            shell.notes = i['Notes']
                            shell.ticket_id = i['Ticket ID']
                            shell.customer_name = i['Customer']
                            shell._priority = i['Priority']
                            shell.category = category_str
                            support.tickets.append(shell)
                        found_ticket=support.find_ticket_id(ID)
                        if found_ticket:
                            newnote=input("Enter the new note you want to add:\n")
                            if newnote:
                                found_ticket.addnote(newnote)
                                Store.SaveTicket(support.tickets)
                                print("Successfully added new note\n")
                            else:
                                print("\nThe new note cant be empty.\n")
                        else:
                            print("\nThe ticket ID was not found.\n")
                except ValueError:
                    print("\nPlease enter a valid numeric selection.\n")
                except Exception as e:
                    print(f"\nAn error occurred while adding note: {e}\n")
            elif choice == 7:
                try:
                    ID = int(input("Enter the ticket ID you want to route to an agent:\n"))
                    datas = Store.LoadTickets()
                    if not datas:
                        print("No tickets found in records.")
                        continue
                    support.tickets = []
                    for i in datas:
                        category_str = i.get('Category', 'General')
                        if category_str == "Billing":
                            shell = BillingTicket(i['Ticket ID'], i['Customer'], i['Message'], i['Priority'])
                        elif category_str == "Technical":
                            shell = TechnicalTicket(i['Ticket ID'], i['Customer'], i['Message'], i['Priority'])
                        elif category_str == "Account":
                            shell = AccountTicket(i['Ticket ID'], i['Customer'], i['Message'], i['Priority'])
                        else:
                            shell = GeneralTicket(i['Ticket ID'], i['Customer'], i['Message'], i['Priority'])
                        shell._status = i['Status']
                        shell.notes = i['Notes']
                        shell.ticket_id = i['Ticket ID']
                        shell.customer_name = i['Customer']
                        shell._priority = i['Priority']
                        shell.category = category_str
                        support.tickets.append(shell)
                    found_ticket = support.find_ticket_id(ID)
                    if found_ticket:
                        print(f"\nRouting Ticket ID {ID} ({found_ticket.category})")
                        assigned_agent = support.routeTicket(found_ticket)
                        if assigned_agent:
                            assigned_agent.handle_ticket(found_ticket)
                            assigned_agent.assign_ticket(found_ticket)
                            print(f"\n{found_ticket.ticket_id} is assigned to {assigned_agent.name}")
                            print("\nTicket Info:\n", found_ticket)
                            print("\nAgent Info:", assigned_agent)
                            Store.SaveTicket(support.tickets)
                        else:
                            print("No suitable agent for this ticket.")
                    else:
                        print("\nThe ticket ID was not found.\n")

                except ValueError:
                    print("\nPlease enter a valid numeric Ticket ID.\n")
                except Exception as e:
                    print(f"\nAn error occurred while routing: {e}\n")
            elif choice==8:
                datas=Store.LoadTickets()
                if not datas:
                    print("No tickets found in records.")
                    continue
                totaltickets=len(datas)
                print("\nTotal")
                print("The total count is: ",totaltickets)
                print("\nCategories:")
                for category in ["Billing", "Technical", "Account", "General"]:
                        count=0
                        for ticket in datas:
                            if ticket.get('Category') == category:
                                count += 1
                        print(f"{category} Count: {count} " )
                print("\nStatus:")
                for status in ["Open", "In Progress", "Resolved", "Escalated"]:
                        count=0
                        for ticket in datas:
                            if ticket.get('Status') == status:
                                count += 1
                        print(f"{status} Count: {count} " )
                print("\nPriorities:")
                for priority in ["Low", "Medium", "High", "Urgent"]:
                    count = 0
                    for ticket in datas:
                        if ticket.get('Priority') == priority:
                            count += 1
                    print(f"{priority} Count: {count}")
            elif choice==9:
                break
            else:
                print("\nPlease enter a valid choice.\n")
        except ValueError:
            print("\nPlease enter a valid choice: Value Error\n")
        except Exception as e:
            print(f"\nAn error occurred while routing: {e}\n")

menu()