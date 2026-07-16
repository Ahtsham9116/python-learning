#================================

# Project: Zoo Management System
# Author: M Ahtsham Javed
# Language: python
# Version: 01

#================================

separator = "=" * 44


class Animal:
    def __init__(self, name, age, specie, health):
        self.name = name
        self.age = age
        self.specie = specie
        self.health = health

    def display_info(self):
        print(separator)
        print(f"\tName: {self.name}")
        print(f"\tAge: {self.age} years")
        print(f"\tSpecies: {self.specie}")
        print(f"\tHealth: {self.health}")

    def eat(self):
        print(f"\t{self.name} is eating.")

    def sleep(self):
        print(f"\t{self.name} is sleeping")

    def make_sound(self):
        print(f"\t{self.name} is making sound")


class Mammal(Animal):
    def __init__(self, name, age, specie, health, fur_color):
        self.fur_color = fur_color
        super().__init__(name, age, specie, health)

    def display_info(self):
        super().display_info()
        print(f"\tFur Color: {self.fur_color}")

    def give_birth(self):
        print(f"\t{self.name} gives birth to live young.")

    def walk(self):
        print(f"\t{self.name} walks around.")


class Lion(Mammal):
    def __init__(self, name, age, specie, health, fur_color):
        super().__init__(name, age, specie, health, fur_color)

    def hunt(self):
        print(f"\t{self.name} is hunting.")

    def make_sound(self):
        print(f"\t{self.name} is Roaring.")


class Elephant(Mammal):
    def __init__(self, name, age, specie, health, fur_color):
        super().__init__(name, age, specie, health, fur_color)

    def spray_water(self):
        print(f"\t{self.name} sprays water with its trunk.")

    def make_sound(self):
        print("\tTrumpet!")


class Bird(Animal):
    def __init__(self, name, age, specie, health, wing_span):
        self.wing_span = wing_span
        super().__init__(name, age, specie, health)

    def display_info(self):
        super().display_info()
        print(f"\tWing Span: {self.wing_span}")

    def fly(self):
        print(f"\t{self.name} is flying.")

    def lay_eggs(self):
        print(f"\t{self.name} laid eggs")


class Parrot(Bird):
    def __init__(self, name, age, specie, health, wing_span):
        super().__init__(name, age, specie, health, wing_span)

    def repeat_words(self):
        print(f"\t{self.name} repeats as we speak")

    def make_sound(self):
        print("\tSquaw!")


class Chicken(Bird):
    def __init__(self, name, age, specie, health, wing_span):
        super().__init__(name, age, specie, health, wing_span)

    def fly(self):
        print(f"\t{self.name} can not fly")

    def make_sound(self):
        print("\tCluck")


class Reptile(Animal):
    def __init__(self, name, age, specie, health, is_venomous: bool):
        self.is_venomous = is_venomous
        super().__init__(name, age, specie, health)

    def display_info(self):
        super().display_info()
        venomous_text = "Yes" if self.is_venomous else "No"
        print(f"\tVenomous: {venomous_text}")

    def crawl(self):
        print(f"\t{self.name} is crawling.")

    def shed_skin(self):
        print(f"\t{self.name} sheds their skin.")


class Snake(Reptile):
    def __init__(self, name, age, specie, health, is_venomous: bool):
        super().__init__(name, age, specie, health, is_venomous)

    def dangerous(self):
        if self.is_venomous:
            print("\tWarning! This snake is venomous.")
        else:
            print("\tWarning! This snake is not venomous.")

    def make_sound(self):
        print("\tHiss!")


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print("Animal added successfully.")

    def remove_animal(self):
        name = input("Enter animal name to remove: ").strip()
        animal = self.find_animal(name)
        if animal is None:
            print("Animal not found.")
            return

        self.animals.remove(animal)
        print("Removed successfully.")

    def search_animal(self):
        name = input("Enter animal name to search: ").strip()
        animal = self.find_animal(name)
        if animal is None:
            print("Animal not found.")
            return

        animal.display_info()

    def display_all_animals(self):
        if not self.animals:
            print("No animals in zoo.")
            return

        for animal in self.animals:
            animal.display_info()
            print("-" * 44)

    def feed_animal(self):
        name = input("Enter animal name to feed: ").strip()
        animal = self.find_animal(name)
        if animal is None:
            print("Animal not found.")
            return

        animal.eat()

    def make_animal_sound(self):
        name = input("Enter animal name to make sound: ").strip()
        animal = self.find_animal(name)
        if animal is None:
            print("Animal not found.")
            return

        animal.make_sound()

    def animal_activity(self):
        name = input("Enter animal name for activity: ").strip()
        animal = self.find_animal(name)
        if animal is None:
            print("Animal not found.")
            return

        if isinstance(animal, Lion):
            animal.hunt()
        elif isinstance(animal, Elephant):
            animal.spray_water()
        elif isinstance(animal, Parrot):
            animal.repeat_words()
        elif isinstance(animal, Snake):
            animal.dangerous()
        else:
            print("No special activity available for this animal.")

    def find_animal(self, name):
        for animal in self.animals:
            if animal.name.lower() == name.lower():
                return animal
        return None


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
        except ValueError:
            print("Please enter a valid number.")
            continue

        if value > 0:
            return value
        print("Value must be positive.")


