from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import RequestContext
from .models import newUser
from django.views.generic import TemplateView,UpdateView
# Create your views here.

def index(request):
    return render(request, "main.html")

class AddcustomerView(TemplateView):
    template_name = 'add.html'
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
        userAadhaarImage = request.FILES['userAadhaarImage']
        userStartingBalance = request.POST['userStartingBalance']
        userRemarks = request.POST['userRemarks']


        if 'tccheck' in request.POST:
            tc = request.POST['tccheck']
        else:
            tc = False


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
            userImage=userImage,
            userAadhaarImage=userAadhaarImage,
            userStartingBalance=userStartingBalance,
            userRemarks=userRemarks,
            tc=tc
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
        userStartingBalance = request.POST['userStartingBalance']
        userRemarks = request.POST['userRemarks']

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
        to_update.userStartingBalance = userStartingBalance
        to_update.userRemarks = userRemarks



        if 'userImage' in request.FILES:
            to_update.userImage = request.FILES['userImage']
        else:
            pass
        to_update.save()


        if 'userAadhaarImage' in request.FILES:
            to_update.userAadhaarImage = request.FILES['userAadhaarImage']
        else:
            pass
        to_update.save()

        if 'tccheck' in request.POST:
            to_update.tc = True
        else:
            to_update.tc = False
        return redirect('list-customer')