from import_export import resources
from .models import Ticket, Employe

class TicketResource(resources.ModelResource):
    employee_nom = resources.Field(attribute='employe__nom', column_name='Last Name')
    employee_prenom = resources.Field(attribute='employe__prenom', column_name='First Name')
    employee_email = resources.Field(attribute='employe__email_address', column_name='Email Address')
    employee_telephone = resources.Field(attribute='employe__telephone', column_name='Telephone')
    employee_department = resources.Field(attribute='employe__department', column_name='Department')

    class Meta:
        model = Ticket
        fields = ('id', 'title', 'ticket_date', 'employee_nom', 'employee_prenom', 'employee_email', 'employee_telephone', 'employee_department', 'material', 'description', 'solution', 'status', 'completed_at')

    def dehydrate_completed_at(self, ticket):
        return ticket.completed_at.strftime('%Y-%m-%d %H:%M:%S') if ticket.completed_at and ticket.status == 'completed' else ""
