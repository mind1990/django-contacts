from django.shortcuts import render

# Import Contact Model
from .models import Contact

def contacts_index(request):
	contacts = Contact.objects.all()
	return render(request, 'contacts/contacts_index.html', {'contacts': contacts})

def contacts_show(request, contact_id):
	contact = Contact.objects.get(id=contact_id)
	return render(request, 'contacts/contacts_show.html', {'contact': contact})
