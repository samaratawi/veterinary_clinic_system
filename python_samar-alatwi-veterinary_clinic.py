import os
import textwrap

from IPython.lib.deepreload import found_now


# ====================== Animals class ======================
#============================================================
# The parent class
# This class contains general information (common among all animals)
# Other classes, such as dog or bird classes, can inherit from this class
class Animals:
    def __init__(self,registration_number,name,age,species,is_vaccinated,owner):
        self.__registration_number = registration_number
        self.name = name
        self.__age = age
        self.species = species
        self.__owner = owner
        self.__is_vaccinated = is_vaccinated

    # registration_number, owner,is_vaccinated  private variables
    # Because it is sensitive data, direct access to it is prohibited except through functions.

    #get and set for registration_number
    def get_registration_number(self):
        return  self.__registration_number

    def set_registration_number(self,registration_number):
        if registration_number is int and len(registration_number) == 10:
            self.__registration_number = registration_number
        else:
            print("Invalid Number!")

    #get and set for age
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if isinstance(age,int) and 0 < age < 40:
            self.__age = age
        else:
            print("Invalid Age!")

    #get and set for owner
    def get_owner(self):
        return self.__owner

    def set_owner(self, owner):
        if isinstance(owner,str) and owner.strip() !="" and "," not in owner:
            self.__owner = owner
        else:
            print("Invalid Name!")

    # get and set for is_vaccinated
    def get_is_vaccinated(self):
        return self.__is_vaccinated

    def set_is_vaccinated(self, is_vaccinated):
        if is_vaccinated.isdigit() and (is_vaccinated.strip() == "1" or is_vaccinated.strip() == "2"):
                if is_vaccinated == "1":
                   self.__is_vaccinated  = "Yes"
                else:
                   self.__is_vaccinated  = "No"
        else:
            print("Invalid vaccinated data!")

# ====================== cat class ======================
#=======================================================
# Child Class
#  inherits from the Animals class and extends the parent class
#  by adding cat-specific attributes.
class Cats(Animals):
    def __init__(self,registration_number,name,age,species,is_vaccinated,owner, cat_breed,\
                 activity_level,temperament,favorite_food,is_house_cat,allergies,diagnosis):
        super().__init__(registration_number,name,age,species,is_vaccinated,owner)
        self.cat_breed = cat_breed
        self.activity_level = activity_level
        self.temperament = temperament
        self.favorite_food = favorite_food
        self.__allergies = allergies
        self.is_house_cat = is_house_cat
        self.__diagnosis = diagnosis

    # allergies, diagnosis  private variables
    # Because it is sensitive data, direct access to it is prohibited except through functions.

    #get and set for allergies
    def get_allergies(self):
        return self.__allergies

    def set_allergies(self, allergies):
        if isinstance(allergies,str) and allergies.strip() !="" and "," not in allergies:
            self.__allergies = allergies
        else:
            print("Invalid Name!")

    # get and set for diagnosis
    def get_diagnosis(self):
        return self.__diagnosis

    def set_diagnosis(self, diagnosis):
        if isinstance(diagnosis,str) and diagnosis.strip() !="" and "," not in diagnosis:
            self.__diagnosis = diagnosis
        else:
            print("Invalid Name!")

    # Converts the cat object into a string format
    # This string is used to save the cat data in the text file
    def to_string(self):
        return f"{self.get_registration_number()},{self.name},{self.get_age()},{self.species},\
            {self.get_owner()},{self.get_is_vaccinated()},{self.cat_breed},{self.activity_level},\
            {self.temperament},{self.favorite_food},{self.is_house_cat},{self.__allergies},{self.__diagnosis}"

    # Static method: a method that belongs to the class but does not depend on any specific object.
    # Static method: It is used here to convert a line from the file into a cat object.
    # It reads the stored text and Re-creation the cat instance
    @staticmethod
    def from_string(data):
        registration_number, name, age, species, is_vaccinated, owner, cat_breed, \
            activity_level, temperament, favorite_food,is_house_cat ,allergies \
            ,diagnosis = data.strip().split(",")
        return Cats(registration_number,name,age,species,is_vaccinated,owner, cat_breed,\
                 activity_level,temperament,favorite_food,is_house_cat,allergies,diagnosis)

    def display(self):
            # Table headings are fixed for all data in the Cats class.
            # Therefore, they were entered consistently.
            headers = [
                "registr number", "Name", "Age", "species", "owner","is vaccinated", "cat breed",
                "activity level", "temperament", "favorite food","is house cat", "allergies"]

            width = 18
            #The data was divided into two rows to enable printing.
            #data in two tables below each other instead of one long table.
            table1 = [
                self.get_registration_number(), self.name, self.get_age(),
                self.species, self.get_is_vaccinated(),self.get_owner()
            ]
            table2 = [
                self.cat_breed, self.activity_level, self.temperament,
                self.favorite_food, self.is_house_cat, self.get_allergies()
            ]

            # We split the headers list into two parts
            # so that we display the data in two tables
            # below each other instead of one long table.
            header1 = headers[:6]
            header2 = headers[6:12]

            #Designing the first table
            print("+" + "+".join(["-" * width] * 6) + "+")
            #Print the headings that were divided in (header1) with the headings
            # centered within the previously defined column width
            print("|" + "|".join(h.center(width) for h in header1) + "|")
            print("+" + "+".join(["-" * width] * 6) + "+")
            # Print the data placed in table1, shortening the long text
            # centering the data within the column width.
            print("|" + "|".join(textwrap.shorten(str(x), width=width, placeholder="").center(width) for x in table1) + "|")
            print("+" + "+".join(["-" * width] * 6) + "+")

            #Designing the second table
            print("+" + "+".join(["-" * width] * 6) + "+")
            # Print the headings that were divided in (header2) with the headings
            # centered within the previously defined column width
            print("|" + "|".join(h.center(width) for h in header2) + "|")
            print("+" + "+".join(["-" * width] * 6) + "+")
            # Print the data placed in table2, shortening the long text
            # centering the data within the column width.
            print("|" + "|".join(textwrap.shorten(str(x), width=width, placeholder="").center(width) for x in table2) + "|")
            print("+" + "+".join(["-" * width] * 6) + "+")

            # ---------- diagnosis ----------
            #Print the diagnosis below the table as it contains a long text
            diagnosis = self.get_diagnosis()
            print("diagnosis:")
            print(textwrap.fill(diagnosis, width=115)+"\n")



