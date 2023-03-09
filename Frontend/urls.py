from django.urls import path
from Frontend import views

urlpatterns=[
    path('homepage/', views.homepage, name="homepage"),
    path('categorypage/', views.categorypage, name="categorypage"),
    path('contactpage/',views.contactpage, name="contactpage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('displayproductpage/<itemcatg>',views.displayproductpage,name="displayproductpage"),
    path('productsinglee/<int:dataid>/', views.productsinglee, name="productsinglee"),
    path('cartpage/',views.cartpage,name="cartpage"),
    path('savecartdb/',views.savecartdb,name="savecartdb"),
    path('deletecart/<int:dataid>/',views.deletecart,name="deletecart"),
    path('checkoutt/',views.checkoutt, name="checkoutt"),
    path('webloginpage/', views.webloginpage, name="webloginpage"),
    path('custemerlogin/', views.custemerlogin, name="custemerlogin"),
    path('logout/', views.logout, name="logout"),
    path('custemerlogin/', views.custemerlogin, name="custemerlogin"),
    path('savecustomer/', views.savecustomer, name="savecustomer"),
    path('savecontact/', views.savecontact, name="savecontact"),
    path('savecheckout/', views.savecheckout, name="savecheckout")

]
