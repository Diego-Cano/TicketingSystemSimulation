# Filename: ticketing_system.py

import time
import random
import queue
import unittest
from datetime import datetime

class Ticket:
    """
    Represents a ticket in the system with a number and timestamp.
    """
    def __init__(self, ticket_number):
        self.ticket_number = ticket_number
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"Ticket #{self.ticket_number} - Issued at {self.timestamp}"

class TicketingSystem:
    """
    A ticketing system that generates and processes tickets using a queue.
    """
    def __init__(self):
        self.ticket_queue = queue.Queue()
        self.current_ticket_number = 1

    def generate_ticket(self):
        """Generates a new ticket and adds it to the queue."""
        ticket = Ticket(self.current_ticket_number)
        self.ticket_queue.put(ticket)
        self.current_ticket_number += 1
        print(f"Generated: {ticket}")

    def process_ticket(self):
        """Processes the next ticket in the queue."""
        if not self.ticket_queue.empty():
            ticket = self.ticket_queue.get()
            print(f"Processing: {ticket}")
            time.sleep(random.uniform(1, 3))  
        else:
            print("No tickets to process.")

# Sample Usage
if __name__ == "__main__":
    system = TicketingSystem()
    

    for _ in range(5):
        system.generate_ticket()
        time.sleep(random.uniform(0.5, 2))  
    
    print("\nProcessing Tickets:\n")
    
    while not system.ticket_queue.empty():
        system.process_ticket()

# Unit Tests
class TestTicketingSystem(unittest.TestCase):
    def test_ticket_generation(self):
        system = TicketingSystem()
        system.generate_ticket()
        self.assertEqual(system.ticket_queue.qsize(), 1)
    
    def test_ticket_processing(self):
        system = TicketingSystem()
        system.generate_ticket()
        system.process_ticket()
        self.assertEqual(system.ticket_queue.qsize(), 0)
    
    def test_multiple_tickets(self):
        system = TicketingSystem()
        for _ in range(5):
            system.generate_ticket()
        self.assertEqual(system.ticket_queue.qsize(), 5)
    
    def test_process_empty_queue(self):
        system = TicketingSystem()
        system.process_ticket()
        self.assertEqual(system.ticket_queue.qsize(), 0)
    
    def test_ticket_order(self):
        system = TicketingSystem()
        system.generate_ticket()
        system.generate_ticket()
        first_ticket = system.ticket_queue.get()
        self.assertEqual(first_ticket.ticket_number, 1)
        second_ticket = system.ticket_queue.get()
        self.assertEqual(second_ticket.ticket_number, 2)

if __name__ == "__main__":
    unittest.main()