#==================== Veterinary ===================
#===================================================
# The Veterinary class represents the clinic management system.
# This class is responsible for managing the cat collection within the program.
# It performs operations such as adding, deleting, modifying, reading, and displaying.
class Veterinary:
    def __init__(self, filename):
        self.filename = filename
        #This prepares a location for storing data later
        self.cats = []
        # We prepare a copy of the data for use in the program
        # so that we can perform operations (view, edit, delete,etc).
        self.read_data()


    #This function reads the cat data from the file and adds it to the list within the program.
    #All cats are saved in the list and can be used within the system.
    def read_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    #It takes textual data and converts it into an object containing cat properties.
                    cat = Cats.from_string(line)
                    self.cats.append(cat)

    #Save the data in the list to the file as a single line after converting it to string.
    def save_data_in_file(self):
        with open(self.filename, "w") as file:
            for cat in self.cats:
                ##Convert the cat's data into a string so that it can be saved in the file.
                file.write(cat.to_string() + "\n")

    #Enter data for a new cat from the user and add it to the list of cats
    #save it in the file.
    def add_data(self):
        #Verify inputs before saving them to the variable by calling validation functions
        registration_number = registration_number_verification(self,"Enter Cate registration number: ")
        name = string_verification("Enter Cate name: ")
        age = age_verification("Enter Cate age: ")
        species = string_verification("Enter Animal Type: ")
        is_vaccinated = boolean_verification("cat Has been vaccinated?:\n 1. yes \n 2. no \n  ")
        owner = string_verification("Enter Owner's Cat: ")
        cat_breed = string_verification("Enter cat breed: ")
        activity_level = string_verification("Enter cat activity level: ")
        temperament = string_verification("Enter cat temperament: ")
        favorite_food = string_verification("Enter cat's favorite food: ")
        is_house_cat = boolean_verification("Is it a house cat?:\n 1. yes \n 2. no \n   ")
        allergies = string_verification("Enter cat allergies: ")
        diagnosis = string_verification("Enter cat diagnosis: ")

        #Create a new object of the Cats class containing all the data entered by the user.
        cat = Cats(registration_number,name,age,species,is_vaccinated,owner, cat_breed,\
                 activity_level,temperament,favorite_food,is_house_cat,allergies,diagnosis)
        self.cats.append(cat)
        self.save_data_in_file()
        print("cat data added successfully!")

    # Display data for all cats in the system.
    def view_data(self):
        if not self.cats:
            print("No data available.")
        for cat in self.cats:
            #Print a title for each table.
            print(cat.name,"CAT DATA SHEET")
            #Calling the function to display data for each cat
            cat.display()

    #Delete the cat's data from the system using the registration number.
    def delete_data(self):
        #The user enters the registration number for deleting
        registration_number = input("Enter cat registration_number to delete: ").strip()
        for cat in self.cats:
            if cat.get_registration_number() == registration_number:
                self.cats.remove(cat)
                #After data is deleted, the file is updated (deletion from file).
                self.save_data_in_file()
                print("cat data deleted.")
                return
        print("cat not found.")

    #Update cat data using registration number
    def update_data(self):
        found = False
        ty = True
        #The user enters the registration number for update
        registration_number = input("Enter cat registration_number to update: ").strip()
        for cat in self.cats:
            if cat.get_registration_number() == registration_number:
                found = True
                # Displays a list of data that the user can update.
                # The user cannot update the registration number.
                while True:
                    print("\n===== Update cat data =====")
                    print("1. Edit Cate name")
                    print("2. Edit Cate age")
                    print("3. Edit Animal Type")
                    print("4. Edit Vaccination status")
                    print("5. Edit Owner's Cat")
                    print("6. Edit cat breed")
                    print("7. Edit cat activity level")
                    print("8. Edit cat temperament")
                    print("9. Edit cat's favorite food")
                    print("10. Edit cat allergies")
                    print("11. is it a house cat?")
                    print("12. Edit cat diagnosis")
                    print("13. Exit")

                    Menu = int(input("Choose the service: "))
                    #According to the user's choice,the system allows the user to enter data.
                    #The entered data is verified by calling validation functions.
                    match Menu:
                        case 1:
                            cat.name = string_verification("Edit Cate name: ",ty)
                        case 2:
                            cat.set_age(age_verification("Edit Cate age: ",ty))
                        case 3:
                            cat.species = string_verification("Edit Animal Type: ",ty)
                        case 4:
                            cat.set_is_vaccinated(boolean_verification("cat Has been vaccinated?: ",ty))
                        case 5:
                            cat.set_owner(string_verification("Edit Owner's Cat: ",ty))
                        case 6:
                            cat.cat_breed = string_verification("Edit cat breed: ",ty)
                        case 7:
                            cat.activity_level = string_verification("Edit cat activity level: ",ty)
                        case 8:
                            cat.temperament = string_verification("Edit cat temperament: ",ty)
                        case 9:
                            cat.favorite_food = string_verification("Edit cat's favorite food: ",ty)
                        case 10:
                            cat.is_house_cat = boolean_verification("is it a house cat?: ",ty)
                        case 11:
                            cat.set_allergies(string_verification("Edit cat allergies: ",ty))
                        case 12:
                            cat.set_diagnosis(string_verification("Edit cat diagnosis: ",ty))
                        case 13:
                            print("Have a wonderful day... See you soon!")
                            #Exiting the data update returns the user to the main menu.
                            return
                        case _:
                            print("Invalid choice!")
                    #Save data after update
                    self.save_data_in_file()
                    print("Finish updated process.")
        if not found:
            print("cat not found.")



