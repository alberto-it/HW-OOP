"""
Lesson 2: Assignment | OOP Fundamentals
1. City Infrastructure Management System
Task 1: Vehicle Registration System

Problem Statement: Create a Python class Vehicle with attributes registration_number, type, 
and owner. Implement a method update_owner to change the vehicle's owner. 
Then, create a few instances of Vehicle and demonstrate changing the owner.
Code Example: Provide a basic structure for the Vehicle class without methods.
"""

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

# Expected Outcome: Completion of the Vehicle class with the update_owner method ...
        
    def update_owner(self, owner):
        self.owner = owner

# and a demonstration script showing the creation of Vehicle objects and updating their owners.

car = Vehicle("CRN1234", "Car", "John Doe")
bike = Vehicle("BRN5432", "Bicycle", "Marcia Brady")
truck = Vehicle("TRN09890", "Truck", "Jane Doe")

car.update_owner("Prince Charming")
truck.update_owner("King Harold")

print("\nCar owner:\t", car.owner)
print("Bike owner:\t", bike.owner)
print("Truck owner:\t", truck.owner, "\n")

"""
Task 2: Event Management System Enhancement

Problem Statement: Extend an existing Event class by adding a feature to keep track 
of the number of participants. Implement a method add_participant that increases the count 
and a method get_participant_count to retrieve the current count.
Code Example: Basic Event class without participant tracking.
"""
class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date

        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1

    def get_participant_count(self):
        return self.participant_count

concert = Event("Fun Concert", "April 6th, 2024")
concert.add_participant()
concert.add_participant()
concert.add_participant()

print(f"Event: {concert.name}")
print(f"Date:  {concert.date}")
print(f"Participant Count:  {concert.get_participant_count()}\n")
