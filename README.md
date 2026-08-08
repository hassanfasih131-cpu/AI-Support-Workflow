# AI Support Workflow

# Description:
This is a python based ticket management system
, it is designed to help a support team, create, organize,
update, and manage customer support ticket.
This project makes use of OOP concepts while providing
a simple command line interface to manage tickets and
support agents

# Business Problem
A support team may have to deal with many different types of issues, such as 
- Technical issues 
- Billing issues 
- Account issues 
- General issues

Tickets can become difficult to manage especially with large
amounts of data, this Project makes it easier to manage tickets
# Features
This project provides a centralised support workflow where you can 
- Create different types of Tickets
- View Tickets
- Search Tickets
- Filter Tickets 
- Update Status
- Add Notes
- Route Tickets 
- View Reports

# OOP Concept Used
- Encapsulation

Ticket attributes such as status and priority are
protected from invalid direct changes. The system validates update
to ensure only only allowed values are used.
- - Allowed Statuses
- - - Open
- - - Assigned
- - - In Progress
- - - Resolved
- - - Escalated
- - Allowed Priorities
- - - Low
- - - Medium
- - - High
- - - Urgent

- Inheritence
The specialised classes inherit from base class
such as
- - Ticket
- - - TechnicalTicket
- - - Billing Ticket
- - - AccountTicket
- - - GeneralTicket

- Polymorphism
Different agent subclasses can be handled through
their common parent types. The routing system can work with 
different agent types without needing seperate
logic for every agent
- Composition
The support desk contains collection of tickets
and available support agents, it creates, route, counts
and manages the whole system
# Class Structure
- Ticket
- - Customer name
- - Message
- - Category
- - Priority
- - Status
- - Creation time
- - Notes


- SupportAgent

The base class representing a support employee.
Agents have:
- - Agent ID
- - Name
- - Specialization
- - Assigned tickets


- SupportDesk

Coordinates the overall ticket workflow.

It manages:

- - Tickets
- - Agents
- - Ticket creation
- - Searching
- - Filtering
- - Routing
- - Ticket counts
- - Workflow coordination


- Router

Contains the rules used to determine which specialized agent should receive a ticket.
- Storage

Handles saving and loading ticket data using JSON.

# Project Structure
- AI Support Workflow/
 - - main.py
 - - README.md
 - - requirements.txt

 - data/
 - - tickets.json

- models/
- - __init__.py
- - ticket.py
- - agent.py

- services/
- -  __init__.py
- - support_desk.py
- - router.py
- - storage.py

# Setup steps
- Requirements
- Python 
- Git
- PyCharm or another Python IDE

# Usage
When the program starts, the user is presented 
with a command line menu:

UNLESS SPECIFIED, USE NUMBER WHEN YOU INPUT DATA

1: Submit Ticket

2: View Ticket

3: Search Ticket

4: Filter Ticket

5: Update Status

6: Add Notes

7: Route Tickets

8: View Reports

9: Exit

Enter your choice: 

You can use this menu depending on what you want to do

# Test Cases
The following test cases were performed

| Test                      | Expected Result          | Result |
|---------------------------| ------------------------ | ------ |
| Create a technical ticket | Ticket is created        | Passed |
| Create a billing ticket   | Ticket is created        | Passed |
| Create an account ticket  | Ticket is created        | Passed |
| Create a general ticket   | Ticket is created        | Passed |
| Route technical ticket    | Technical agent assigned | Passed |
| Route billing ticket      | Billing agent assigned   | Passed |
| Find ticket by ID         | Correct ticket returned  | Passed |
| Count tickets             | Correct number returned  | Passed |
| Update ticket status      | Status changes correctly | Passed |
| Add ticket note           | Note is added            | Passed |
| Save tickets to JSON      | Data is stored           | Passed |
| Load tickets from JSON    | Saved data is restored   | Passed |
| Empty JSON file           | Program still starts     | Passed |
| Missing JSON file         | Program still starts     | Passed |
| Invalid menu choice       | Program does not crash   | Passed |
| Empty user input          | Program does not crash   | Passed |
| Invalid numeric input     | Program does not crash   | Passed |

# Sample 
- UNLESS SPECIFIED, USE NUMBER WHEN YOU INPUT DATA

- 1: Submit Ticket
- 2: View Ticket
- 3: Search Ticket
- 4: Filter Ticket
- 5: Update Status
- 6: Add Notes
- 7: Route Tickets
- 8: View Reports
- 9: Exit

- Enter your choice: 1
- Enter your ticket ID: 1
- Enter the customer name: Ali
- Enter the customer message: Payment Issue
- Enter the priority: (Low/Medium/High/Urgent) High
- What type of ticket do you want?:
- 1: Billing Ticket
- 2: Technical Ticket
- 3: Account Ticket
- 4: General Ticket
- 1

- UNLESS SPECIFIED, USE NUMBER WHEN YOU INPUT DATA

- 1: Submit Ticket
- 2: View Ticket
- 3: Search Ticket
- 4: Filter Ticket
- 5: Update Status
- 6: Add Notes
- 7: Route Tickets
- 8: View Reports
- 9: Exit

- Enter your choice: 7
- Enter the ticket ID you want to route to an agent: 1

- Routing Ticket ID 1 (Billing)
- 1 is assigned to Ali

- Ticket Info:
- Ticket ID: 1
- Customer Name: Ali
- Message: Payment Issue
- Category: Billing
- Priority: High
- Status: Assigned
- Creation Time: 2026-08-08 05:44:04
- Notes: ['Handled by Billing Agent', 'Handled by Billing Agent']

- Agent Info:
- Agent: 1
- Name: Ali
- Specialization: Billing
- Assigned tickets: [BillingTicket object]

- UNLESS SPECIFIED, USE NUMBER WHEN YOU INPUT DATA

- 1: Submit Ticket
- 2: View Ticket
- 3: Search Ticket
- 4: Filter Ticket
- 5: Update Status
- 6: Add Notes
- 7: Route Tickets
- 8: View Reports
- 9: Exit

- Enter your choice: 5
- Enter the ticket ID you want to update status for: 1
- Enter a new Status: (Open, Assigned, In Progress, Resolved, Escalated)
- In Progress

- Successfully updated Ticket ID to: In Progress

- UNLESS SPECIFIED, USE NUMBER WHEN YOU INPUT DATA

- 1: Submit Ticket
- 2: View Ticket
- 3: Search Ticket
- 4: Filter Ticket
- 5: Update Status
- 6: Add Notes
- 7: Route Tickets
- 8: View Reports
- 9: Exit

- Enter your choice: 2

- Ticket ID: 1
- Customer: Ali
- Message: Payment Issue
- Category: Billing
- Priority: High
- Status: In Progress
- Creation Time: 2026-08-08 05:53:08.102781
- Notes: []

- UNLESS SPECIFIED, USE NUMBER WHEN YOU INPUT DATA

- 1: Submit Ticket
- 2: View Ticket
- 3: Search Ticket
- 4: Filter Ticket
- 5: Update Status
- 6: Add Notes
- 7: Route Tickets
- 8: View Reports
- 9: Exit

- Enter your choice: 9

- Process finished with exit code 0

# Future Improvements

Possible future improvements include:

- Add a graphical user interface (GUI).
- Add user authentication for support agents.
- Add a database instead of JSON storage.
- Add automatic ticket priority detection.
- Add timestamps for status changes.
- Add more advanced reporting and statistics.
- Add email notifications when tickets are assigned.
- Add ticket deletion.
- Add search by customer name or keywords.
