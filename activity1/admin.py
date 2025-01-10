from django.contrib import admin

from .models import Accounts, MaayoRF
from .models import NatureParkReservation
from .models import Beach, SeabreezeForm
from .models import EcoBayBooking
from .models import EcoBayVenueRF
from .models import Extreme_Reservation
from .models import JkaMembership, SportsCampMembership, EdmodoMemberShip
from django.utils import timezone


from .models import jsjsreservation
from .models import varlinasreservation
from .models import elkapitanreservation
from .models import threesixtyreservation
from .models import vikingsreservation
from .models import treasurereservation

from .models import GuilangTortaOrder,JessieTortaOrder,OjTortaOrder,ChitangTortaOrder,HablonOrder

admin.site.register
admin.site.register(Extreme_Reservation)
    
    
    
    

# Register your models here.
class AccountsAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'password')

admin.site.register(Accounts, AccountsAdmin)
#admin.site.register(Accounts)

@admin.register(NatureParkReservation)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phonenum','etype', 'edetail','edate', 'starttime', 'endtime', 'noguest', 'etheme')
    ordering = ('fullname',)
    search_fields = ('fullname', 'etype')



'''Hotels and Beaches'''
@admin.register(MaayoRF)
class Maayoadmin(admin.ModelAdmin):
    list_display = [ 'GuestName','ContactNum','EAddr', 'RoomNum','ArrivalDate','DepartureDate', 'NumPerson','Adults','Kids', 'RoomRate','payment','CheckInTime','WakeCall', 'Accompany' ,'Age' ,'CompNameGroup','Addr' ,'VehicleNum','Nationality','PassportNum']

@admin.register(Beach)
class Beachadmin(admin.ModelAdmin):
    list_display= ['owner','phone','Rdate','time','price']

@admin.register(SeabreezeForm)
class Seabreezeadmin(admin.ModelAdmin):
    list_display = ['GuestName','ContactNum','EAddr','RoomNum', 'ArrivalDate','DepartureDate','Adults','Kids','CheckInTime','CheckOutTime','payment', 'CompNameGroup','Addr']


@admin.register(EcoBayBooking)
class EcoBayBookingadmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'numberOfGuest', 'checkInDate', 'modeofpayment', 'room')

@admin.register(EcoBayVenueRF)
class EcoBayVenueRFadmin(admin.ModelAdmin):
    list_display = ('fullname', 'contact', 'numberofguest', 'date', 'modeOfpayment', 'venue')
    
@admin.register(JkaMembership)
class JkaMembershipAdmin(admin.ModelAdmin):
    list_display = ('membership_ID', 'fullname', 'age', 'date_of_birth', 'phone_number', 'cell_number', 'nationality', 'address', 'have_martial_arts_experience', 'if_yes_where', 'parent_name', 'parent_address', 'parent_contact_number', 'received_at')
    ordering = ('membership_ID', 'fullname',)
    search_fields = ('membership_ID', 'fullname')

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.received_at = timezone.now()
        super().save_model(request, obj, form, change)