#==================== for validation =============

#Check that the text input is not empty
def string_verification(message,ty=False):
    #The data entry request is repeated
    # until a valid value is entered.
    while True:
        value = input(message)
        if value.strip() == "" or "," in value:
            print("The field cannot be empty or contain (,)")
            if ty == False: continue
            else: return
        return value.strip()

#Verify that the entered text value represents a valid number
#and text number is (1 or 2)
def boolean_verification(message,ty=False):
    # The data entry request is repeated
    # until a valid value is entered.
    while True:
        value_input = input(message)
        if value_input.isdigit() and (value_input.strip() == "1" or value_input.strip() == "2"):
            if value_input == "1":
                return "Yes"
            else:
                return  "No"
        else:
            print("Enter a valid value")
            if ty == False: continue
            else: return

#Verify that the entered text value represents a valid number
#and text number between (1 and 39)
def age_verification(message,ty=False):
    # The data entry request is repeated
    # until a valid value is entered.
    while True:
        age_input = input(message)
        if age_input.isdigit():
            if 0 < int(age_input) < 40:
                #Converting number after verifying the text represents number.
                #To avoid errors when the user enters characters
                return int(age_input)
            else:
                print("The cat's age should be between 1 and 40")
                if ty == False:continue
                else:return
        else:
            print("Enter a valid value")
            if ty == False: continue
            else: return


#Verify that the number is not registered to another entity (a unique number)
#Verify that the entered text represents a number
#Verify that the entered number contains 10 digits
def registration_number_verification(self,message):
    data = []
    if os.path.exists(self.filename):
        with open(self.filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if parts:
                    data.append(parts[0])

     # The data entry request is repeated
    # until a valid value is entered.
    while True:
        reg_number_input = input(message)
        if len(reg_number_input.strip()) == 10 and reg_number_input.isdigit() and reg_number_input not in data :
            # Converting number after verifying the text represents number.
            # To avoid errors when the user enters characters
            return  int(reg_number_input)
        else:
            print("Enter a valid number")
            continue


#========================= main program ==========
#===========================================
## The system's main function runs a program:
def main_program():

    ##Create object of the class
    Veterinary_system = Veterinary("veterinary_data.txt")


    #Repeats the cycle until the user selects Exit.
    while True:
        print("\n===== Veterinary System Menu =====")
        print("1. Add Cats")
        print("2. View Cats data")
        print("3. Update Cats data")
        print("4. Delete Cats data")
        print("5. Exit")

        Menu = int(input("Choose the service: "))

        #Operations are performed based on user selection.
        match Menu:
            case 1:
                Veterinary_system.add_data()
            case 2:
                Veterinary_system.view_data()
            case 3:
                Veterinary_system.update_data()
            case 4:
                Veterinary_system.delete_data()
            case 5:
                print("Have a wonderful day... See you soon!")
                break
            case _:
                print("Invalid choice!")

#The function called when the program starts
main_program()