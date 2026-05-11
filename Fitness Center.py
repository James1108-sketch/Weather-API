from enum import member
import sys

def read_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
                continue
            
            return value
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def read_nonempty(prompt):
    while True:
        value = input(prompt).strip()
        
        if value:
           
            return value
        print("Input cannot be empty. Please try again.")

def pause():
    input("Press Enter to continue...")
"""Being with the member class,
which represents a fitness center member. 
It includes attributes for the member's name, age, membership type, 
active status, and balance. The class also has methods to deactivate the membership, 
add charges, apply payments, and calculate discounted fees based on membership type."""
class Memeber:
    next_id = 1
    
    def __init__(self, name, age, membership_type):
        self.name = name
        self.age = age
        self.membership_type = membership_type
        self.active = True
        self.balance = 0.0

    def deactivate(self):
        self.active = False

    def add_charge(self, amount):
        self.balance += amount

    def apply_payment(self, amount):
        self.balance -= amount
    
    def get_discounted_fee(self, base_fee):
        if self.membership_type == "Student":
            return base_fee * 0.5  # 50% discount
        elif self.membership_type == "faculty":
            return base_fee * 0.25  # 75% discount
        return base_fee

    def __str__(self):
        status = "Active" if self.active else "Inactive"
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Membership: {self.membership_type}, Status: {status}, Balance: ${self.balance:.2f}"
    """Next, we define the FitnessCenterSystem class, which manages the overall system. 
It maintains lists of members, trainers, and classes, and provides methods to add members, list"""
    class FitnessCenterSystem:

        next_id = 1

        def __init__(self,name,difficutly,capacity):

            self.id = FitnessCenterSystem.next_id
            FitnessCenterSystem.next_id += 1

            self.name = name
            self.difficutly = difficutly
            self.capacity = capacity
            self.enrolled_members = []

        def enroll_member(self, member):
            
            if not member.active:
                print(f"Cannot enroll {member.name}. Membership is inactive.")
                return False
            
            if member in self.enrolled_members:
                print(f"{member.name} is already enrolled in {self.name}.")
                return False
            
            if len(self.enrolled_members) >= self.capacity:
                print(f"Cannot enroll {member.name}. {self.name} is at full capacity.")
                return False
            
            self.enrolled_members.append(member)
            
            base_fee= 10.0
            discounted_fee = member.get_discounted_fee(base_fee)
            member.add_charge(discounted_fee)

            print(f"{member.name} enrolled in {self.name}. Charged ${discounted_fee:.2f}.")
            return True
        
        def show_roster(self):
            print(f"\n{self.name} Roster:")
            if not self.enrolled_members:
                print("No members enrolled.")
                return
            for member in self.enrolled_members:
                print(f"- {member.name} (ID: {member.id})")

        def __str__(self):
            return f"ID: {self.id}, Name: {self.name}, Difficulty: {self.difficutly}, Capacity: {self.capacity}, Enrolled: {len(self.enrolled_members)}"
"""The Trainer class represents a fitness trainer, with attributes for the trainer's name, specialty, and schedule.
The class includes methods to add availability and replace the schedule, as well as a string representation method."""        
class Trainer:
    next_id = 1

    def __init__(self, name, specialty):
        self.id = Trainer.next_id
        Trainer.next_id += 1

        self.name = name
        self.specialty = specialty
        self.schedule = []

    def add_availability(self, fitness_class):
        self.schedule.append(fitness_class)

    def replace_schedule(self, new_schedule):
        self.schedule = new_schedule

    def __str__(self):

        schedule_str = (", ".join([cls.name for cls in self.schedule]) if self.schedule else "No classes scheduled")
        return f"ID: {self.id}, Name: {self.name}, Specialty: {self.specialty}, Schedule: {schedule_str}" 
