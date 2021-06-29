from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver


# Create your models here.

class User(AbstractUser):
	g = [('M','Male'),('F','Female'),('O','Others')]
	gender = models.CharField(max_length=10,choices=g)
	age = models.IntegerField(default=18)
	mobile_no = models.CharField(max_length=10)
	dob = models.DateField(null=True)
	pid_no=models.CharField(max_length=10) 
	address_line1=models.CharField(max_length=200)
	address_line2=models.CharField(max_length=200)
	city=models.CharField(max_length=30)
	state=models.CharField(max_length=30)
	country=models.CharField(max_length=30)
	im = models.ImageField(upload_to="Profile_pics/",default="avatar.png")
	r = [(0,'guest'),(1,'user'),(2,'manager')]
	role = models.IntegerField(choices=r,default=0)

# @receiver(post_save,sender=User)
# def CrtPfle(sender,instance,created,**kwargs):
# 	 if created: 
# 	 	Updf.objects.create(pr=instance)

class RoleRqst(models.Model):
	t=[(1,'user'),(2,'manager')]
	uname= models.CharField(max_length=30)
	roletype = models.PositiveIntegerField(choices=t)
	proof = models.ImageField(blank=True)
	is_checked=models.BooleanField(default=0)
	uid= models.OneToOneField(User,on_delete=models.CASCADE)

class AdHl(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=70)
	contact = models.IntegerField(default="0000000000")
	landmark = models.CharField(max_length=50)
	h = [('Marriage','Marriage'),('Seminar','Seminar'),('Event','Event')]
	halltype = models.CharField(choices=h,max_length=10,default="Event")
	a = [('AC','Ac'),('Non-AC','Non-AC')]
	aircond = models.CharField(choices=a,max_length=10,default="Non-AC")
	ACHall_Amount = models.CharField(max_length=30,default="25000 per hour")
	NonACHall_Amount = models.CharField(max_length=30,default="20000 per hour")
	occupancy = models.IntegerField(null=True)
	rooms = models.IntegerField(default=0)
	ACRoom_Cost = models.CharField(max_length=30,default="5000 per hour")
	NonACRoom_Cost = models.CharField(max_length=30,default="3000 per hour")
	area = models.CharField(max_length=20)
	amount = models.IntegerField(default=300)
	status = models.CharField(max_length=50,default="Available")
	fil = models.ImageField(upload_to="Hall_Images/")
	add = models.ForeignKey(User,on_delete=models.CASCADE)


class Booking(models.Model):
	contact = models.IntegerField()
	your_address = models.CharField(max_length=70)
	occupation = models.CharField(max_length=30)
	rooms_needed = models.IntegerField(default=2)
	date = models.DateField(null=True)
	timings = models.CharField(max_length=30,default="AM to PM")
	noof_hours = models.IntegerField(default=3)
	hall_status = models.BooleanField(default=False)
	hll_id = models.ForeignKey(AdHl,on_delete=models.CASCADE)
	c = models.ForeignKey(User,on_delete=models.CASCADE)


class Services(models.Model):
	eventmanager = models.CharField(max_length=20)
	managercontact = models.IntegerField()
	company = models.CharField(max_length=50)
	e = models.ForeignKey(User,on_delete=models.CASCADE)
	


	
	
	





