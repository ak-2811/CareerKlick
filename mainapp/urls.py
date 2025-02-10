from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginUserView, name='login'),
    path('register/', RegisterUSerView, name='register'),
    path('add-list/', Add_Listing, name='addlist'),
    path('owner-add-list/', owner_Add_Listing, name='owneraddlist'),
    path('Update_Owner_Job/<int:id>/',Update_Owner_Property,name='Update_Owner_Property'),
    path('all-list/', AllListView, name='alllist'),
    path('profile/<int:id>/', ProfileView, name='profile'),
    path('OwnerProfileView/<int:id>/',OwnerProfileView,name='OwnerProfileView'),
    path('', UserIndexPage, name='UserIndexPage'),
    path('OwnerIndexView/', OwnerIndexView, name='OwnerIndexView'),
    path('MyOpenings/',MyPropertyView,name='myproperty'),
    path('OwnerAllListView/',OwnerAllListView,name='OwnerAllListView'),
    path('Owner_MyOpenings/',Owner_myproperty,name='Owner_myproperty'),
    path('deleteproperty/<int:id>/',deleteproperty,name='deleteproperty'),
    path('logout/',logout,name='logout'),
    path('UserBooks/',UserBooks,name='UserBooks'),
    path('viewBooks/<int:id>',viewBooks,name='viewBooks'),
    path('Owner_logout/',Owner_logout,name='Owner_logout'),
    path('ownerlogin/',ownerlogin,name='ownerlogin'),
    path('main_data',main,name='main'),
    path('Acceptancehandler/', paymenthandler, name='paymenthandler'),
    path('propbooking/<int:id>/',prop_booking,name='propbooking'),
    path('alldata/',alldata,name='alldata'),
    path('edit/<int:id>/',edit),
    path('update/<int:id>/',update),
    path('ownersignup/',ownersignup,name="ownersignup"),
    path('userbuy/',userbuy,name='userbuy'),
    path('getdetails/<int:id>/',getdetails,name='getdetails'),
    path('ownerbookpymentdetails/',ownerordertable,name='ownerordertable')
  
]
