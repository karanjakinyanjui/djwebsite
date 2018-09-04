from .models import Contact

contacts = Contact.objects.get(id=1)


def contact(request):
    return {'contact': contacts}