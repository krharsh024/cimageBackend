from django.urls import path,include
from . import views

urlpatterns = [
    path("signup/",views.userSignup.as_view()),
    path("membershipDetails/<email>",views.userMembership.as_view())
]