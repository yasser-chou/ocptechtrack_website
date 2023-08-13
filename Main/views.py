from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from .models import Employe
from .models import Tech
from .models import Ticket
from .filters import TicketFilter
from .forms import TicketForm
from .forms import EmployeForm
from .forms import TechRegistrationForm
from django.contrib import messages 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .resources import TicketResource
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.conf import settings
from django.urls import reverse
from datetime import datetime
from django.utils import timezone
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet


ms_identity_web = settings.MS_IDENTITY_WEB

def index(request):
    return render(request, "auth/status.html")

@ms_identity_web.login_required
def token_details(request):
    return render(request, 'auth/token.html')

def home(request):
    return render(request,'Main/home.html',{})

def all_Employe(request):
    Employe_list = Employe.objects.all()
    return render(request,'Main/Employe_list.html',
              {'Employe_list' : Employe_list }) 


def all_Tech(request):
    profile = Tech.objects.all()
    return render(request,'Main/profile.html',
                  { 'profile'  : profile } )




def all_tickets(request):
    list_tickets = Ticket.objects.all().order_by('-ticket_date') #show latest tickets first
    myFilter = TicketFilter(request.GET,queryset=list_tickets)
    list_tickets=myFilter.qs
    return render(request, 'Main/ticket_list.html', 
                  {'list_tickets': list_tickets, 'myFilter': myFilter})

    
def Ticket_form(request):
     form=TicketForm()
     if request.method == 'POST':
        form=TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_tickets')
     context={'form':form}
     return render(request, 'Main/Ticket_form.html',context)



def Employee_form(request):
    form = EmployeForm()
    
    if request.method == 'POST':
        form = EmployeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Employe_list')
    
    context = {'form': form}
    return render(request, 'Main/Employe_form.html', context)







from django.utils import timezone

def update_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    form = TicketForm(request.POST or None, instance=ticket)

    if form.is_valid():
        # Get the previous status of the ticket before saving the form
        previous_status = ticket.status

        # Save the form to update the ticket
        ticket = form.save()

        # Check if the status has changed from "in progress" to "completed"
        if previous_status == 'in progress' and ticket.status == 'completed':
            # Set the completion date to the current date and time
            ticket.completed_at = timezone.now()
            ticket.save()

        return redirect('list_tickets')

    return render(request, 'Main/update_ticket.html', {'ticket': ticket, 'form': form})







def Delete_Ticket(request,ticket_id):
    Delete_Ticket = Ticket.objects.get(pk=ticket_id)
    if request.method == "POST" :
        Delete_Ticket.delete() 
        return redirect('list_tickets')
    context={'item':Delete_Ticket}
    return render(request,'Main/Delete_Ticket.html',context)

from django.shortcuts import render, get_object_or_404
from .models import Ticket

def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    technicians = ticket.writed1.all()  
    
    context = {
        'ticket': ticket,

    }
    return render(request, 'Main/ticket_detail.html', context)




def register_view(request):
    if request.method == 'POST':
        form = TechRegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login')  
    else:
        form = TechRegistrationForm()

    return render(request, 'Main/register.html', {'form': form})





# def signup(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         pass1 = request.POST['pass1']
#         pass2 = request.POST['pass2']
        
#         if pass1 != pass2:
#             messages.error(request, "Passwords do not match.")
#             return redirect('signup')

#         # Next, check if the username is unique
#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists.")
#             return redirect('signup')

#         # Next, check if the email is unique
#         if User.objects.filter(email=email).exists():
#             messages.error(request, "Email already exists.")
#             return redirect('signup')

#         # Create the user object with the create_user method
#         technicien = User.objects.create_user(username=username, email=email, password=pass1)
#         technicien.first_name = fname
#         technicien.last_name = lname
#         technicien.save()

#         messages.success(request, "Your account has been successfully created.")
#         return redirect('signin')

#     return render(request, 'Main/signup.html')





# def signin(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         pass1 = request.POST.get('pass1')

#         # Check if both username and password are provided
#         if not username or not pass1:
#             messages.error(request, "Please provide both username and password.")
#             return redirect('signin')

#         user = authenticate(username=username, password=pass1)

#         if user is not None:
#             login(request, user)
#             lname = user.last_name
#             return redirect('list_tickets')
#         else:
#             messages.error(request, "Invalid username or password.")
#             return redirect('signin')  

#     return render(request, 'Main/signin.html')

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully !")
    return redirect('home')








def export_ticket_xls(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    dataset = TicketResource().export([ticket])

    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename="ticket_{ticket_id}.xls"'
    return response





def download_ticket_as_pdf(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)

    # Create a BytesIO buffer to store the PDF data
    buffer = BytesIO()

    # Create a new PDF using the BytesIO buffer
    p = canvas.Canvas(buffer)

    # Set the ticket title as the PDF title
    p.setTitle(f"Ticket: {ticket.title}")

    # Set the filename for the PDF download
    filename = f'ticket_{ticket_id}.pdf'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'

    # Set the completed_date to "Not completed yet" if the ticket is not completed
    completed_date = ticket.completed_at.strftime('%Y-%m-%d %H:%M:%S') if ticket.completed_at else "Not completed yet"

    # Set the ticket_date to a formatted string
    ticket_date = ticket.ticket_date.strftime('%Y-%m-%d %H:%M:%S') if ticket.ticket_date else "Not available"

    # Create a style sheet to format the text
    styles = getSampleStyleSheet()
    header_style = styles['Heading1']

    # Write the ticket title as the header with a larger font
    p.setFont(header_style.fontName, header_style.fontSize + 10)  # Increase the font size by 10
    p.drawString(100, 820, f"Ticket Title: {ticket.title}")

    # Write the ticket ID as a subheader
    p.setFont(header_style.fontName, header_style.fontSize)  # Set the font size back to the default
    p.drawString(100, 790, f"Ticket ID: {ticket_id}")

    # Additional fields
    p.setFont("Helvetica", 12)  # Using "Helvetica" as an example font name and 12 as font size
    p.drawString(100, 760, f"Ticket Date: {ticket_date}")  # Display the formatted ticket_date
    p.drawString(100, 740, f"Employee: {ticket.employe}")
    p.drawString(100, 720, f"Employee Email: {ticket.employe.email_address}")
    p.drawString(100, 700, f"Employee Telephone: {ticket.employe.telephone}")
    p.drawString(100, 680, f"Employee Department: {ticket.employe.department}")
    p.drawString(100, 660, f"Material: {ticket.material}")
    p.drawString(100, 640, f"Description: {ticket.description}")
    p.drawString(100, 620, f"Solution: {ticket.solution}")
    p.drawString(100, 600, f"Status: {ticket.status}")

    if ticket.status == 'completed':
        p.drawString(100, 580, f"Completed Date: {completed_date}")

    # Save the PDF content
    p.save()

    # Get the value of the BytesIO buffer and write it to the response
    pdf_data = buffer.getvalue()
    response.write(pdf_data)

    return response









    



