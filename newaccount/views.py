from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import newUser
from django.views.generic import TemplateView,UpdateView
# Create your views here.

def index(request):
    return HttpResponse('hi')


class AddcustomerView(TemplateView):
    template_name = 'index.html'
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        userID = request.POST['userID']
        userFirstName = request.POST['userFirstName']
        userLastName = request.POST['userLastName']
        userAge = request.POST['userAge']
        userGender = request.POST['userGender']
        userDistrict = request.POST['userDistrict']
        userState = request.POST['userState']
        userNationality = request.POST['userNationality']
        userAadhaar = request.POST['userAadhaar']
        userEmail = request.POST['userEmail']
        userContact = request.POST['userContact']
        userImage = request.FILES['userImage']
        newCustomer = newUser(
            userID=userID,
            userFirstName=userFirstName,
            userLastName=userLastName,
            userAge=userAge,
            userGender=userGender,
            userDistrict=userDistrict,
            userState=userState,
            userNationality=userNationality,
            userAadhaar=userAadhaar,
            userEmail=userEmail,
            userContact=userContact,
            userImage=userImage
        )
        newCustomer.save()
        return render(request,self.template_name)
    

class ListcustomerView(TemplateView):
    template_name = 'list.html'
    def get(self,request):
        context = {
            'newUsers': newUser.objects.all()
        }
        return render(request, self.template_name,context=context)

class DeletecustomerView(TemplateView):
    def get(self,request,pk):
        to_delete = newUser.objects.get(pk=pk)
        to_delete.delete()
        return redirect('list-customer')


class UpdatecustomerView(TemplateView):
    template_name = 'update.html'
    def get(self,request,pk):
        to_update = newUser.objects.get(pk=pk)
        context = {
            'newUser': to_update
        }
        return render(request,self.template_name,context)
    def post(self,request,pk):

        userID = request.POST['userID']
        userFirstName = request.POST['userFirstName']
        userLastName = request.POST['userLastName']
        userAge = request.POST['userAge']
        userGender = request.POST['userGender']
        userDistrict = request.POST['userDistrict']
        userState = request.POST['userState']
        userNationality = request.POST['userNationality']
        userAadhaar = request.POST['userAadhaar']
        userEmail = request.POST['userEmail']
        userContact = request.POST['userContact']

        to_update = newUser.objects.get(pk=pk)
        to_update.userID = userID
        to_update.userFirstName = userFirstName
        to_update.userLastName = userLastName
        to_update.userAge = userAge
        to_update.userGender = userGender
        to_update.userDistrict = userDistrict
        to_update.userState = userState
        to_update.userNationality = userNationality
        to_update.userAadhaar = userAadhaar
        to_update.userEmail = userEmail
        to_update.userContact = userContact


        if 'userImage' in request.FILES:
            to_update.userImage = request.FILES['userImage']
        else:
            pass
        to_update.save()
        return redirect('list-customer')