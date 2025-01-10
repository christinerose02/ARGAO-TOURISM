from django.db import models
from django.contrib import admin




# Create your models here.
class Accounts(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email


# class RequestForm(models.Model):
#     CHOICES = (
#         ('', 'Select a subject'),
#         ('option1', 'Driver for Long Rides'),
#         ('option2', 'Third wheel for Dates'),
#         ('option3', 'Gym Buddy / Coach'),
#     )

#     email = models.EmailField()
#     name = models.CharField(max_length=50)
#     phonenumber = models.CharField(max_length=20)
#     subject = models.CharField(max_length=20, choices=CHOICES)
#     message = models.TextField()

#     def __str__(self):
#         return self.name
# # Orderform here.    
# class OrderForm(models.Model):
#     product = models.CharField(max_length=100)
#     quantity = models.IntegerField()
#     name = models.CharField(max_length=100)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name

"""class RequestForm(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=20)
    subject = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return self.name """
        
        
        
        
        
        
        
        
        
"""GROUP 4 RESERVATION"""
class NatureParkReservation(models.Model):
    edetail = models.CharField('Event detail', max_length=250)
    etype = models.CharField('Event type', max_length=40)
    edate  = models.DateField('Event date')
    starttime = models.TimeField('Event Start Time')
    endtime  = models.TimeField('Event End Time')
    noguest = models.IntegerField('Number of Guest')                                  
    etheme =models.CharField('Event theme', max_length=70)
    fullname = models.CharField('Full name of Client',max_length=50)
    email = models.EmailField('Email address')
    phonenum = models.CharField('Phone number', max_length=11)
    
    






'''Hotels and Beaches'''
class MaayoRF(models.Model):
    PAYMENTS = [
        ('Cash','Cash'),
        ('CreditCard','Credit Card'),
        ('Others','Others'),
    ]
    payment = models.CharField(max_length=50, choices=PAYMENTS)
    RoomNum = models.IntegerField()
    ArrivalDate = models.DateField()
    NumPerson = models.IntegerField()
    WakeCall = models.TimeField()
    RoomRate = models.IntegerField()
    DepartureDate = models.DateField()
    Adults = models.IntegerField()
    Kids = models.IntegerField()
    CheckInTime = models.TimeField()
    GuestName = models.CharField(max_length=200)
    Accompany = models.CharField(max_length=100)
    Age = models.IntegerField()
    CompNameGroup = models.CharField(max_length=200)
    Addr = models.CharField(max_length=200)
    VehicleNum = models.IntegerField()
    Nationality = models.CharField(max_length=50)
    ContactNum = models.IntegerField()
    PassportNum = models.IntegerField()
    EAddr = models.EmailField()
    
    def __str__(self):
        return self.GuestName

class EcoBayBooking(models.Model):
    MOPS = [
        
        ('gcash', 'Gcash'),
        ('MetroBank', 'Metro Bank'),
    ]
    
    ROOM = [
        
        ('StandardRoom', 'Standard Room'),
        ('DeLuxeRoom', 'De Luxe Room'),
        ('ExecutiveRoom', 'Executive Room'),
    ]

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    numberOfGuest = models.CharField(max_length=50)
    room = models.CharField(max_length=50)
    checkInDate = models.CharField(max_length=50)
    modeofpayment = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name

class EcoBayVenueRF(models.Model):
    MOP = [
        
        ('gcash', 'Gcash'),
        ('MetroBank', 'Metro Bank'),
    ]
    
    VENUE = [
        
        ('ElizabethHall', 'Elizabeth Hall'),
        ('AlexanderHall', 'Alexander Hall'),
        ('OpenSpaceVenue', 'Open Space Venue'),
    ]

    fullname = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    numberofguest = models.CharField(max_length=50)
    venue = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    modeOfpayment = models.CharField(max_length=50)
    

class Beach(models.Model):
    OWNERNAME = [
        ('ALBARRACIN', 'ALBARRACIN'),
        ('BIRONDO', 'BIRONDO'),
        ('CEUVAS', 'CUEVAS'),
        ('LARGO', 'LARGO'),
        ('YBANEZ', 'YBANEZ'),
        ('LASOLA', 'LASOLA'),
        ('SAYSON', 'SAYSON'),
    ]
    owner = models.CharField(max_length=50, choices=OWNERNAME)
    phone = models.IntegerField()
    Rdate = models.DateField()
    time = models.TimeField()
    RESERVATION_CHOICES = [
        ('price300', '300'),
        ('price500', '500'),
        ('price250-300', '250-300'),
        ('price400-500', '400-500'),
        ('price400', '400'),
    ]
    price = models.CharField(max_length=20, choices=RESERVATION_CHOICES)

    def __str__(self):
        if self.owner == "SAYSON":
            return 'MAHAYAHAY/' + self.owner
        else:
            return 'LAWIS/' + self.owner
        
class MaayoForm(models.Model):
    PAYMENTS = [
        ('Cash','Cash'),
        ('CreditCard','Credit Card'),
        ('Others','Others'),
    ]
    payment = models.CharField(max_length=50, choices=PAYMENTS)
    RoomNum = models.IntegerField()
    ArrivalDate = models.DateField()
    NumPerson = models.IntegerField()
    WakeCall = models.TimeField()
    RoomRate = models.IntegerField()
    DepartureDate = models.DateField()
    Adults = models.IntegerField()
    Kids = models.IntegerField()
    CheckInTime = models.TimeField()
    GuestName = models.CharField(max_length=100)
    Accompany = models.CharField(max_length=100)
    Age = models.IntegerField()
    CompNameGroup = models.CharField(max_length=200)
    Addr = models.CharField(max_length=200)
    VehicleNum = models.IntegerField()
    Nationality = models.CharField(max_length=50)
    ContactNum = models.IntegerField()
    PassportNum = models.IntegerField()
    EAddr = models.EmailField()
    
    def __str__(self):
        return self.GuestName
    
class SeabreezeForm(models.Model):
    PAYMENTS = [
        ('Cash','Cash'),
        ('CreditCard','Credit Card'),
        ('Others','Others'),
    ]
    payment = models.CharField(max_length=50, choices=PAYMENTS)
    RoomNum = models.IntegerField()
    ArrivalDate = models.DateField()
    DepartureDate = models.DateField()
    Adults = models.IntegerField()
    Kids = models.IntegerField()
    CheckInTime = models.TimeField()	
    CheckOutTime = models.TimeField()
    GuestName = models.CharField(max_length=100)
    CompNameGroup = models.CharField(max_length=200)
    Addr = models.CharField(max_length=200)
    ContactNum = models.IntegerField()
    EAddr = models.EmailField()
    
    def __str__(self):
        return self.GuestName
    
class EcoBayVenueRF(models.Model):
    MOP = [
        ('gcash', 'Gcash'),
        ('MetroBank', 'Metro Bank'),
    ]
    
    VENUES = [
        ('ElizabethHall', 'Elizabeth Hall'),
        ('AlexanderHall', 'Alexander Hall'),
        ('OpenSpaceVenue', 'Open Space Venue'),
    ]
    
    
    fullname = models.CharField(max_length=50)
    contact = models.IntegerField()
    numberofguest = models.IntegerField()
    date = models.DateField()
    modeOfpayment = models.CharField(max_length=50, choices=MOP)
    venue = models.CharField(max_length=50, choices=VENUES)

    def __str__(self):
        return self.fullname
    




'''EXTREME ADVENTURES'''
class Extreme_Reservation(models.Model):
    reservation_reference = models.AutoField(primary_key=True, editable=False)
    reserved_activity = models.CharField(max_length=200)
    client_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    email = models.CharField(max_length=200)
    no_of_adults = models.CharField(max_length=50)
    no_of_children = models.CharField(max_length=50)
    reservation_date = models.CharField(max_length=50)
    reservation_time = models.CharField(max_length=50)
    mode_of_payment = models.CharField(max_length=50)

    def __str__(self):
        return "Reservation Reference: " + self.reservation_reference.__str__() + " | Client Representative: " + self.client_name + " | Reservation Date: " + self.reservation_date

class HablonOrder(models.Model):
    ordernum = models.AutoField('Order Number',primary_key=True)

    firstname = models.CharField('First name',max_length=30)
    middlename = models.CharField('Middle name', max_length=30)
    lastname = models.CharField('Last name',max_length=30)
    address = models.CharField('address',max_length=50)
    phonenum = models.CharField('Phone Number', max_length=11)
    dateofdeliver = models.DateField('Date of Delivery')
    product1 = models.CharField('Product Name', max_length=50)
    quantity1 = models.IntegerField('Quantity',default="0")
    product2 = models.CharField('Product Name', max_length=50)
    quantity2 = models.IntegerField('Quantity',default="0")
    product3 = models.CharField('Product Name', max_length=50)
    quantity3 = models.IntegerField('Quantity',default="0")
    product4 = models.CharField('Product Name', max_length=50)
    quantity4 = models.IntegerField('Quantity',default="0")
    # product5 = models.CharField('Product Name', max_length=50)
    # quantity5 = models.IntegerField('Quantity',default="0")
    product6 = models.CharField('Product Name', max_length=50)
    quantity6 = models.IntegerField('Quantity',default="0")
    product7 = models.CharField('Product Name', max_length=50)
    quantity7 = models.IntegerField('Quantity',default="0")
    product8 = models.CharField('Product Name', max_length=50)
    quantity8 = models.IntegerField('Quantity',default="0")
    product9 = models.CharField('Product Name', max_length=50)
    quantity9 = models.IntegerField('Quantity',default="0")
    # product10 = models.CharField('Product Name', max_length=50)
    # quantity10 = models.IntegerField('Quantity',default="0")
    product11 = models.CharField('Product Name', max_length=50)
    quantity11 = models.IntegerField('Quantity',default="0")
    product12 = models.CharField('Product Name', max_length=50)
    quantity12 = models.IntegerField('Quantity',default="0")
    product13 = models.CharField('Product Name', max_length=50)
    quantity13 = models.IntegerField('Quantity',default="0")
    product14 = models.CharField('Product Name', max_length=50)
    quantity14 = models.IntegerField('Quantity',default="0")

    def __str__(self):
        return f"Order Number: {self.ordernum}"

class GuilangTortaOrder(models.Model):
    ordernum = models.AutoField('Order Number',primary_key=True)
   
    firstname = models.CharField('First name',max_length=30)
    middlename = models.CharField('Middle name', max_length=30)
    lastname = models.CharField('Last name',max_length=30)
    address = models.CharField('address',max_length=50)
    phonenum = models.CharField('Phone Number', max_length=11)
    dateofdeliver = models.DateField('Date of Delivery')
    product1 = models.CharField('Product Name', max_length=50)
    quantity1 = models.IntegerField('Quantity',default="0")
    product2 = models.CharField('Product Name', max_length=50)
    quantity2 = models.IntegerField('Quantity',default="0")
    product3 = models.CharField('Product Name', max_length=50)
    quantity3 = models.IntegerField('Quantity',default="0")
    product4 = models.CharField('Product Name', max_length=50)
    quantity4 = models.IntegerField('Quantity',default="0")
    product5 = models.CharField('Product Name', max_length=50)
    quantity5 = models.IntegerField('Quantity',default="0")
    product6 = models.CharField('Product Name', max_length=50)
    quantity6 = models.IntegerField('Quantity',default="0")
    product7 = models.CharField('Product Name', max_length=50)
    quantity7 = models.IntegerField('Quantity',default="0")
   
    def __str__(self):
        return f"Order Number: {self.ordernum}"

class JessieTortaOrder(models.Model):
    ordernum = models.AutoField('Order Number',primary_key=True)

    firstname = models.CharField('First name',max_length=30)
    middlename = models.CharField('Middle name', max_length=30)
    lastname = models.CharField('Last name',max_length=30)
    address = models.CharField('address',max_length=50)
    phonenum = models.CharField('Phone Number', max_length=11)
    dateofdeliver = models.DateField('Date of Delivery')
    product1 = models.CharField('Product Name', max_length=50)
    quantity1 = models.IntegerField('Quantity')
    product2 = models.CharField('Product Name', max_length=50)
    quantity2 = models.IntegerField('Quantity')
    
    def __str__(self):
        return f"Order Number: {self.ordernum}"


class OjTortaOrder(models.Model):
    ordernum = models.AutoField('Order Number',primary_key=True)

    firstname = models.CharField('First name',max_length=30)
    middlename = models.CharField('Middle name', max_length=30)
    lastname = models.CharField('Last name',max_length=30)
    address = models.CharField('address',max_length=50)
    phonenum = models.CharField('Phone Number', max_length=11)
    dateofdeliver = models.DateField('Date of Delivery')
    product1 = models.CharField('Product Name', max_length=50)
    quantity1 = models.IntegerField('Quantity',default="0")
    product2 = models.CharField('Product Name', max_length=50)
    quantity2 = models.IntegerField('Quantity',default="0")
    product3 = models.CharField('Product Name', max_length=50)
    quantity3 = models.IntegerField('Quantity',default="0")
    product4 = models.CharField('Product Name', max_length=50)
    quantity4 = models.IntegerField('Quantity',default="0")
    product5 = models.CharField('Product Name', max_length=50)
    quantity5 = models.IntegerField('Quantity',default="0")
    product6 = models.CharField('Product Name', max_length=50)
    quantity6 = models.IntegerField('Quantity',default="0")
    product7 = models.CharField('Product Name', max_length=50)
    quantity7 = models.IntegerField('Quantity',default="0")
    product8 = models.CharField('Product Name', max_length=50)
    quantity8 = models.IntegerField('Quantity',default="0")
    product9 = models.CharField('Product Name', max_length=50)
    quantity9 = models.IntegerField('Quantity',default="0")
    product10 = models.CharField('Product Name', max_length=50)
    quantity10 = models.IntegerField('Quantity',default="0")
    product11 = models.CharField('Product Name', max_length=50)
    quantity11 = models.IntegerField('Quantity',default="0")
    product12 = models.CharField('Product Name', max_length=50)
    quantity12 = models.IntegerField('Quantity',default="0")
    product13 = models.CharField('Product Name', max_length=50)
    quantity13 = models.IntegerField('Quantity',default="0")
   

    def __str__(self):
        return f"Order Number: {self.ordernum}"
    
class ChitangTortaOrder(models.Model):
    ordernum = models.AutoField('Order Number',primary_key=True)

    firstname = models.CharField('First name',max_length=30)
    middlename = models.CharField('Middle name', max_length=30)
    lastname = models.CharField('Last name',max_length=30)
    address = models.CharField('address',max_length=50)
    phonenum = models.CharField('Phone Number', max_length=11)
    dateofdeliver = models.DateField('Date of Delivery')
    product1 = models.CharField('Product Name', max_length=50)
    quantity1 = models.IntegerField('Quantity',default="0")
    product2 = models.CharField('Product Name', max_length=50)
    quantity2 = models.IntegerField('Quantity',default="0")
    product3 = models.CharField('Product Name', max_length=50)
    quantity3 = models.IntegerField('Quantity',default="0")
    product4 = models.CharField('Product Name', max_length=50)
    quantity4 = models.IntegerField('Quantity',default="0")
    product5 = models.CharField('Product Name', max_length=50)
    quantity5 = models.IntegerField('Quantity',default="0")
    product6 = models.CharField('Product Name', max_length=50)
    quantity6 = models.IntegerField('Quantity',default="0")
    product7 = models.CharField('Product Name', max_length=50)
    quantity7 = models.IntegerField('Quantity',default="0")
    product8 = models.CharField('Product Name', max_length=50)
    quantity8 = models.IntegerField('Quantity',default="0")
    product9 = models.CharField('Product Name', max_length=50)
    quantity9 = models.IntegerField('Quantity',default="0")
    product10 = models.CharField('Product Name', max_length=50)
    quantity10 = models.IntegerField('Quantity',default="0")
    product11 = models.CharField('Product Name', max_length=50)
    quantity11 = models.IntegerField('Quantity',default="0")
    product12 = models.CharField('Product Name', max_length=50)
    quantity12 = models.IntegerField('Quantity',default="0")
   

    def __str__(self):
        return f"Order Number: {self.ordernum}"
    
class JkaMembership(models.Model):
        
    membership_ID = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    age = models.IntegerField()
    date_of_birth = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    cell_number = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    have_martial_arts_experience = models.CharField(max_length=50, default = False)
    if_yes_where = models.CharField(max_length=100)
    parent_name = models.CharField(max_length=100)
    parent_address = models.CharField(max_length=100)
    parent_contact_number = models.CharField(max_length=100)
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "JKA Membership"
        verbose_name_plural = "JKA Memberships"

class SportsCampMembership(models.Model):
    # SPORT_CHOICES = (
    #     ('Basketball', 'Basketball'),
    #     ('Volleyball', 'Volleyball'),
    # )
    # ASTHMA = 'Asthma'
    # HYPERTENSION = 'Hypertension'
    # LEG_ARM_PROSTHETICS = 'Leg/Arm Prosthetics'
    # ALLERGIES = 'Allergies'
    # PRE_EXISTING_HEART_CONDITION = 'Pre-existing Heart Condition'
    # EYESIGHT_PROBLEMS = 'Eyesight Problems'

    # HEALTH_CONDITION_CHOICES = (
    #     (ASTHMA, 'Asthma'),
    #     (HYPERTENSION, 'Hypertension'),
    #     (LEG_ARM_PROSTHETICS, 'Leg/Arm Prosthetics'),
    #     (ALLERGIES, 'Allergies'),
    #     (PRE_EXISTING_HEART_CONDITION, 'Pre-existing Heart Condition'),
    #     (EYESIGHT_PROBLEMS, 'Eyesight Problems')
        
    # )
    ID_number = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    nick = models.CharField(max_length=100)
    age = models.IntegerField()
    date_of_birth = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    cellphone_number = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    grade_level = models.CharField(default="College",max_length=100)
    school_attending = models.CharField(max_length=100)
    sports_preferred = models.CharField(max_length=255, blank=True)
    have_previous_training = models.CharField(max_length=100)
    have_martial_arts_experience = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    fathers_cellphone_number = models.IntegerField()
    fathers_email_address = models.CharField(max_length=100)
    fathers_work_address = models.CharField(max_length=100)
    fathers_work_phone_number = models.CharField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    mothers_cellphone_number = models.IntegerField()
    mothers_email_address = models.CharField(max_length=100)
    mothers_work_address = models.CharField(max_length=100)
    mothers_work_phone_number = models.CharField(max_length=100)
    emergency_contact_person = models.CharField(max_length=100)
    emergency_contact_number = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    contact_person_address = models.CharField(max_length=100)
    health_condition = models.CharField(max_length=255, blank=True)  
    others = models.CharField(default="None",max_length=255) 
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


    class Meta:
        verbose_name = "Sports Camp Membership"
        verbose_name_plural = "Sports Camp Memberships"

class EdmodoMemberShip(models.Model):
    member_ship_ID = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    date_of_birth = models.DateField(max_length=100)
    mothers_name = models.CharField(max_length=100)
    mothers_contact_number = models.IntegerField()
    fathers_name = models.CharField(max_length=100)
    fathers_contact_number = models.IntegerField()
    address = models.CharField(max_length=100)
    postal_city = models.CharField(max_length=100)
    post_code = models.CharField(default="6021",max_length=100)
    country = models.CharField(max_length=100)
    telephone_number = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    last_school_attended = models.CharField(max_length= 100)
    date_of_graduation = models.CharField(max_length = 100)
    previous_martial_arts_school = models.CharField(default="None",max_length= 100)
    level_attained = models.CharField(max_length= 100)
    person_who_endorse = models.CharField(max_length=100)
    relationship_with = models.CharField(max_length = 100)
    any_health_problem = models.CharField(default="None",max_length=100)
    medication_taken = models.CharField(default="None", max_length= 100)
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


    class Meta:
        verbose_name = "Tong-Il Moo-Do Membership"
        verbose_name_plural = "Tong-Il Moo-Do Memberships"















class jsjsreservation(models.Model):
   
    reservation_number = models.AutoField('Reservation Number', primary_key=True)
    fullname = models.CharField('Full Name',max_length=100)
    address = models.CharField('Address',max_length=100)
    cell_number = models.CharField('Cellphone Number' ,max_length=100)
    check_in = models.DateField('Check In Date' ,max_length=100)
    check_out = models.DateField('Check Out Date',max_length=100) 
    number_guest = models.IntegerField('Number of Guest')
    room_accommodation = models.CharField('Room Accommodation' ,max_length=100)
    payment = models.CharField('Payment Method',max_length=100)


    @property
    def dateofstay(self):
        if(self.check_out != None):
            dateofstay = self.check_out - self.check_in
            return dateofstay

    @property
    def price(self):
        if(self.room_accommodation == "Standard Room 2pax Php 1,500.00"):
            price = self.dateofstay * 1500
            return price
        if(self.room_accommodation == "Standard Room 4pax Php 3,000.00"):
            price = self.dateofstay * 3000
            return price
        if(self.room_accommodation == "Dorm Style 10pax Php 5,990.00"):
            price = self.dateofstay * 59900
            return price
    

        
    @property
    def remainingpayment(self):
        if(self.price != None ):
            remainingpayment = self.price / 2
            return remainingpayment
 
    
    
class varlinasreservation(models.Model):
    
    reservation_number = models.AutoField('Reservation Number', primary_key=True)
    fullname = models.CharField('Full Name',max_length=100)
    address = models.CharField('Address',max_length=100)
    cell_number = models.CharField('Cellphone Number' ,max_length=100)
    check_in = models.DateField('Check In Date' ,max_length=100)
    check_out = models.DateField('Check Out Date',max_length=100) 
    number_guest = models.IntegerField('Number of Guest')
    room_accommodation = models.CharField('Room Accommodation' ,max_length=100)
    payment = models.CharField('Payment Method',max_length=100)

    @property
    def dateofstay(self):
        if(self.check_out != None):
            dateofstay = self.check_out - self.check_in
            return dateofstay
    
    @property
    def price(self):
        if(self.room_accommodation == "Non Air-conditioned Rooms w/ poolside view: ₱900 per night, good for 2pax"):
            price = self.dateofstay * 900
            return price
        if(self.room_accommodation == "Air-conditioned Rooms w/ mountain view: ₱1,800 per night, good for 2"):
            price = self.dateofstay * 1800
            return price
        if(self.room_accommodation == "Barkada Room: ₱3,800 per night, good for 6pax"):
            price = self.dateofstay * 3800
            return price
          
    @property
    def remainingpayment(self):
        if(self.price != None ):
            remainingpayment = self.price / 2
            return remainingpayment
 
    def __str__(self):
        return self.name
    
class elkapitanreservation(models.Model):
    
    reservation_number = models.AutoField('Reservation Number', primary_key=True)
    fullname = models.CharField('Full Name',max_length=100)
    address = models.CharField('Address',max_length=100)
    cell_number = models.CharField('Cellphone Number' ,max_length=100)
    check_in = models.DateField('Check In Date' ,max_length=100)
    check_out = models.DateField('Check Out Date',max_length=100) 
    number_guest = models.IntegerField('Number of Guest')
    room_accommodation = models.CharField('Room Accommodation' ,max_length=100)
    payment = models.CharField('Payment Method',max_length=100)
    
    def __str__(self):
        return self.name
    

class threesixtyreservation(models.Model):
    
    reservation_number = models.AutoField('Reservation Number', primary_key=True)
    fullname = models.CharField('Full Name',max_length=100)
    address = models.CharField('Address',max_length=100)
    cell_number = models.CharField('Cellphone Number' ,max_length=100)
    check_in = models.DateField('Check In Date' ,max_length=100)
    check_out = models.DateField('Check Out Date',max_length=100) 
    number_guest = models.IntegerField('Number of Guest')
    room_accommodation = models.CharField('Room Accommodation' ,max_length=100)
    payment = models.CharField('Payment Method',max_length=100)
    
    def __str__(self):
        return self.name
    
class vikingsreservation(models.Model):
    
    reservation_number = models.AutoField('Reservation Number', primary_key=True)
    fullname = models.CharField('Full Name',max_length=100)
    address = models.CharField('Address',max_length=100)
    cell_number = models.CharField('Cellphone Number' ,max_length=100)
    check_in = models.DateField('Check In Date' ,max_length=100)
    check_out = models.DateField('Check Out Date',max_length=100) 
    number_guest = models.IntegerField('Number of Guest')
    room_accommodation = models.CharField('Room Accommodation' ,max_length=100)
    payment = models.CharField('Payment Method',max_length=100)
    
    def __str__(self):
        return self.name
    
class treasurereservation(models.Model):
    
    reservation_number = models.AutoField('Reservation Number', primary_key=True)
    fullname = models.CharField('Full Name',max_length=100)
    address = models.CharField('Address',max_length=100)
    cell_number = models.CharField('Cellphone Number' ,max_length=100)
    check_in = models.DateField('Check In Date' ,max_length=100)
    check_out = models.DateField('Check Out Date',max_length=100) 
    number_guest = models.IntegerField('Number of Guest')
    room_accommodation = models.CharField('Room Accommodation' ,max_length=100)
    payment = models.CharField('Payment Method',max_length=100)
    
    def __str__(self):
        return self.name