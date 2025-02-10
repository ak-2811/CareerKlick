from django.contrib import admin
from .models import UserRegistration, ListingModel,OwnerDetails,Jobs,ProperFeedback,candidatedetails

class UserRegestrationAdmin(admin.ModelAdmin):
    list_display=['full_name','email_id']
admin.site.register(UserRegistration,UserRegestrationAdmin)

class CandidatedetailsAdmin(admin.ModelAdmin):
    list_display=['Owner','job_name']
admin.site.register(candidatedetails,CandidatedetailsAdmin)

class ListingModelAdmin(admin.ModelAdmin):
    list_display=['job_title','available']
admin.site.register(ListingModel,ListingModelAdmin)

class OwnerDetailsAdmin(admin.ModelAdmin):
    list_display=['Ownername','Owneremail']
admin.site.register(OwnerDetails,OwnerDetailsAdmin)

class JobsAdmin(admin.ModelAdmin):
    list_display=['date']
admin.site.register(Jobs,JobsAdmin)

class ProperFeedbackAdmin(admin.ModelAdmin):
    list_display=['cust_data','rating']
admin.site.register(ProperFeedback,ProperFeedbackAdmin)

admin.site.site_header = 'Administration Rental'                    # default: "Django Administration"
admin.site.index_title = 'Rental Admin APnel'                 # default: "Site administration"
admin.site.site_title = 'Adminsitration Panel'