from django.urls import path
from shop import views
urlpatterns = [
    path("", views.base,name='base'),
    path("index/", views.index,name='index'),
    path("aboutus/", views.aboutus,name='aboutus'),
    path("enquiry/", views.enquiry,name='enquiry'),
    path("kids/", views.kids,name='kids'),
    path("mens/", views.mens,name='mens'),
    path("myorder/", views.myorder,name='myorder'),
    path("myprofile/", views.myprofile,name='myprofile'),
    path("product/", views.product,name='product'),
    path("signin/", views.signin,name='signin'),
    path("signup/", views.signup,name='signup'),
    path("womens/", views.womens,name='womens'),
    path("viewproduct/", views.viewproduct,name='viewproduct'),
    path("signout/", views.signout,name='signout'),
    path("myordr/", views.myordr,name='myordr'),
    path("mycart/", views.mycart,name='mycart'),
    path("showcart/", views.showcart,name='showcart'),
    path("cpdetail/", views.cpdetail,name='cpdetail'),
]