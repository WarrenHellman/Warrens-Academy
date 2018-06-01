############################
#####Python OOP#############
############################

##########
#Assignment: Bike
##########Create a new class called Bike with the following properties/attributes:

# price
# max_speed
# miles
# Create 3 instances of the Bike class.

# Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a new instance is created.

# Add the following functions to this class:

# displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
# reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
# Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().

# What would you do to prevent the instance from having negative miles?

# Which methods can return self in order to allow chaining methods?

# class Bike():
#     def __init__(self, price, max_speed, miles):
#         self.price = price
#         self.max_speed = max_speed
#         self.miles = miles
#     def displayInfo(self):
#         print "This bike costs "+str(self.price)+" dollars, can go a max speed of "+self.max_speed+" and currently has "+str(self.miles)+" miles on it"
#     def ride(self):
#         print "Riding"
#         self.miles+=10
#         return self
#     def reverse(self):
#         print "Reversing"
#         if self.miles<=4:
#             print "Cannot go negative"
#             return self
#         self.miles-=5
#         return self
        


# bike1 = Bike(8000, "120mph", 574)
# bike2 = Bike(15000, "200mph", 3)
# bike3 = Bike(2000, "80mph", 48000)

# bike1.ride().ride().ride().reverse().displayInfo()
# bike2.reverse().reverse().displayInfo()
# bike3.reverse().reverse().displayInfo()

###################
#Assignment: Car
###################

# Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 

#Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.


# class Car():
#     tax=.12

#     def __init__(self, price, speed, fuel, mileage):
#         self.price = price
#         self.speed = speed
#         self.fuel = fuel
#         self.mileage = mileage
#         if self.price>10000:
#             self.tax=.15
#         self.display_all()
    
#     def display_all(self):
#         print "Price: "+str(self.price)
#         print "Speed: "+ self.speed
#         print "Fuel: "+self.fuel
#         print "Mileage: "+str(self.mileage)
#         print "Tax: "+ str(self.tax)

# car1 = Car(9000, "80mph", "15gal", 15000)
# car2 = Car(100000, "180mph", "5gal", 4000)
# car3 = Car(200000, "280mph", "14gal", 1000)
# car4 = Car(100, "18mph", "45gal", 248000)
# car5 = Car(20000, "60mph", "10gal", 75000)

#####################
# Assignment: Product
#####################

# The owner of a store wants a program to track products. Create a product class to fill the following requirements.
# Product Class:
# Attributes:
# • Price
# • Item Name
# • Weight
# • Brand
# • Status: default "for sale"
# Methods:
# • Sell: changes status to "sold"
# • Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
# • Return: takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been, opened, set the status to "used" and apply a 20% discount.
# • Display Info: show all product details.
# Every method that doesn't have to return something should return self so methods can be chained.

# class Product():
#     def __init__(self, price, name, weight, brand):
#         self.price = price
#         self.name = name
#         self.weight = weight
#         self.brand = brand
#         self.status = "For Sale"

#     def sell(self):
#         self.status = "Sold"
#         return self
#     def addTax(self, taxRate):
#         self.price = self.price+self.price*taxRate
#         return self
#     def returnItem(self, reason):
#         if reason == "defective":
#             self.status = "Defective"
#             self.price = 0
#             return self
#         elif reason == "opened":
#             self.status = "used"
#             self.price = self.price*.8
#             return self
#         else:
#             print "Invalid reason. Use 'defective' or 'opened'"
#             return self
#     def displayInfo(self):
#         print "Price: "+ str(self.price)
#         print "Name: "+ self.name
#         print "Weight: "+ str(self.weight)
#         print "Brand: "+ self.brand
#         print "Status: "+ self.status
#         return self

# item1 = Product(15, "Shoe", 2, "Nike")
# item2 = Product(100, "Cabinet", 100, "Amish")
# item3 = Product(1, "Gum", .5, "Dubble Bubble")
# item4 = Product(1000, "Couch", 400, "Serta")
# item5 = Product(150000, "Boat", 30000, "Bayliner")

# item1.addTax(.10).sell().displayInfo()
# item2.returnItem("dont want").displayInfo()
# item5.returnItem("opened").displayInfo()
# item4.sell().displayInfo()


###################
# Assignment: Animal
###################

# Create an Animal class and give it the below attributes and methods. Extend the Animal class to two child classes, Dog and Dragon.

# Objective
# The objective of this assignment is to help you understand inheritance. Remember that a class is more than just a collection of properties and methods. If you want to create a new class with attributes and methods that are already defined in another class, you can have this new class inherit from that other class (called the parent) instead of copying and pasting code from the original class. Child classes can access all the attributes and methods of a parent class AND have new attributes and methods of its own, for child instances to call. As we see with Wizard / Ninja / Samurai (that are each descended from Human), we can have numerous unique child classes that inherit from the same parent class.