"""This is the main class that ties everything together. 
It provides methods for managing members, classes, and trainers, as well as a summary report and menu systems for each category. 
The run method serves as the entry point for the application, allowing users to navigate through the different management options."""
class FitnessCenterSystem:
    def __init__(self):
        self.members = []
        self.trainers = []
        self.classes = []

    def add_member(self):
        print("\nAdd New Member")
        name = read_nonempty("Enter member name: ")
        age = read_int("Enter member age: ", min_value=0)
        membership_type = read_nonempty("Enter membership type (Student/Faculty/Community): ")
        member = Memeber(name, age, membership_type)
        
        if membership_type not in ["Student", "Faculty", "Community"]:
            print("Invalid membership type. Defaulting to Community.")
            member.membership_type = "Community"

        
        self.members.append(member)
        print(f"Member {name} added with ID {member.id}.")

    def list_members(self):
        print("\nList of Members:")
        if not self.members:
            print("No members found.")
            return
        for member in self.members:
            if member.active:
                print(member)
        
    def find_member(self, member_id):
        for member in self.members:
            if member.id == member_id:
                return member
        return None

    def deactivate_member(self):
        member_id = read_int("Enter member ID to deactivate: ")
        member = self.find_member(member_id)
        if member:
            member.deactivate()
            print(f"Member {member.name} (ID: {member.id}) has been deactivated.")
        else:
            print("Member not found.")


    def add_charge(self):

        self.list_members()
        member_id = read_int(
            "Enter member ID: "
        )

        member = self.find_member(member_id)

        if not member:
            print("Member not found.")
            return

        try:
            amount = float(
                input("Charge amount: $")
            )

            member.add_charge(amount)

            print(
                f"Added ${amount:.2f} "
                f"to {member.name}'s balance."
            )

        except ValueError:
            print("Invalid amount.")

    def apply_payment(self):

        self.list_members()

        member_id = read_int(
            "Enter member ID: "
        )

        member = self.find_member(member_id)

        if not member:
            print("Member not found.")
            return

        try:
            amount = float(
                input("Payment amount: $")
            )

            member.apply_payment(amount)
            print(
                f"Payment recorded for "
                f"{member.name}.")

        except ValueError:
            print("Invalid amount.")

def create_class(self):

        print("\n=== Create Fitness Class ===")

        name = read_nonempty("Class name: ")

        difficulty = input(
            "Difficulty: "
        ).strip().lower()

        if difficulty not in (
            "beginner",
            "intermediate",
            "advanced"
        ):
            difficulty = "beginner"

        capacity = read_int(
            "Capacity: ",
            min_value=1
        )

        fitness_class = FitnessCenterSystem(
            name,
            difficulty,
            capacity
        )

        self.classes.append(fitness_class)

        print(
            f"Class created with ID "
            f"{fitness_class.id}"
        )

def list_classes(self):

        print("\n=== Fitness Classes ===")

        if not self.classes:
            print("No classes found.")
            return

        for fitness_class in self.classes:
            print(fitness_class)

def find_class(self, class_id):

        for fitness_class in self.classes:
            if fitness_class.id == class_id:
                return fitness_class

        return None

def enroll_member(self):

        self.list_members()

        member_id = read_int(
            "Enter member ID: "
        )

        member = self.find_member(member_id)

        if not member:
            print("Member not found.")
            return

        self.list_classes()

        class_id = read_int(
            "Enter class ID: "
        )

        fitness_class = self.find_class(class_id)

        if not fitness_class:
            print("Class not found.")
            return

        fitness_class.enroll_member(member)

def show_class_roster(self):

        self.list_classes()

        class_id = read_int(
            "Enter class ID: "
        )

        fitness_class = self.find_class(class_id)

        if fitness_class:
            fitness_class.show_roster()
        else:
            print("Class not found.")

def add_trainer(self):

        print("\n=== Add Trainer ===")

        name = read_nonempty(
            "Trainer name: "
        )

        specialty = read_nonempty(
            "Specialty: "
        )

        trainer = Trainer(
            name,
            specialty
        )

        print(
            "Enter availability "
            "(blank to stop)"
        )

        while True:

            slot = input(
                "Availability: "
            ).strip()

            if not slot:
                break

            trainer.add_availability(slot)

        self.trainers.append(trainer)

        print(
            f"Trainer added with ID "
            f"{trainer.id}"
        )

