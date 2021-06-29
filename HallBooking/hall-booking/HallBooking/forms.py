from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from HallBooking.models import User,AdHl,RoleRqst,Booking,Services
from django.forms import ModelForm

class Usrg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ["username","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Username",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Email id",
			}),
		}

class RoleR(forms.ModelForm):
	class Meta:
		model = RoleRqst
		fields= ["uname","roletype","proof"]
		widgets={
		"uname":forms.TextInput(attrs={"class":"form-control my-2","readonly":True}),
		"roletype":forms.Select(attrs = {"class": "form-control my-2",}),
		"proof":forms.ClearableFileInput(attrs={"class":"form-control"}),

		}

class RoleUp(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","role"]
		widgets={
		"username": forms.TextInput(attrs={"class":"form-control","readonly":True,}),
		"role":forms.Select(attrs={"class":"form-control"}),
		}

class UpdaPfl(ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update First Name"
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update Last Name"
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Update Emailid"
			}),
		}


class Im(ModelForm):
	class Meta:
		model = User
		fields = ["age","gender","dob","im"]
		widgets = {
		"age":forms.NumberInput(attrs={
			"class":"form-control",
			}),
		"gender":forms.Select(attrs={
			"class":"form-control",
			}),
		"dob":forms.DateInput(attrs={
			"class":"form-control",
			"type":"date",
			"placeholder":"Date Of Birth",
			}),
		}

class ChpwdForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Enter Old password"}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Enter New password"}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Confirm your New password"}))
	class Meta:
		model=User
		fields=['oldpassword','newpassword','confirmpassword']


class AddHalls(forms.ModelForm):
	class Meta:
		model = AdHl
		fields = ["name","address","halltype","occupancy"]
		widgets = {
		"name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter name",
			}),
		"address":forms.Textarea(attrs={
			"class":"form-control",
			"placeholder":"Enter address",
			"rows":3,
			"cols":10
			}),
		"halltype":forms.Select(attrs={
			"class":"form-control",
			"placeholder":"Marriage/Seminar/Event",
			}),
		"occupancy":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Occupancy(capacity)",
			})

		}


class UpHls(ModelForm):
	class Meta:
		model = AdHl
		fields = ["name","address","contact","halltype","status","occupancy","rooms","aircond"]
		widgets = {
		"name":forms.TextInput(attrs={
			"class":"form-control",
			"label":"Hall Name",
			"placeholder":"Update Hall Name" 
			}),
		"address":forms.Textarea(attrs={
			"class":"form-control",
			"placeholder":"Update Address",
			"rows":3,
			"cols":10
			}),
		"contact":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Hall Manager Contact",
			}),
		"halltype":forms.Select(attrs={
			"class":"form-control",
			"placeholder":"Marriage/Seminar/Event",
			}),
		"occupancy":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Occupancy(capacity)",
			}),
		"status":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Hall availability",
			}),
		"rooms":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"No.Of Rooms Available",
			}),
		"aircond":forms.Select(attrs={
			"class":"form-control",
			"placeholder":"Ac/Non-AC",
			}),
		
		}


class Fil(ModelForm):
	class Meta:
		model = AdHl
		fields = ["ACHall_Amount","NonACHall_Amount","ACRoom_Cost","NonACRoom_Cost","amount","area","fil"]
		widgets = {
		"ACHall_Amount":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Hall with AC Amount",
			}),
		"NonACHall_Amount":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Hall Without AC Amount",
			}),
		"ACRoom_Cost":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Room With AC Amount",
			}),
		"NonACRoom_Cost":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Room Without AC Amount",
			}),
		"amount":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Amount to be paid",
			}),
		"area":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Area of Hall",
			}),
		}

class Booking_Hall(forms.ModelForm):
	class Meta:
		model=Booking
		fields= ["contact","your_address","rooms_needed","date","timings","occupation","noof_hours"]
		widgets = {
		"contact":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Your Contact number",
			}),
		"your_address":forms.Textarea(attrs={
			"class":"form-control",
			"placeholder":"Enter address",
			"rows":3,
			"cols":10
			}),
		"rooms_needed":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"No.of Rooms Needed",
			}),
		"date":forms.DateInput(attrs={
			"class":"form-control",
			"type":"date",
			"placeholder":"Date You want",
			}),
		"timings":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Timings when hall needed",
			}),
		"occupation":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Your Occupation",
			}),
		"noof_hours":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"No.of Hours",
			})

		}

class services(forms.ModelForm):
	class Meta:
		model=Services
		fields=["eventmanager","managercontact","company"]
		widgets = {
		"eventmanager":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Event Manager Name",
			}),
		"managercontact":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Contact number",
			}),
		"company":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Company Name",
			}),
		}


