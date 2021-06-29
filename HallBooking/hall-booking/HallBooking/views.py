from django.shortcuts import render,redirect
from HallBooking.forms import Usrg,UpdaPfl,Im,Fil,ChpwdForm,AddHalls,RoleR,RoleUp,UpHls,Booking_Hall,services
from django.contrib.auth.decorators import login_required
from HallBooking.models import User,AdHl,RoleRqst,Booking,Services
from django.contrib import messages
from django.http import HttpResponse
from OnlineHallBooking import settings
from django.core.mail import EmailMessage

# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')


def register(request):
	if request.method == "POST":
		p = Usrg(request.POST)
		if p.is_valid():
			p.save()
			# messages.success(request,"You have successfully registered")
			return redirect('/login')
	p = Usrg()
	return render(request,'html/register.html',{'k':p})


def dashboard(request):
	return render(request,'html/dashboard.html')

@login_required
def prfle(request):
	return render(request,'html/profile.html')

def cgf(request):
	if request.method=="POST":
		print("yes")
		c=ChpwdForm(user=request.user,data=request.POST)
		if c.is_valid():
			c.save()
			return redirect('/login')
	c=ChpwdForm(user=request)
	return render(request,'html/changepwd.html',{'t':c})


def updfple(request):
	if request.method == "POST":
		m = UpdaPfl(request.POST,instance=request.user)
		n = Im(request.POST,request.FILES,instance=request.user)
		if m.is_valid() and n.is_valid():
			m.save()
			n.save()
			messages.success(request,"Profile updated Successfully")
			return redirect('/pfle')
	m = UpdaPfl(instance=request.user)
	n = Im(instance=request.user)
	return render(request,'html/updateprofile.html',{'p':m,'r':n})


@login_required
def hallsview(request):
	l = AdHl.objects.filter(add_id=request.user.id)
	s = AdHl.objects.all()
	return render(request,'html/hallsview.html',{'mn':l,"ss":s})

@login_required
def addhall(request):
	if request.method == "POST":
		k = AddHalls(request.POST,request.FILES)
		if k.is_valid():
			m = k.save(commit=False)
			m.add_id = request.user.id
			m.save()
			messages.success(request,"{} Hall Added Successfully".format(m.name))
			return redirect('/vwhl') 
	k = AddHalls()
	return render(request,'html/adhal.html',{'p':k})

@login_required
def updatehall(request,pk):
	c = AdHl.objects.get(id=pk)
	if request.method == "POST":
		m = UpHls(request.POST,instance=c)
		n = Fil(request.POST,request.FILES,instance=c)
		if m.is_valid():
			m.save()
			n.save()			
			# messages.success(request,"Profile updated Successfully")
			return redirect('/vwhl')
	m = UpHls(instance=c)
	n = Fil(instance=c)
	# n = Im(instance=request.user.updf)
	return render(request,'html/updatehallinfo.html',{'p':m,'r':n})
	

	
@login_required
def deletehall(request,pj):
	s = AdHl.objects.get(id=pj)
	if request.method == "POST":
			s.delete()
			messages.warning(request,"{} Hall Deleted Successfully".format(s.name))
			return redirect('/vwhl')
	return render(request,'html/deletehall.html',{'t':s})

@login_required
def rolereq(request):
	if request.method== "POST":
		k =RoleR(request.POST,request.FILES)
		if k.is_valid():
			s=k.save(commit=False)
			s.uname= request.user.username
			s.uid_id= request.user.id
			s.save()
			return redirect('/dash')
	k=RoleR() 
	return render(request,'html/rolereq.html',{'a':k})


@login_required
def permissions(request):
	ty=User.objects.all()
	a=RoleRqst.objects.all()
	c,rr=[],{}
	for b in a:
		c.append(b.uid_id)
	for j in ty:
		if j.is_superuser==1 or j.id not in c:
			continue
		else: 
			d=RoleRqst.objects.get(uid_id=j.id)
			rr[j.id]=j.username,d.roletype,j.role,j.id
	e=rr.values()
	return render(request,'html/givepermissions.html',{'q':e})



@login_required
def giveper(request,k):
	r=User.objects.get(id=k)
	m=RoleRqst.objects.get(uid_id=k)
	if request.method == "POST":
		k=RoleUp(request.POST,instance=r)
		if k.is_valid():
			k.save()
			m.is_checked=1
			m.save()
			return redirect('/permission')
	k= RoleUp(instance=r)
	return render(request,'html/acceptpermissions.html',{'y':k})


@login_required
def availhalls(request):
	l = AdHl.objects.filter(add_id=request.user.id)
	y = AdHl.objects.all()
	return render(request,'html/availablehalls.html',{'mn':l,'m':y})


def details(request,p):
	q = AdHl.objects.get(id=p)
	print(q.id,q.name,q.status,q.halltype,q.occupancy,q.fil,q.amount)
	return render(request,'html/details.html',{'s':q})

def bookhall(request,f):
	r = AdHl.objects.get(id=f)
	if request.method == "POST":
		k = Booking_Hall(request.POST)
		if k.is_valid():
			m = k.save(commit=False)
			m.contact = r.contact
			m.c_id = request.user.id
			m.hll_id_id = f
			m.hall_status = True
			m.save()
			# messages.success(request," Your Booking request for {}  done Successfully".format(m.name))
			return redirect('/req') 
	k = Booking_Hall(instance=r)
	return render(request,'html/booking.html',{'p':k})
	


