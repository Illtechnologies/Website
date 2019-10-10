from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_3ba8d95e88ea4cccaa095fde191158d5")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "ERROR"
        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol"})

def about(request):
    return render(request, 'about.html', {})

def aticker(request):
    import requests
    import json
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Ticker has successfully been added to list."))
            return redirect('aticker')

    else:
        ticker = Stock.objects.all()
        output = []
        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_3ba8d95e88ea4cccaa095fde191158d5")

            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "ERROR"
        return render(request, 'aticker.html', {'ticker': ticker, 'output': output})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ('Ticker has been successfully deleted.'))
    return redirect('aticker')
