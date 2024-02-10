from django.shortcuts import render
from itertools import groupby
from operator import itemgetter
from .models import CloudProvider, CloudCredentials, CloudCostData

def dashboard(request):
    data = [
        {'provider': 'AWS', 'service': 'EC2', 'cost': 500},
        {'provider': 'AWS', 'service': 'S3', 'cost': 300},
        {'provider': 'GCP', 'service': 'Compute Engine', 'cost': 400},
    ]
    grouped_data = {key: list(group) for key, group in groupby(sorted(data, key=itemgetter('provider')), key=itemgetter('provider'))}
    return render(request, 'explorer/dashboard.html', {'grouped_data': grouped_data})

def connector(request):
    if request.method == 'POST':
        pass
    return render(request, 'explorer/connector.html')