def get_valid_health(prompt):
    valid_health = ["Healthy", "Good", "Fair", "Bad"]
    normalized_health = [item.lower() for item in valid_health]

    while True:
        value = input(prompt).strip()
        if value.lower() in normalized_health:
            return next(item for item in valid_health if item.lower() == value.lower())
        print("Please enter one of: Healthy, Good, Fair, Bad")


def create_animal_from_input():
    print("Choose an animal type:")
    print("\t1. Lion")
    print("\t2. Elephant")
    print("\t3. Parrot")
    print("\t4. Chicken")
    print("\t5. Snake")

    while True:
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            name = get_non_empty_input("Enter name: ")
            age = get_positive_number("Enter age in years: ")
            health = get_valid_health("Enter health (Healthy/Good/Fair/Bad): ")
            fur_color = get_non_empty_input("Enter fur color: ")
            return Lion(name, age, "Lion", health, fur_color)
        elif choice == "2":
            name = get_non_empty_input("Enter name: ")
            age = get_positive_number("Enter age in years: ")
            health = get_valid_health("Enter health (Healthy/Good/Fair/Bad): ")
            fur_color = get_non_empty_input("Enter fur color: ")
            return Elephant(name, age, "Elephant", health, fur_color)
        elif choice == "3":
            name = get_non_empty_input("Enter name: ")
            age = get_positive_number("Enter age in years: ")
            health = get_valid_health("Enter health (Healthy/Good/Fair/Bad): ")
            wing_span = get_positive_number("Enter wing span: ")
            return Parrot(name, age, "Parrot", health, wing_span)
        elif choice == "4":
            name = get_non_empty_input("Enter name: ")
            age = get_positive_number("Enter age in years: ")
            health = get_valid_health("Enter health (Healthy/Good/Fair/Bad): ")
            wing_span = get_positive_number("Enter wing span: ")
            return Chicken(name, age, "Chicken", health, wing_span)
        elif choice == "5":
            name = get_non_empty_input("Enter name: ")
            age = get_positive_number("Enter age in years: ")
            health = get_valid_health("Enter health (Healthy/Good/Fair/Bad): ")
            is_venomous_input = input("Is the snake venomous? (yes/no): ").strip().lower()
            while is_venomous_input not in ["yes", "no"]:
                print("Please answer yes or no.")
                is_venomous_input = input("Is the snake venomous? (yes/no): ").strip().lower()
            return Snake(name, age, "Snake", health, is_venomous_input == "yes")
        else:
            print("Invalid choice. Please select a valid animal type.")


def menu():
    print(separator)
    print("           Welcome to the Zoo          ")
    print(separator)
    print("\t1. Add Animal")
    print("\t2. Remove Animal")
    print("\t3. Search Animal")
    print("\t4. Display All Animals")
    print("\t5. Feed Animal")
    print("\t6. Make Animal Sound")
    print("\t7. Animal Activity")
    print("\t8. Exit")
    print(separator)


def main():
    zoo = Zoo()

    while True:
        menu()
        try:
            choice = int(input("\tEnter your choice (1-8): ").strip())
        except ValueError:
            print("Invalid input, please try a number from 1 to 8.")
            continue

        if choice == 1:
            animal = create_animal_from_input()
            zoo.add_animal(animal)
        elif choice == 2:
            zoo.remove_animal()
        elif choice == 3:
            zoo.search_animal()
        elif choice == 4:
            zoo.display_all_animals()
        elif choice == 5:
            zoo.feed_animal()
        elif choice == 6:
            zoo.make_animal_sound()
        elif choice == 7:
            zoo.animal_activity()
        elif choice == 8:
            print("Thank you for your visit in our Zoo")
            break
        else:
            print("Invalid input, please try a number from 1 to 8.")


if __name__ == "__main__":
    main()
