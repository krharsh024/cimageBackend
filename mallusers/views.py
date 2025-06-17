from rest_framework.views import APIView
from .serializers import *
from .models import *
from django.http import JsonResponse
# Create your views here.

class userSignup(APIView):
    def post(self,request):
        serializerData=userDetailsSerializer(data=request.data)
        if serializerData.is_valid():
            userDetails.objects.create(**serializerData.data)
            message={"message":"User signup successfully"}
            return JsonResponse(message)
        return JsonResponse(serializerData.errors)
    

class userMembership(APIView):
    def get(self,request,email):
        result=list(membershipDetails.objects.filter(email=email).values())
        message={"Membership details":result}
        return JsonResponse(message,safe=False)