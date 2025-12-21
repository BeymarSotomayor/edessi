from .models import Company

def company_data(request):
    company = Company.objects.first()  # o get(pk=1) si tienes una sola
    return {
        'company': company
    }
