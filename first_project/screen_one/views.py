from django.shortcuts import render

def show_text(request):    # functional views
  context = {
    'text': 'Hello World',
    'fruits' : ['Apple','Banana','Cherry','Mango','Dragon Fruit']
  }

  return render(request,"show_text.html",context)
