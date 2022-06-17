from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_ticket(request):

    """ Create Ticket View """

    context = {}

    return render(request, 'tickets/create_ticket_form.html', context)