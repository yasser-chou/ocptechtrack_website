from django.urls import path
from . import views


urlpatterns = [
    path('sign_in_status', views.home, name='status'),
    path('token_details', views.token_details, name='token_details'),
    path('', views.home, name="home"),
    path('Employe', views.all_Employe, name="Employe_list"),
    path('profile', views.all_Tech, name="profile"),
    path('tickets', views.all_tickets, name="list_tickets"),
    path('Ticket_form', views.Ticket_form, name="Ticket_form"),
    path('Employe_form', views.Employee_form, name="Employe_form"),
    path('update_ticket/<int:ticket_id>', views.update_ticket, name='update_ticket'),
    path('Delete_Ticket/<int:ticket_id>', views.Delete_Ticket, name='Delete_Ticket'),
    path('register', views.register_view, name='register'),
    # path('signup', views.signup, name="signup"),
    # path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('ticket/<int:ticket_id>', views.ticket_detail, name='ticket_detail'),
    path('ticket/export/xls/<int:ticket_id>', views.export_ticket_xls, name='export_ticket_xls'),
    path('ticket/download/pdf/<int:ticket_id>', views.download_ticket_as_pdf, name='download_ticket_as_pdf'),
]
