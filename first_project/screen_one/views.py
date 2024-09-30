from django.shortcuts import render,redirect
from .forms import EmailPasswordForm

class User:
    def __init__(self,name,age,gender,company,image):
        self.image = image
        self.name = name
        self.age = age
        self.gender = gender
        self.company = company


def show_dashboard(request):
    return render(request, "dashboard.html")

def mysql_database(request):
    form = EmailPasswordForm()
    if request.method=="POST":
        form = EmailPasswordForm(request.POST)
        if(form.is_valid):
            form.save()
            return redirect('mysql_database')
            print("Data saved in database")
        else:
            print("Data not saved in database")
    context = {'form':form}
    return render(request, "my_sql_database.html",context)

def show_pass_data(request):

    user = User("Atul",22,"Male","Bascom","https://images.pexels.com/photos/5593326/pexels-photo-5593326.jpeg?auto=compress&cs=tinysrgb&w=600")

    context = {
        'data': 'This is passed data',
        'fruits' : ["Banana","Apple","Watermelon","Pomegranade","Dates","Guvava","Kiwi"],
        'user':user,
    }
    return render(request, "pass_data.html", context)