def list_trainers(self):

        print("\n=== Trainers ===")

        if not self.trainers:
            print("No trainers found.")
            return

        for trainer in self.trainers:
            print(trainer)

def find_trainer(self, trainer_id):

        for trainer in self.trainers:
            if trainer.id == trainer_id:
                return trainer

        return None

def update_trainer_schedule(self):

        self.list_trainers()

        trainer_id = read_int(
            "Enter trainer ID: "
        )

        trainer = self.find_trainer(trainer_id)

        if not trainer:
            print("Trainer not found.")
            return

        print("1. Replace schedule")
        print("2. Add availability")

        choice = read_int(
            "Choice: ",
            min_value=1,
            max_value=2
        )

        if choice == 1:

            new_schedule = []

            while True:

                slot = input(
                    "Availability: "
                ).strip()

                if not slot:
                    break

                new_schedule.append(slot)

            trainer.replace_schedule(
                new_schedule
            )

        else:

            while True:

                slot = input(
                    "Availability: "
                ).strip()

                if not slot:
                    break

                trainer.add_availability(slot)

        print("Schedule updated.")

def summary_report(self):

        print("\n=== Summary Report ===")

        total_members = len(self.members)

        active_members = sum(
            1 for m in self.members if m.active
        )

        total_balance = sum(
            m.balance for m in self.members
        )

        print(f"Total members: {total_members}")
        print(f"Active members: {active_members}")

        print(
            f"Outstanding balance: "
            f"${total_balance:.2f}"
        )

        print("\nClasses:")

        for fitness_class in self.classes:
            print(f"- {fitness_class.name}")

        print("\nTrainers:")

        for trainer in self.trainers:
            print(f"- {trainer.name}")

"""The menu for the your membership 
management, class management, and trainer 
management. Each menu allows you to perform various actions related to that category."""

def member_menu(self):

        while True:

            print("\n=== Member Menu ===")
            print("1. Add member")
            print("2. List members")
            print("3. Deactivate member")
            print("4. Add charge")
            print("5. Record payment")
            print("6. Back")

            choice = read_int(
                "Choice: ",
                min_value=1,
                max_value=6
            )

            if choice == 1:
                self.add_member()

            elif choice == 2:
                self.list_members()

            elif choice == 3:
                self.deactivate_member()

            elif choice == 4:
                self.add_charge()

            elif choice == 5:
                self.apply_payment()

            elif choice == 6:
                break

            pause()

def class_menu(self):

        while True:

            print("\n=== Class Menu ===")
            print("1. Create class")
            print("2. List classes")
            print("3. Enroll member")
            print("4. Show roster")
            print("5. Back")

            choice = read_int(
                "Choice: ",
                min_value=1,
                max_value=5
            )

            if choice == 1:
                self.create_class()

            elif choice == 2:
                self.list_classes()

            elif choice == 3:
                self.enroll_member()

            elif choice == 4:
                self.show_class_roster()

            elif choice == 5:
                break

            pause()

def trainer_menu(self):

        while True:

            print("\n=== Trainer Menu ===")
            print("1. Add trainer")
            print("2. List trainers")
            print("3. Update schedule")
            print("4. Back")

            choice = read_int(
                "Choice: ",
                min_value=1,
                max_value=4
            )

            if choice == 1:
                self.add_trainer()

            elif choice == 2:
                self.list_trainers()

            elif choice == 3:
                self.update_trainer_schedule()

            elif choice == 4:
                break

            pause()

def run(self):

        while True:

            print("\n=== Campus Fitness Center ===")
            print("1. Manage members")
            print("2. Manage classes")
            print("3. Manage trainers")
            print("4. Summary report")
            print("5. Exit")

            choice = read_int(
                "Choice: ",
                min_value=1,
                max_value=5
            )

            if choice == 1:
                self.member_menu()

            elif choice == 2:
                self.class_menu()

            elif choice == 3:
                self.trainer_menu()

            elif choice == 4:
                self.summary_report()
                pause()

            elif choice == 5:
                print("Goodbye!")
                sys.exit(0)
"We now put it all together in the main block to run the fitness center system."
if __name__ == "__main__":
    system = FitnessCenterSystem()
    system.run()