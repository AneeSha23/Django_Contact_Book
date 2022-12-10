from django.shortcuts import redirect, render
from .models  import Contacts

# Create your views here.


# --------------------add contact-------------------------------
def savecontact(request):
# formil ninnum varunna datasne oro variablekk assign chyunn
    if request.method == "POST":
        FirstName=request.POST['firstname']
        LastName=request.POST['lastname']
        Email=request.POST['email']
        PhoneNumber=request.POST['phone']
# ippo declare chytha variablesne contactsile modelilekk assign chyunn
        add=Contacts(FirstName=FirstName,LastName=LastName,Email=Email,PhoneNumber=PhoneNumber)
        add.save()

    Data = Contacts.objects.all() 
    return render(request,"index.html",{'Data':Data})
#formil ninnum send chyyunath modelil chenn store aavum.. 
# Enitt athine save chyum... 
# Data enulla variableil ah valuesne kondu varum 
    # return render(request,"index.html")


# --------------------Display contact List-------------------------------

def contactdisplay(request):
    if request.method == "POST":
        FirstName=request.POST['firstname']
        LastName=request.POST['lastname']
        Email=request.POST['email']
        PhoneNumber=request.POST['phone']
        add=Contacts(FirstName=FirstName,LastName=LastName,Email=Email,PhoneNumber=PhoneNumber)
        add.save()
    Data = Contacts.objects.all() 
    return render(request,"list.html",{'Data':Data})

#-----onclick edit button in form it update the values in the database -----------------
def formUpdate(request,id):
    if request.method == 'POST':
        add=Contacts.objects.get(id=id)
        add.FirstName=request.POST['firstname']
        add.LastName=request.POST['lastname']
        add.Email=request.POST['email']
        add.PhoneNumber=request.POST['phone']
        add.save()

        return redirect('contactdisplay')



# --------------------edit contact-------------------------------
def edit(request,id):
    Data=Contacts.objects.get(id=id)
    return render(request,"edit.html",{'Data':Data})



# --------------------delete contact-------------------------------
def deletecontact(request,id):
    add=Contacts.objects.get(id=id)
    add.delete()
    return redirect('contactdisplay')


# -----------------------search----------------------------------------
def search(request):
    query=request.GET['search']
    # xxx_icontains searches the whole xxx field for the argument, case-insensitively.
    Data = Contacts.objects.filter(FirstName__icontains=query)
    return render(request,'search.html',{'Data':Data})