@admin.register(SportsCampMembership)
class SportsCampMembershipAdmin(admin.ModelAdmin):
    list_display = ('ID_number','last_name', 'first_name', 'middle_name', 'nick', 'age', 'date_of_birth', 'gender', 'cellphone_number', 'email_address', 'address', 'grade_level', 'school_attending', 'sports_preferred', 'have_previous_training', 'have_martial_arts_experience', 'fathers_name', 'fathers_cellphone_number', 'fathers_email_address', 'fathers_work_address','fathers_work_phone_number', 'mothers_name', 'mothers_cellphone_number', 'mothers_email_address', 'mothers_work_address','mothers_work_phone_number', 'emergency_contact_person', 'emergency_contact_number', 'relationship', 'contact_person_address', 'health_condition', 'others', 'received_at')
    ordering = ('ID_number',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.received_at = timezone.now()
        super().save_model(request, obj, form, change)

@admin.register(EdmodoMemberShip)
class EdmodoMemberShipAdmin(admin.ModelAdmin):
    list_display = ('first_name','family_name', 'middle_name', 'gender', 'date_of_birth', 'mothers_name', 'mothers_contact_number', 'fathers_name', 'fathers_contact_number', 'address', 'postal_city', 'post_code', 'country', 'telephone_number', 'mobile_number', 'email_address', 'last_school_attended', 'date_of_graduation','previous_martial_arts_school', 'level_attained', 'person_who_endorse', 'relationship_with', 'any_health_problem', 'medication_taken', 'received_at')
    ordering = ('first_name',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.received_at = timezone.now()
        super().save_model(request, obj, form, change)    
        
        









@admin.register(jsjsreservation)
class jsjsAdmin(admin.ModelAdmin):
    list_display = ('reservation_number','fullname', 'address', 'cell_number', 'check_in', 'check_out','dateofstay', 'number_guest', 'room_accommodation','payment','price','remainingpayment')
    search_fields = ('fullname', 'address')

@admin.register(varlinasreservation)
class varlinasAdmin(admin.ModelAdmin):
    list_display = ('reservation_number','fullname', 'address', 'cell_number', 'check_in', 'check_out', 'number_guest', 'room_accommodation','payment','price','remainingpayment')
    search_fields = ('fullname', 'address')

@admin.register(elkapitanreservation)
class elAdmin(admin.ModelAdmin):
    list_display = ('reservation_number','fullname', 'address', 'cell_number', 'check_in', 'check_out', 'number_guest', 'room_accommodation','payment')
    search_fields = ('fullname', 'address')
@admin.register(threesixtyreservation)
class threesixtyAdmin(admin.ModelAdmin):
    list_display = ('reservation_number','fullname', 'address', 'cell_number', 'check_in', 'check_out', 'number_guest', 'room_accommodation','payment')
    search_fields = ('fullname', 'address')
@admin.register(vikingsreservation)
class vikingsAdmin(admin.ModelAdmin):
    list_display = ('reservation_number','fullname', 'address', 'cell_number', 'check_in', 'check_out', 'number_guest', 'room_accommodation','payment')
    search_fields = ('fullname', 'address')
@admin.register(treasurereservation)
class treasureAdmin(admin.ModelAdmin):
    list_display = ('reservation_number','fullname', 'address', 'cell_number', 'check_in', 'check_out', 'number_guest', 'room_accommodation','payment')
    search_fields = ('fullname', 'address')








@admin.register(HablonOrder)
class hablonorderadmin(admin.ModelAdmin):
    list_display = ('ordernum','firstname','lastname','address','phonenum','dateofdeliver','product1','quantity1','product2','quantity2','product3','quantity3', 'product4','quantity4','product6','quantity6','product7','quantity7','product8','quantity8','product9','quantity9', 'product11','quantity11','product12','quantity12','product13','quantity13','product14','quantity14')
    search_fields = ('ordernum','firstname')


@admin.register(GuilangTortaOrder)
class guilangorderadmin(admin.ModelAdmin):
    list_display = ('ordernum','firstname','middlename','lastname','address','phonenum','dateofdeliver','product1','quantity1','product2','quantity2','product3','quantity3', 'product4','quantity4','product5','quantity5','product6','quantity6','product7','quantity7')
    search_fields = ('ordernum','firstname')

@admin.register(JessieTortaOrder)
class jessieorderadmin(admin.ModelAdmin):
    list_display = ('ordernum','firstname','middlename','lastname','address','phonenum','dateofdeliver','product1','quantity1','product2','quantity2')
    search_fields = ('ordernum','firstname')

@admin.register(OjTortaOrder)
class ojorderadmin(admin.ModelAdmin):
    list_display = ('ordernum','firstname','lastname','address','phonenum','dateofdeliver','product1','quantity1','product2','quantity2','product3','quantity3', 'product4','quantity4','product5','quantity5','product6','quantity6','product7','quantity7','product8','quantity8','product9','quantity9','product10','quantity10', 'product11','quantity11','product12','quantity12','product13','quantity13')
    search_fields = ('ordernum','firstname')

@admin.register(ChitangTortaOrder)
class chitangorderadmin(admin.ModelAdmin):
    list_display = ('ordernum','firstname','lastname','address','phonenum','dateofdeliver','product1','quantity1','product2','quantity2','product3','quantity3', 'product4','quantity4','product5','quantity5','product6','quantity6','product7','quantity7','product8','quantity8','product9','quantity9','product10','quantity10', 'product11','quantity11','product12','quantity12')
    search_fields = ('ordernum','firstname')