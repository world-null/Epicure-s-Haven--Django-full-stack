from django.shortcuts import render
from django.http import HttpResponse
from Base_App.models import ItemList, Items, AboutUs, Feedback, BookTable

# Create your views here.
def Homeview(request):
    items=Items.objects.all()
    list=ItemList.objects.all()
    review=Feedback.objects.all()
    return render(request, 'home.html', {'items':items, 'list':list, 'review': review} )

def Aboutview(request):
    data=AboutUs.objects.all()
    return render(request, 'about.html', {'data': data})

def Menuview(request):
    items=Items.objects.all()
    list=ItemList.objects.all()
    return render(request, 'menu.html', {'items':items, 'list':list} )

def BookTableview(request):
    if request.method=='POST':
        name=request.POST.get('user_name')
        phone_number=request.POST.get('user_number')
        email=request.POST.get('user_email')
        total_person=request.POST.get('total_person')
        booking_date=request.POST.get('booking_date')

        if name != '' and phone_number != '' and email != '' and total_person != '' and booking_date != '':
            data= BookTable(Name=name, Phone_Number=phone_number, Email=email, Total_Person=total_person, Booking_Date=booking_date)
            data.save()
    return render(request, 'booktable.html')

def Feedbackview(request):
    return HttpResponse("Hii! This is my Feedback Page")

