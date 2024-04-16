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

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.reg_num = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner

    def display_vehicles(self):
        print(f"\nRegistration: {self.reg_num}, \nMake and Model: {self.type}, \nOwner: {self.owner}")


vehicles = {}

def register_vehicle(reg_num, type, owner):
    if reg_num in vehicles:
        print("Error: Registration number already exists")
        return
    vehicles[reg_num] = Vehicle(reg_num, type, owner)
    print(f"Vehicle with reg num {reg_num} registered")


def upadte_owner(reg_num, new_owner):
    if reg_num in vehicles:
        vehicles[reg_num].update_owner(new_owner)
        print(f"Updated owner to {new_owner} for vehicle {reg_num}")
    else:
        print("Vehicle not found.")

def display_all_vehicles():
    for vehicle in vehicles.values():
        vehicle.display_vehicles()

while True:
    selection = input("\nEnter a choice (register, update, display, exit): ")
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
            upadte_owner(reg_num, new_owner)
        elif selection == 'display':
            display_all_vehicles()
    except Exception as e:
        print(f"An error has occured: {e}")

print("Registration System Closed")