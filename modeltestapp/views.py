from django.shortcuts import render
from modeltestapp.models import Contact

# Create your views here.
def get_contacts(request):
    return render(request, "MT/home.html",
                  {'contact list': Contact.objects.all(),'foo': "Bar"})
