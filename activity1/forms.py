from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import NatureParkReservation
from .models import MaayoRF
from .models import Beach, SeabreezeForm
from .models import EcoBayVenueRF
from .models import EcoBayBooking
from django.forms import ModelForm
from .models import Extreme_Reservation
from .models import GuilangTortaOrder,JessieTortaOrder,OjTortaOrder,ChitangTortaOrder,HablonOrder
from .models import JkaMembership, SportsCampMembership, EdmodoMemberShip


from typing import Any
from django import forms
from datetime import datetime
from django.forms import ModelForm
from .models import jsjsreservation
from .models import varlinasreservation
from .models import elkapitanreservation
from .models import threesixtyreservation
from .models import vikingsreservation
from .models import treasurereservation

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(self, *args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control'})
        self.fields['password1'].widget.attrs.update({'class':'form-control'})
        self.fields['password2'].widget.attrs.update({'class':'form-control'})
        
class RequestForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    subject = forms.ChoiceField(choices=(
        ('', 'Select a subject'),
        ('option1', 'Driver for Long Rides'),
        ('option2', 'Tig Picture'),
        ('option3', 'Gym Buddy / Coach'),
    ))
    message = forms.CharField(widget=forms.Textarea)

class OrderForm(forms.Form):
    product_choices = (
        ('product1', 'Product 1'),
        ('product2', 'Product 2'),
        ('product3', 'Product 3'),
    )
    
    product = forms.ChoiceField(choices=product_choices)
    quantity = forms.IntegerField()
    name = forms.CharField(max_length=100)
    email = forms.EmailField()





"""GROUP4 RESERVATION"""
class NatureParkReservationForm(ModelForm):
    class Meta:
        model = NatureParkReservation
        fields = ('edetail', 'etype', 'edate', 'starttime', 'endtime', 'noguest', 'etheme', 'fullname', 'email', 'phonenum')
        widgets = {
            'edetail': forms.TextInput(attrs={'class': 'form-label form-control', 'placeholder': ''}),
            'etype': forms.TextInput(attrs={'class': 'form-label form-control', 'placeholder': ''}),
            'edate': forms.DateInput(attrs={'class': 'datepicker', }),
            'starttime': forms.TimeInput(attrs={'class': 'timepicker'}),
            'endtime': forms.TimeInput(attrs={'class': 'timepicker'}),
            'noguest': forms.NumberInput(attrs={'class': 'form-label form-control','class': 'form-control'}),
            'etheme': forms.TextInput(attrs={'class': 'form-label form-control', 'placeholder': ''}),
            'fullname': forms.TextInput(attrs={'class': 'form-label form-control', 'placeholder': ''}),
            'email': forms.EmailInput(),
            'phonenum': forms.TextInput(attrs={'class': 'form-label form-control', 'placeholder': 'XXXX-XXX-XXXX'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(NatureParkReservationForm, self).__init__(*args, **kwargs)
        self.fields['starttime'].input_formats = ('%I:%M %p',)
        self.fields['endtime'].input_formats = ('%I:%M %p',)  # Set the input format for the time field
        


'''HOTELS AND BEACHES'''
class Beaches(forms.ModelForm):
    class Meta:
        model = Beach
        fields = ['owner','phone','Rdate','time','price']


class MaayoRFS(forms.ModelForm):
    class Meta:
        model = MaayoRF
        fields = ['payment', 'RoomNum', 'ArrivalDate','NumPerson','WakeCall', 'RoomRate','DepartureDate','Adults','Kids','CheckInTime', 'GuestName', 'Accompany' ,'Age' ,'CompNameGroup','Addr' ,'VehicleNum','Nationality','ContactNum','PassportNum','EAddr']

class SeabreezeForms(forms.ModelForm):
    class Meta:
        model = SeabreezeForm
        fields = ['payment', 'RoomNum', 'ArrivalDate','DepartureDate','Adults','Kids','CheckInTime','CheckOutTime', 'GuestName','CompNameGroup','Addr','ContactNum','EAddr']

class EcoBayBookingForm(forms.ModelForm):
     class Meta:
        model = EcoBayBooking
        fields = ('name', 'phone', 'numberOfGuest', 'checkInDate','modeofpayment', 'room')
    
class EcoBayVenueRFForm(forms.ModelForm):
    
    MOP = [
        
        ('gcash', 'Gcash'),
        ('MetroBank', 'Metro Bank'),
    ]
    
    VENUE = [
        
        ('ElizabethHall', 'Elizabeth Hall'),
        ('AlexanderHall', 'Alexander Hall'),
        ('OpenSpaceVenue', 'Open Space Venue'),
    ]
    
    
    fullname = forms.CharField(max_length=50)
    contact = forms.CharField(max_length=20)
    numberofguest = forms.CharField(max_length=50)
    venue = forms.ChoiceField(choices=VENUE)
    date = forms.CharField(max_length=50)
    modeOfpayment = forms.ChoiceField(choices=MOP)
    
    class Meta:
        model = EcoBayVenueRF
        fields = ('fullname', 'contact', 'numberofguest', 'date','modeOfpayment', 'venue')
        
        



'''EXTREME ADVENTURE'''
class Reservation_Form(forms.ModelForm):
    class Meta:
        model = Extreme_Reservation

        fields = [ 'reserved_activity', 'client_name', 'contact_number', 'email',
                  'no_of_adults', 'no_of_children', 'reservation_date', 'reservation_time', 'mode_of_payment'
        ]







class DateInput(forms.DateInput):

    input_type = 'date'

class guilangorderform(ModelForm):

    Classic =   [

        ('empty','Empty'),
        ('class200g','Classic(200g)'),
        ('class335g','Classic(335g)'),
    ]
    Premium = [
        ('empty','Empty'),
        ('prem200g','Premium(200g)'),
        ('prem335g','Premium(335g)'),

    ]
    Tube = [
        ('empty','Empty'),
        ('tube200g','Tube(200g)'),
        ('tube335g','Tube(335g)'),
        ('tube400g','Tube(400g)'),
    ]
   
    

    firstname =forms.CharField(max_length=30)
    middlename = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    address = forms.CharField(max_length=50)
    phonenum = forms.CharField(max_length=11)
    dateofdeliver = forms.DateField(widget=DateInput)
  
 

    product1 = forms.ChoiceField(choices=Classic)
    quantity1 = forms.IntegerField(initial=0)
    product2 = forms.ChoiceField(choices=Classic)
    quantity2 = forms.IntegerField(initial=0)
    product3 = forms.ChoiceField(choices=Premium)
    quantity3 = forms.IntegerField(initial=0)
    product4 = forms.ChoiceField(choices=Premium)
    quantity4 = forms.IntegerField(initial=0)
    product5 = forms.ChoiceField(choices=Tube)
    quantity5 = forms.IntegerField(initial=0)
    product6 = forms.ChoiceField(choices=Tube)
    quantity6 = forms.IntegerField(initial=0)
    product7 = forms.ChoiceField(choices=Tube)
    quantity7 = forms.IntegerField(initial=0)
  

    class Meta:
        model = GuilangTortaOrder
        fields = ('firstname','middlename','lastname','address','phonenum','dateofdeliver','product1','quantity1','product2','quantity2','product3','quantity3', 'product4','quantity4','product5','quantity5','product6','quantity6','product7','quantity7')
   
   

class jessieorderform(ModelForm):

    Torta =  [

        ('empty','Empty'),
        ('torta','Torta Original'),
       
    ]
    Cookies = [
        ('empty','Empty'),
        ('cookies12pcs','Cookies 12pcs/pack'),
        

    ]
  

    firstname =forms.CharField(max_length=30)
    middlename = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    address = forms.CharField(max_length=50)
    phonenum = forms.CharField(max_length=11)
    dateofdeliver = forms.DateField(widget=DateInput)
    product1 = forms.ChoiceField(choices=Torta)
    quantity1 = forms.IntegerField()
    product2 = forms.ChoiceField(choices=Cookies)
    quantity2 = forms.IntegerField()
    

    class Meta:
        model = JessieTortaOrder
        fields = ('firstname','middlename','lastname','address','phonenum','dateofdeliver','product1','quantity1','product2','quantity2')


class ojorderform(ModelForm):

    Torta =  [

        ('empty','Empty'),
        ('TortaClassicBig','Torta Classic (Big)'),
        ('TortaClassicSmall','Torta Classic (Small)'),
        ('TortaUbe','Torta Ube Filling'),
        ('TortaPandan','Torta Panda Filling'),
        ('TortaChocolate','Torta Chocolate Filling'),
       
    ]
    Snacks = [
        ('empty','Empty'),
        ('Salvaro','Salvaro'),
        ('PeanutBroas','Peanut Broas'),
        ('Macaroons','Macaroons'),
        ('Cheesecake','Cheesecake'),
        ('Pastillas','Pastillas'),
        ('Suncake','Suncake'),
        ('BakedPolvoron','Baked Polvoron'),
        ('Peanut Toron','Peanut Toron'),
        

    ]
  

    firstname =forms.CharField(max_length=30)
    middlename = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    address = forms.CharField(max_length=50)
    phonenum = forms.CharField(max_length=11)
    dateofdeliver = forms.DateField(widget=DateInput)
    product1 = forms.ChoiceField(choices=Torta)
    quantity1 = forms.IntegerField(initial=0)
    product2 = forms.ChoiceField(choices=Torta)
    quantity2 = forms.IntegerField(initial=0)
    product3 = forms.ChoiceField(choices=Torta)
    quantity3 = forms.IntegerField(initial=0)
    product4 = forms.ChoiceField(choices=Torta)
    quantity4 = forms.IntegerField(initial=0)
    product5 = forms.ChoiceField(choices=Torta)
    quantity5 = forms.IntegerField(initial=0)
    product6 = forms.ChoiceField(choices=Snacks)
    quantity6 = forms.IntegerField(initial=0)
    product7 = forms.ChoiceField(choices=Snacks)
    quantity7 = forms.IntegerField(initial=0)
    product8 = forms.ChoiceField(choices=Snacks)
    quantity8 = forms.IntegerField(initial=0)
    product9 = forms.ChoiceField(choices=Snacks)
    quantity9 = forms.IntegerField(initial=0)
    product10 = forms.ChoiceField(choices=Snacks)
    quantity10 = forms.IntegerField(initial=0)
    product11 = forms.ChoiceField(choices=Snacks)
    quantity11 = forms.IntegerField(initial=0)
    product12 = forms.ChoiceField(choices=Snacks)
    quantity12 = forms.IntegerField(initial=0)
    product13 = forms.ChoiceField(choices=Snacks)
    quantity13 = forms.IntegerField(initial=0)
  

    class Meta:
        model = OjTortaOrder
        fields = ('firstname','middlename','lastname','address','phonenum','dateofdeliver','product1','quantity1','product2','quantity2','product3','quantity3', 'product4','quantity4','product5','quantity5','product6','quantity6','product7','quantity7','product8','quantity8', 'product9','quantity9','product10','quantity10','product11','quantity11','product12','quantity12','product13','quantity13')

class chitangorderform(ModelForm):

    Torta =  [

        ('empty','Empty'),
        ('TortaBig','Torta Big'),
        ('TortaSmall','Torta Small'),
        ('TortaDozenBig','Torta Dozen Big'),
        ('TortaDozenSmall','Torta Dozen Small'),
        
       
    ]
    Snacks = [
        ('empty','Empty'),
        ('Tostados','Tostados'),
        ('Podreda','Podreda'),
        ('Suncake','Suncake'),
        ('Polvoron','Polvoron'),
        ('MasaPodreda','Masa Podreda'),
        ('Pinato','Pinato'),
        ('Tamarind','Tamarind'),
        ('Pastillas','Pastillas'),
        

    ]
  

    firstname =forms.CharField(max_length=30)
    middlename = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    address = forms.CharField(max_length=50)
    phonenum = forms.CharField(max_length=11)
    dateofdeliver = forms.DateField(widget=DateInput)
    product1 = forms.ChoiceField(choices=Torta)
    quantity1 = forms.IntegerField(initial=0)
    product2 = forms.ChoiceField(choices=Torta)
    quantity2 = forms.IntegerField(initial=0)
    product3 = forms.ChoiceField(choices=Torta)
    quantity3 = forms.IntegerField(initial=0)
    product4 = forms.ChoiceField(choices=Torta)
    quantity4 = forms.IntegerField(initial=0)
    product5 = forms.ChoiceField(choices=Snacks)
    quantity5 = forms.IntegerField(initial=0)
    product6 = forms.ChoiceField(choices=Snacks)
    quantity6 = forms.IntegerField(initial=0)
    product7 = forms.ChoiceField(choices=Snacks)
    quantity7 = forms.IntegerField(initial=0)
    product8 = forms.ChoiceField(choices=Snacks)
    quantity8 = forms.IntegerField(initial=0)
    product9 = forms.ChoiceField(choices=Snacks)
    quantity9 = forms.IntegerField(initial=0)
    product10 = forms.ChoiceField(choices=Snacks)
    quantity10 = forms.IntegerField(initial=0)
    product11 = forms.ChoiceField(choices=Snacks)
    quantity11 = forms.IntegerField(initial=0)
    product12 = forms.ChoiceField(choices=Snacks)
    quantity12 = forms.IntegerField(initial=0)
    
  

    class Meta:
        model = ChitangTortaOrder
        fields = ('firstname','middlename','lastname','address','phonenum','dateofdeliver','product1','quantity1','product2','quantity2','product3','quantity3', 'product4','quantity4','product5','quantity5','product6','quantity6','product7','quantity7','product8','quantity8', 'product9','quantity9','product10','quantity10','product11','quantity11','product12','quantity12')



class hablonorderform(ModelForm):

    Bags =  [

        ('empty','Empty'),
        ('Hinablon Pouch','Hinablon Pouch'),
        ('Hinablon Tote Bag','Hinablon Tote Bag'),
        ('Tote Bag with Embroidered Design','Tote Bag with Embroidered Design'),
        ('Drawstring - Combi','Drawstring - Combi'),
        ('Undok','Undok'),
       
    ]
    Scarf = [
        ('empty','Empty'),
        ('Hand Printed Shawl','Hand Printed Shawl'),
        ('Sabado Towel','Sabado Towel'),
        ('Sabado Blanket','Sabado Blanket'),
        ('Regular Shawl','Regular Shawl'),
        ('Petite Regular Shawl','Petite Regular Shawl'),  

    ]
    Clothes = [
        ('empty','Empty'),
        ('Barong','Barong'),
        ('Barong Dress','Barong Dress'),
        ('Hand Printed Poncho','Hand Printed Poncho'),
        ('Gown','Gown'),
    ]
  

    firstname =forms.CharField(max_length=30)
    middlename = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    address = forms.CharField(max_length=50)
    phonenum = forms.CharField(max_length=11)
    dateofdeliver = forms.DateField(widget=DateInput)
    product1 = forms.ChoiceField(choices=Bags)
    quantity1 = forms.IntegerField(initial=0)
    product2 = forms.ChoiceField(choices=Bags)
    quantity2 = forms.IntegerField(initial=0)
    product3 = forms.ChoiceField(choices=Bags)
    quantity3 = forms.IntegerField(initial=0)
    product4 = forms.ChoiceField(choices=Bags)
    quantity4 = forms.IntegerField(initial=0)
    # product5 = forms.ChoiceField(choices=Bags)
    # quantity5 = forms.IntegerField(initial=0)
    product6 = forms.ChoiceField(choices=Scarf)
    quantity6 = forms.IntegerField(initial=0)
    product7 = forms.ChoiceField(choices=Scarf)
    quantity7 = forms.IntegerField(initial=0)
    product8 = forms.ChoiceField(choices=Scarf)
    quantity8 = forms.IntegerField(initial=0)
    product9 = forms.ChoiceField(choices=Scarf)
    quantity9 = forms.IntegerField(initial=0)
    # product10 = forms.ChoiceField(choices=Scarf)
    # quantity10 = forms.IntegerField(initial=0)
    product11 = forms.ChoiceField(choices=Clothes)
    quantity11 = forms.IntegerField(initial=0)
    product12 = forms.ChoiceField(choices=Clothes)
    quantity12 = forms.IntegerField(initial=0)
    product13 = forms.ChoiceField(choices=Clothes)
    quantity13 = forms.IntegerField(initial=0)
    product14 = forms.ChoiceField(choices=Clothes)
    quantity14 = forms.IntegerField(initial=0)
  

    class Meta:
        model = HablonOrder
        fields = ('firstname','middlename','lastname','address','phonenum','dateofdeliver','product1','quantity1','product2','quantity2','product3','quantity3', 'product4','quantity4','product6','quantity6','product7','quantity7','product8','quantity8', 'product9','quantity9','product11','quantity11','product12','quantity12','product13','quantity13','product14','quantity14')
       
class JkaMemberShip(ModelForm):
  
    class Meta:
        model = JkaMembership
        fields = ('fullname', 'age', 'date_of_birth', 'phone_number', 'cell_number', 'nationality', 'address', 'have_martial_arts_experience', 'if_yes_where', 'parent_name', 'parent_address', 'parent_contact_number')

class SportsCampMembershipForm(ModelForm):
    SPORT_CHOICES = (
        ('Basketball', 'Basketball'),
        ('Volleyball', 'Volleyball'),
    )
    HEALTH_CONDITION_CHOICES = (
        ('Asthma', 'Asthma'),
        ('Hypertension', 'Hypertension'),
        ('Leg/Arm Prosthetics', 'Leg/Arm Prosthetics'),
        ('Allergies', 'Allergies'),
        ('Pre-existing Heart Condition', 'Pre-existing Heart Condition'),
        ('Eyesight Problems', 'Eyesight Problems'), 
    )

    HAVE_PREVIOUS_TRAINING = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    HAVE_MARTIAL_ARTS_EXPERIENCE = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )

    sports_preferred = forms.ChoiceField(widget=forms.RadioSelect,choices=SPORT_CHOICES)
    have_previous_training = forms.ChoiceField(widget=forms.RadioSelect,choices=HAVE_PREVIOUS_TRAINING)
    have_martial_arts_experience = forms.ChoiceField(widget=forms.RadioSelect,choices=HAVE_MARTIAL_ARTS_EXPERIENCE)
    health_condition = forms.MultipleChoiceField(choices=HEALTH_CONDITION_CHOICES, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = SportsCampMembership
        fields = ('ID_number','last_name', 'first_name', 'middle_name', 'nick', 'age', 'date_of_birth', 'gender', 'cellphone_number', 'email_address', 'address', 'grade_level', 'school_attending', 'sports_preferred', 'have_previous_training', 'have_martial_arts_experience', 'fathers_name', 'fathers_cellphone_number', 'fathers_email_address', 'fathers_work_address', 'fathers_work_phone_number', 'mothers_name', 'mothers_cellphone_number', 'mothers_email_address', 'mothers_work_address', 'mothers_work_phone_number', 'emergency_contact_person', 'emergency_contact_number', 'relationship', 'contact_person_address', 'health_condition', 'others')

class EdmodoMemberShipForm(ModelForm):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = forms.ChoiceField(widget=forms.RadioSelect,choices=GENDER_CHOICES)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = EdmodoMemberShip
        fields = ('first_name','family_name', 'middle_name', 'gender', 'date_of_birth', 'mothers_name', 'mothers_contact_number', 'fathers_name', 'fathers_contact_number', 'address', 'postal_city', 'post_code', 'country', 'telephone_number', 'mobile_number', 'email_address', 'last_school_attended', 'date_of_graduation', 'previous_martial_arts_school', 'level_attained', 'person_who_endorse', 'relationship_with', 'any_health_problem', 'medication_taken')












class DateInput(forms.DateInput):

    input_type='date'

class jsjsreservationform(ModelForm):

    room_type = [
        ('Standard Room 2pax Php 1,500.00', 'Standard Room 2pax Php 1,500.00'),
        ('Standard Room 4pax Php 3,000.00', 'Standard Room 4pax Php 3,000.00'),
        ('Dorm Style 10pax Php 5,990.00', 'Dorm Style 10pax Php 5,990.00')
    ]

    payment_method = [
        ('Gcash', 'Gcash'),
        ('Metro Bank', 'Metro Bank'),
        
    ]
    fullname = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    cell_number = forms.CharField(max_length=100)
    check_in = forms.DateField(widget=DateInput, initial=datetime.today().date())
    check_out = forms.DateField(widget=DateInput, initial=datetime.today().date())
    number_guest = forms.IntegerField(initial=0)
    room_accommodation = forms.ChoiceField(choices=room_type)
    payment = forms.ChoiceField(choices=payment_method)


    
    class Meta:
        model = jsjsreservation
        fields = ('fullname', 'address', 'cell_number', 'check_in', 'check_out', 'number_guest', 'room_accommodation', 'payment')

class varlinasreservationform(ModelForm):


    room_type = [
        ('Non Air-conditioned Rooms w/ poolside view: ₱900 per night, good for 2pax', 'Non Air-conditioned Rooms w/ poolside view: ₱900 per night, good for 2pax'),
        ('Air-conditioned Rooms w/ mountain view: ₱1,800 per night, good for 2', 'Air-conditioned Rooms w/ mountain view: ₱1,800 per night, good for 2'),
        ('Barkada Room: ₱3,800 per night, good for 6pax', 'Barkada Room: ₱3,800 per night, good for 6pax')
    ]

    payment_method = [
        ('Gcash', 'Gcash'),
        ('Metro Bank', 'Metro Bank'),
        
    ]
    fullname = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    cell_number = forms.CharField(max_length=100)
    check_in = forms.DateField(widget=DateInput, initial=datetime.today().date())
    check_out = forms.DateField(widget=DateInput, initial=datetime.today().date())
    number_guest = forms.IntegerField(initial=0)
    room_accommodation = forms.ChoiceField(choices=room_type)
    payment = forms.ChoiceField(choices=payment_method)
    
    class Meta:
        model = varlinasreservation
        fields = ('fullname', 'address', 'cell_number', 'check_in', 'check_out', 'number_guest', 'room_accommodation', 'payment')





class elkapitanreservationform(ModelForm):


    room_type = [
        ('Aircondation Room 2pax', 'Aircondation Room  2pax'),
        ('Non-Aircondation Room  2pax', 'Non-Aircondation Room  2pax'),
        ('Barkada Room 6pax', 'Barkada Room 6pax')
    ]

    payment_method = [
        ('Gcash', 'Gcash'),
        ('Metro Bank', 'Metro Bank'),
        
    ]
    fullname = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    cell_number = forms.CharField(max_length=100)
    check_in = forms.DateField(widget=DateInput)
    check_out = forms.DateField(widget=DateInput) 
    number_guest = forms.IntegerField(initial=0)
    room_accommodation = forms.ChoiceField(choices=room_type)
    payment = forms.ChoiceField(choices=payment_method)
    
    class Meta:
        model = elkapitanreservation
        fields = ('fullname', 'address', 'cell_number', 'check_in', 'check_out', 'number_guest', 'room_accommodation', 'payment')


class threesixtyreservationform(ModelForm):


    room_type = [
        ('Aircondation Room 2pax', 'Aircondation Room  2pax'),
        ('Non-Aircondation Room  2pax', 'Non-Aircondation Room  2pax'),
        ('Barkada Room 6pax', 'Barkada Room 6pax')
    ]

    payment_method = [
        ('Gcash', 'Gcash'),
        ('Metro Bank', 'Metro Bank'),
        
    ]
    fullname = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    cell_number = forms.CharField(max_length=100)
    check_in = forms.DateField(widget=DateInput)
    check_out = forms.DateField(widget=DateInput) 
    number_guest = forms.IntegerField(initial=0)
    room_accommodation = forms.ChoiceField(choices=room_type)
    payment = forms.ChoiceField(choices=payment_method)
    
    class Meta:
        model = threesixtyreservation
        fields = ('fullname', 'address', 'cell_number', 'check_in', 'check_out', 'number_guest', 'room_accommodation', 'payment')


class vikingsreservationform(ModelForm):


    room_type = [
        ('Aircondation Room 2pax', 'Aircondation Room  2pax'),
        ('Non-Aircondation Room  2pax', 'Non-Aircondation Room  2pax'),
        ('Barkada Room 6pax', 'Barkada Room 6pax')
    ]

    payment_method = [
        ('Gcash', 'Gcash'),
        ('Metro Bank', 'Metro Bank'),
        
    ]
    fullname = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    cell_number = forms.CharField(max_length=100)
    check_in = forms.DateField(widget=DateInput)
    check_out = forms.DateField(widget=DateInput) 
    number_guest = forms.IntegerField(initial=0)
    room_accommodation = forms.ChoiceField(choices=room_type)
    payment = forms.ChoiceField(choices=payment_method)
    
    class Meta:
        model = vikingsreservation
        fields = ('fullname', 'address', 'cell_number', 'check_in', 'check_out', 'number_guest', 'room_accommodation', 'payment')


class treasurereservationform(ModelForm):


    room_type = [
        ('Aircondation Room 2pax', 'Aircondation Room  2pax'),
        ('Non-Aircondation Room  2pax', 'Non-Aircondation Room  2pax'),
        ('Barkada Room 6pax', 'Barkada Room 6pax')
    ]

    payment_method = [
        ('Gcash', 'Gcash'),
        ('Metro Bank', 'Metro Bank'),
        
    ]
    fullname = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    cell_number = forms.CharField(max_length=100)
    check_in = forms.DateField(widget=DateInput)
    check_out = forms.DateField(widget=DateInput) 
    number_guest = forms.IntegerField(initial=0)
    room_accommodation = forms.ChoiceField(choices=room_type)
    payment = forms.ChoiceField(choices=payment_method)
    
    class Meta:
        model = treasurereservation
        fields = ('fullname', 'address', 'cell_number', 'check_in', 'check_out', 'number_guest', 'room_accommodation', 'payment')