def mybookings(request):
	m = Booking.objects.filter(c_id=request.user.id)
	mx = {}
	for j in m:
		mx[j.id]=j.c_id,j.hll_id_id,j.date,j.hall_status
	mv = {}
	t = AdHl.objects.all()
	z = 0
	for n in t:
		for x in mx.values():
			if x[1] == n.id:
				mv[z] = n.id,n.name,n.address,x[2],x[3]
				z +=1
	print(mv)
	return render(request,'html/mybookings.html',{'y':mv.values})


def bookedhalls(request):
	m = Booking.objects.filter(c_id=request.user.id)
	v = User.objects.filter(id=request.user.id)
	my = {}
	for k in v:
		my[k.id]=k.username,k.city
	mx = {}
	for j in m:
		mx[j.id]=j.c_id,j.hll_id_id,j.date,j.hall_status
	mv = {}
	t = AdHl.objects.all()
	z = 0
	for n in t:
		for x in mx.values():
			for p in my.values():
				if x[1] == n.id:
					mv[id] = n.id,n.name,n.address,x[2],x[3],p[0],p[1]
					z +=1
	print(mv)
	return render(request,'html/bookedhalls.html',{'y':mv.values})



	# s={}
	# d=Booking.objects.all()
	# f=AdHl.objects.all()
	# r=User.objects.all()
	# for i in r:
	# 	s[i.id]=i.id,i.username
	# print(s)
	# z=list(s.values())
	# e,o={},{}
	# for h in d:
	# 	for l in f:
	# 		for w in z:
	# 			if h.c_id==w[0]:
	# 				o[h.id]=h.date,w[1],l.name,h.id
	# k=Booking.objects.filter(c_id=request.user.id)
	# m=o.values()
	# print(m)
	# return render(request,'html/bookedhalls.html',{'y':m,'g':k})
	
	
	

@login_required
def deletebooking(request,pj):
	s = Booking.objects.get(id=pj)
	if request.method == "POST":
			s.delete()
			# messages.warning(request,"{} Booking record Deleted Successfully".format(s.name))
			return redirect('/mybook')
	return render(request,'html/deletebooking.html',{'t':s})

@login_required
def bookeddelete(request,uy):
	s = Booking.objects.get(id=uy)
	if request.method == "POST":
			s.delete()
			# messages.warning(request,"{} Booking record Deleted Successfully".format(s.name))
			return redirect('/booked')
	return render(request,'html/bookedhalldelt.html',{'t':s})


	

def hallrequest(request):
	if request.method == "POST":
			return redirect('/pay')
	return render(request,'html/hallrequest.html')

	
def hallpayment(request):
	if request.method=="POST":
		am=request.POST.get('amt')
		a="One of your hall is booked and Your account has been credited with "+am+" Rupees. Update the hall status." 
		t = EmailMessage("Amount",a,settings.EMAIL_HOST_USER,[settings.ADMINS[0][1]])
		t.content_subtype='html'
		t.send()
		if t==1:
			return redirect('/mybook')
		else:
			return redirect('/mybook')
	return render(request,'html/payment.html')


def reciept(request):
	m = Booking.objects.filter(c_id=request.user.id)
	mx = {}
	for j in m:
		mx[j.id]=j.c_id,j.hll_id_id,j.date,j.hall_status
	mv = {}
	t = AdHl.objects.all()
	z = 0
	for n in t:
		for x in mx.values():
			if x[1] == n.id:
				mv[z] = n.id,n.name,n.address,x[2],x[3]
				z +=1
	print(mv)
	return render(request,'html/reciept.html',{'y':mv.values})



	# s={}
	# d=Booking.objects.all()
	# f=AdHl.objects.all()
	# r=User.objects.all()
	# for i in r:
	# 	s[i.id]=i.id,i.username
	# print(s)
	# z=list(s.values())
	# e,o={},{}
	# for h in d:
	# 	for l in f:
	# 		for w in z:
	# 			if h.c_id==w[0]:
	# 				o[h.id]=h.date,w[1],l.name,h.id,l.amount
	# k=Booking.objects.filter(c_id=request.user.id)
	# m=o.values()
	# print(m)
	# return render(request,'html/reciept.html',{'y':m,'g':k})


def service(request):
	return render(request,'html/services.html')


def foodserve(request):
	return render(request,'html/foodservice.html')

def decoration(request):
	return render(request,'html/decorations.html')

def firework(request):
	return render(request,'html/fireworks.html')

def addevtman(request):
	if request.method == "POST":
		k = services(request.POST,request.FILES)
		if k.is_valid():
			m = k.save(commit=False)
			m.add_id = request.user.id
			m.save()
			return redirect('/event') 
	k = services()
	return render(request,'html/addeventman.html',{'p':k})

def eventmanager(request):
	l = Services.objects.filter(e_id=request.user.id)
	s = Services.objects.all()
	return render(request,'html/eventmanagers.html',{'mn':l,"ss":s})
	
def vieweventmanager(request):
	l = Services.objects.filter(e_id=request.user.id)
	y = Services.objects.all()
	return render(request,'html/vieweventman.html',{'mn':l,'m':y})
