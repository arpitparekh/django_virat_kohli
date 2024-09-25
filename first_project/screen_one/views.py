from django.shortcuts import render

def show_text(request):    # functional views
  context = {
    'text': 'Hello World',
  }
  return render(request,"show_text.html",context)
