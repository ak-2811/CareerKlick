from django.db import models

class UserRegistration(models.Model):
    full_name = models.CharField(max_length = 50)
    mobile_num = models.IntegerField()
    email_id = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    is_approved=models.BooleanField(default=False)

    
class ListingModel(models.Model):
    #details
    email_id = models.CharField(max_length=50,blank=True, null=True)
    view_count = models.IntegerField(default = 0)
    job_title = models.CharField(max_length=50)
    companys_state = models.TextField(max_length=200)
    experience_level = models.TextField(max_length=50)
    work_model = models.TextField(max_length=50)
    job_type = models.TextField(max_length=50)
    salary = models.IntegerField(default=0)
    image = models.ImageField(upload_to = "images/")
    video=models.FileField(upload_to="video/",default='',null=True,blank=True)
    description = models.TextField(max_length=500)
    companys_country = models.CharField(max_length=50)
    job_industry = models.CharField(max_length=50)
    property_id = models.IntegerField(default=0)
    no_of_openings = models.IntegerField(default=0)
    sponsorship = models.BooleanField(default=False)
    citizenship_required = models.BooleanField(default=False)
    immediate_requirement = models.BooleanField(default=False)
    early_stage = models.BooleanField(default=False)
    growth_stage = models.BooleanField(default=False)
    late_stage = models.BooleanField(default=False)
    public_company = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    

    

Product_Raings = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)

class ProperFeedback(models.Model):
    Property_name = models.ForeignKey("ListingModel", on_delete=models.CASCADE,blank=True, null=True)
    cust_data = models.ForeignKey("UserRegistration", on_delete=models.CASCADE,blank=True, null=True)
    date_time = models.DateTimeField(auto_now=True)
    rating = models.CharField(max_length=20,choices=Product_Raings,default = '1')
    feedback = models.TextField()
    feed_pos = models.FloatField(default=0.0)
    feed_neg = models.FloatField(default=0.0)

    


class OwnerDetails(models.Model):
    Ownername=models.CharField(max_length=30)
    Owneremail=models.EmailField(unique=True)
    Ownerphone=models.PositiveIntegerField()
    Ownerstate=models.CharField(max_length=30)
    password=models.CharField(max_length=10)
    Amount=models.IntegerField(default=1)
    Approved=models.BooleanField(default=False)

    

class Jobs(models.Model):
    user_id=models.ForeignKey(UserRegistration,on_delete=models.CASCADE)
    owner_id=models.ForeignKey(OwnerDetails,on_delete=models.CASCADE,null=True)
    prop_id=models.ForeignKey(ListingModel,on_delete=models.CASCADE)
    document=models.FileField(upload_to='file/')
    boked=models.BooleanField(default=False)
    date=models.DateField(null=True)
    pyment=models.BooleanField(default=False)


class candidatedetails(models.Model):
    user_id=models.CharField(max_length=50,default="")
    owner_id=models.CharField(max_length=50,default="")
    user=models.CharField(max_length=50)
    Owner=models.CharField(max_length=50)
    job_name=models.CharField(max_length=50)
    salary=models.CharField(max_length=50)
    orderDate = models.DateTimeField(auto_created=True,auto_now=True)

    
    