# Animal Class
# Attributes:
# • name
# • health
# Methods:
# • walk: decreases health by one
# • run: health decreases by five
# • display health: print to the terminal the animal's health.
# Create an instance of the Animal, have it walk() three times, run() twice, and finally displayHealth() to confirm that the health attribute has changed.

# class Animal(object):
#     def __init__(self, name):
#         self.name = name
#         self.health=100
#     def walk(self):
#         self.health -=1
#         return self
#     def run(self):
#         self.health-=5
#         return self
#     def displayHealth(self):
#         print "Your health is: "+ str(self.health)


# class Dog(Animal):
#     def __init__(self, name):
#         super(Dog, self).__init__(name)
#         self.health=150
#     def pet(self):
#         self.health+=5
#         return self

# Dog Class
# • inherits everything from Animal
# Attributes:
# • default health of 150
# Methods:
# • pet: increases health by 5
# Have the Dog walk() three times, run() twice, pet() once, and have it displayHealth().
    
# dog= Dog("Michael")
# dog.pet()

# Dragon Class
# • inherits everything from Animal

# Attributes:

# • default health of 170

# Methods:

# • fly: decreases health by 10

# • display health: prints health by calling the parent method and prints "I am a Dragon"

# Now try creating a new Animal and confirm that it can not call the pet() and fly() methods, and its displayHealth() is not saying 'this is a dragon!'. Also confirm that your Dog class can not fly().

# class Dragon(Animal):
#     def __init__(self, name):
#         super(Dragon, self).__init__(name)
#         self.health = 170
#     def fly(self):
#         self.health -= 10
#         return self
#     def displayHealth(self):
#         print "Your health is: "+ str(self.health)
#         print "I am a Dragon"

# dragon = Dragon("Charles")

# dragon.displayHealth()

#############################
#Assignment: Hospital
#############################

#You're going to build a hospital with patients in it! Create a hospital class.

class Hospital(object):
    #KNOWN ISSUE: currently does not adjust bed number assignments for vacancies. How to do that?
    def __init__(self, name, capacity):
        self.patients=["bed not available"]
        self.name=name
        self.capacity=capacity
    def admit(self, patient, fullID):
        #I used a placeholder for the first (0th) bed so bed number will corresond to a conventional number
        #checks to see if there is room in the hospital
        if len(self.patients)>self.capacity:
            print "Cannot admit, hospital is currently full. Please reach out to another hospital"
            return
        else: 
            #adds patient to list of patients
            self.patients.append(fullID)
            #assigns a bed based on the order they are checked in. first patient in first bed, etc
            if fullID in self.patients:
                patient.bedNum = self.patients.index(fullID)
            print fullID +" confirmed and admitted"
            return self
    def discharge(self, patient, fullID):
        # • Discharge: look up and remove a patient from the list of patients. Change bed number for that patient back to none.
        if fullID in self.patients:
            self.patients.remove(fullID)
            patient.bedNum=None
            print "Patient "+fullID+" has been successfully discharged"
            #currently does not adjust bed number assignments for vacancies. How to do that?
            return self
        

class Patient(object):
    def __init__(self, id, name, allergies):
        self.id= id
        self.name=name
        self.allergies=allergies
        self.bedNum=None
        self.fullID = name + " - " + str(id)
    def displayInfo(self):
        print "Name: "+self.name
        print "ID: "+str(self.id)
        print "Bed Number: "+str(self.bedNum)
        print "Allergies: "+ self.allergies


patient1 = Patient(1, "Warren Hellman", "peanut butter")
patient2 = Patient(2, "Erin Korte", "apples")
hospital1 = Hospital("General Hospital", 5)

hospital1.admit(patient1, patient1.fullID)
hospital1.admit(patient2, patient2.fullID)
hospital1.discharge(patient1, patient1.fullID)
hospital1.admit(patient1, patient1.fullID)

patient1.displayInfo()
patient2.displayInfo()
print hospital1.patients

# Before looking at the requirements below, think about the potential characteristics of each patient and hospital. How would you design each?
# Patient:
# Attributes:
# • Id: an id number
# • Name
# • Allergies
# • Bed number: should be none by default
# Hospital
# Attributes:
# • Patients: an empty array
# • Name: hospital name
# • Capacity: an integer indicating the maximum number of patients the hospital can hold.
# Methods:
# • Admit: add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. Return a message either confirming that admission is complete or saying the hospital is full.
# • Discharge: look up and remove a patient from the list of patients. Change bed number for that patient back to none.
# This is a challenging assignment. Ask yourself what input each method requires and what output you will need.