from django.shortcuts import render

def show_dashboard(request):
    return render(request, "dashboard.html")

def show_pass_data(request):
    context = {
        'data': 'This is passed data'
    }
    return render(request, "pass_data.html", context)
