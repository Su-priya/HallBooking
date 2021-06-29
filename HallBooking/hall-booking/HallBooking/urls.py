from django.urls import path
from HallBooking import views
from django.contrib.auth import views as v

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="cn"),
	path('reg/',views.register,name="rg"),
	path('ch/',views.cgf,name="cg"),
	path('dash/',views.dashboard,name="dsh"),
	
	path('login/',v.LoginView.as_view(template_name="html/login.html"),name="lg"),
	path('logout/',v.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
	
	path('pfle/',views.prfle,name="pf"),
	path('updf/',views.updfple,name="upf"),
	
	path('vwhl/',views.hallsview,name="hlv"),
	path('adhl/',views.addhall,name="adh"),
	path('avhl/',views.availhalls,name="avh"),
	path('updhl/<int:pk>/',views.updatehall,name="uphl"),
	path('dlt/<int:pj>/',views.deletehall,name="delt"),
    
    path('rolerq/',views.rolereq,name="rr"),
    path('permission/',views.permissions,name="per"),
    path('gvp/<int:k>/',views.giveper,name="gvpr"),

    path('bkhl/<int:f>/',views.bookhall,name="bkh"),
    path('det/<int:p>/',views.details,name="detail"),
    path('req/',views.hallrequest,name="request"),
    path('mybook/',views.mybookings,name="mybookings"),
    path('dltb/<int:pj>/',views.deletebooking,name="deltb"),
    path('dtbd/<int:uy>/',views.bookeddelete,name="dtbkd"),
    path('booked/',views.bookedhalls,name="bookedhalls"),

    path('pay/',views.hallpayment,name="payment"),
    path('recpt/',views.reciept,name="rct"),


    path('ser/',views.service,name="srvc"),
    path('foods/',views.foodserve,name="food"),
    path('deco/',views.decoration,name="decor"),
    path('fire/',views.firework,name="firwor"),
    path('adevnt/',views.addevtman,name="addeve"),
    path('event/',views.eventmanager,name="eventman"),
    path('viewevent/',views.vieweventmanager,name="vieweventman"),

] 