from django.shortcuts import render
def index_home(request):
    return render(request, 'main/home.html')

def index_contacts(request):
    return render(request, 'main/contacts.html')
