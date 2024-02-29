import boto3
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from itertools import groupby
from operator import itemgetter
from datetime import datetime, timedelta
from .forms import CloudCredentialsForm, SearchForm
from .models import CloudCredentials, CloudCostData

def overview(request):
    data = CloudCostData.objects.all()
    return render(request, 'app/overview.html', {'grouped_data': data})

def get_cloud_cost_data(request):
    labels = ['Label 1', 'Label 2', 'Label 3']
    values = [100, 200, 150]
    data = {
            'labels': labels,
            'values': values,
    }
    return JsonResponse(data)

def search_providers(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid(): 
            return render(request, )
    else:
        form = SearchForm(request.POST)

def create_connector(request):
    if request.method == 'POST':
        form = CloudCredentialsForm(request.POST)
        connector_id_to_delete = request.POST.get('connector_id_to_delete')
        if connector_id_to_delete:
            return delete_connector(request, connector_id_to_delete)
        elif form.is_valid():
            form.save()
        return redirect('connectors')
    else:
        form = CloudCredentialsForm()
        existing_providers = CloudCredentials.objects.all()
        return render(request, 'app/connectors.html', {'form': form, 'existing_connectors': existing_providers})

def delete_connector(request, connector_id):
    connector = get_object_or_404(CloudCredentials, pk=connector_id)
    connector.delete()
    return redirect("connectors")

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
