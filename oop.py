# Question 1
'''
Objective:
 The aim of this assignment is to apply the concepts of Object Oriented Programming in Python to build a simulated City Infrastructure Management System.
 This system will incorporate classes, objects, methods, and data structures to manage didfferent aspects of a city, such as buildings, traffic, and events.

Task 1: Vehicle Registration System:
Problem Statement:
 Create a Python class Vehicle with attributes registration_number, Type, and Owner.
 Implement a method update_owner to change the vehicles owner. 
 Then, create a few instances of Vehicle and demonstrate changing the owner

Expected Outcome:
 Completion of the Vehicle class with the update_owner method and a demonstration script showing the creation of vehicle objects and updating their owners

'''
import json

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.reg_num = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

    def display_vehicles(self):
        print(f"\nRegistration: {self.reg_num}, \nMake and Model: {self.type}, \nOwner: {self.owner}")

    def to_dict(self):
        return {"reg_num": self.reg_num, "type": self.type, "owner": self.owner}



vehicles = {}


def register_vehicle(reg_num, type, owner):
    if reg_num in vehicles:
        print("Error: Registration number already exists")
        return
    vehicles[reg_num] = Vehicle(reg_num, type, owner)
    print(f"Vehicle with reg num {reg_num} registered")


def update_owner(reg_num, new_owner):
    if reg_num in vehicles:
        vehicles[reg_num].update_owner(new_owner)
        print(f"Updated owner to {new_owner} for vehicle {reg_num}")
    else:
        print("Vehicle not found.")


def display_all_vehicles():
    for vehicle in vehicles.values():
        vehicle.display_vehicles()


def load_vehicles():
    try:
        with open("vehicles.json", "r") as file:
            vehicles_dict = json.load(file)
            for reg, data in vehicles_dict.items():
                vehicles[reg] = Vehicle(data["reg_num"], data["type"], data["owner"])
    except FileNotFoundError:
        print("File Not Found")
        pass


def save_vehicles():
    with open("vehicles.json", "w") as file:
        json.dump({reg_num: vehicles[reg_num].to_dict() for reg_num in vehicles}, file, indent=4, sort_keys=True)

load_vehicles()

while True:
    selection = input("\nEnter a choice (register, update, display, save, exit): ")
    if selection == 'exit':
        break
    try:
        if selection == 'register':
            reg_num = input("Enter your registration number: ")
            type = input("Enter your vehicle make and model: ")
            owner = input("Enter your name: ")
            register_vehicle(reg_num, type, owner)
        elif selection == 'update':
            reg_num = input("Enter registration number: ")
            new_owner = input("Enter new owner's name: ")
            update_owner(reg_num, new_owner)
        elif selection == 'display':
            display_all_vehicles()
        elif selection == 'save':
            SaveState = input("Would you like to save your changes (y or n): ").lower()
            if SaveState == 'y':
                save_vehicles()
            else:
                break
    except Exception as e:
        print(f"An error has occured: {e}")

print("Registration System Closed")

'''
Task 2: Event Management System Enhancement

Problem Statement: 
 Extend an existing Event class by adding a feature to keep track of the number of participants. 
 Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.


'''
import os

class Event:
    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location
        self.participants = []

    def register_participant(self, participant_name):
        self.participants.append(participant_name)

    def add_participant(self, participant_name):
        self.register_participant(participant_name)

    def get_participant_count(self):
        return len(self.participants)

    def display_event(self):
        participant_count = self.get_participant_count()
        print(f"\nEvent: {self.name}, Date: {self.date}, Location: {self.location}")
        print(f"Participants ({participant_count}): {', '.join(self.participants) if self.participants else 'None'}")

def save_events_to_file():
    with open('events.txt', 'w') as file:
        file.write("Event,Date,Location,Participants Count,Participants\n")
        for event in events.values():
            participants_str = ','.join(event.participants)
            participant_count = event.get_participant_count()
            file.write(f"{event.name},{event.date},{event.location},{participant_count},{participants_str}\n")

def load_events_from_file():
    if os.path.exists('events.txt'):
        with open('events.txt', 'r') as file:
            next(file)  # Skip the header line
            for line in file:
                parts = line.strip().split(',')
                name, date, location, participant_count, *participants = parts
                event = Event(name, date, location)
                event.participants.extend(participants)
                events[name] = event

events = {}
load_events_from_file()

while True:
    action = input("\nEnter action (add, register, display, save, exit): ").lower()
    if action == "exit":
        break

    try:
        if action == "add":
            name = input("Enter event name: ")
            date = input("Enter event date: ")
            location = input("Enter event location: ")
            events[name] = Event(name, date, location)
        elif action == "register":
            event_name = input("Enter Event Name: ")
            participant = input("Enter participant name: ")
            if event_name in events:
                events[event_name].add_participant(participant)
                print(f"Participant {participant} added to {event_name}. Current count: {events[event_name].get_participant_count()}")
            else:
                print("Event not found.")
        elif action == "display":
            for event in events.values():
                event.display_event()
        elif action == "save":
            save_events_to_file()
            print("Events saved to file")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Event Planner System Closed.")




'''  2. Python City Planning Simulator
Objective:
 The aim of this assignment is to solidify understanding of Python's Object-Oriented Programming concepts through the development of a simulated city planning system. 
 This system will integrate the use of classes, objects, inheritance, and file handling to manage various city elements like buildings, traffic systems, and public events.

Task 1: File Handling for Building Records

Problem Statement: 
 Implement a system to handle building records using file operations. 
 Create a Building class and write a script to save and load building details to and from a file.

'''