import django_filters
from django_filters import DateFilter, CharFilter
from django import forms
from .models import Ticket

class DateInput(forms.DateInput):
    input_type = 'date'

class TicketFilter(django_filters.FilterSet):
    full_name = CharFilter(method='filter_full_name', label='Employee Name')
    start_date = DateFilter(field_name='ticket_date', lookup_expr='gte', widget=DateInput(attrs={'type': 'date'}), label='Start Date')
    end_date = DateFilter(field_name='ticket_date', lookup_expr='lte', widget=DateInput(attrs={'type': 'date'}), label='End Date')

    def filter_full_name(self, queryset, name, value):
        return queryset.filter(employe__nom__icontains=value) | queryset.filter(employe__prenom__icontains=value)
    

    class Meta:
        model = Ticket
        fields = ['employe__site']
