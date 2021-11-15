from django.shortcuts import render

# Create your views here.

def home_page(request):
  return render(request, 'code_snips/home.html')

def user_page(request):
  return render(request, 'code_snips/user_page.html')

def code_view(request):
  return render(request, 'code_snips/code_view.html')