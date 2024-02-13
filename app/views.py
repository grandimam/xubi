import boto3
from django.shortcuts import render
from itertools import groupby
from operator import itemgetter
from datetime import datetime, timedelta
from .forms import CloudCredentialsForm
from .models import CloudCredentials, CloudCostData

def overview(request):
    data = [
        {'provider': 'AWS', 'service': 'EC2', 'cost': 500},
        {'provider': 'GCP', 'service': 'Compute Engine', 'cost': 400},
    ]
    grouped_data = {key: list(group) for key, group in groupby(sorted(data, key=itemgetter('provider')), key=itemgetter('provider'))}
    return render(request, 'app/overview.html', {'grouped_data': grouped_data})

def connectors(request):
    existing_providers = CloudCredentials.objects.all()
    if request.method == 'POST':
        form = CloudCredentialsForm(request.POST)
        if form.is_valid():
            r = form.save()
            return redirect('overview')
    else:
        form = CloudCredentialsForm()
    return render(request, 'app/connectors.html', {'form': form, 'existing_providers': existing_providers})

def fetch_and_store_paginated_cost_data():
    client = boto3.client('ce', region_name='your-aws-region')
    start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')
    granularity = 'MONTHLY'
    next_page_token = None
    while True:
        params = {'TimePeriod': {'Start': start_date, 'End': end_date}, 'Granularity': granularity, 'Metrics': ['BlendedCost']}
        if next_page_token:
            params['NextPageToken'] = next_page_token
        response = client.get_cost_and_usage(**params)
        for result in response['ResultsByTime']:
            timestamp = result['TimePeriod']['Start']
            for group in result['Groups']:
                service = group['Keys'][0]
                usage_type = group['Keys'][1]
                usage_value = group['Metrics']['BlendedCost']['Amount']
                currency = group['Metrics']['BlendedCost']['Unit']
                CloudCostData.objects.create(
                    timestamp=timestamp,
                    service=service,
                    usage_type=usage_type,
                    usage_value=usage_value,
                    currency=currency,
                )
        next_page_token = response.get('NextPageToken')
        if not next_page_token:
            break
