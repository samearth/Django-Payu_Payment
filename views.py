from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Import Payu from Paywix
from paywix.payu import Payu
from core import models

payu_config = settings.PAYU_CONFIG
merchant_key = payu_config.get('merchant_key')
merchant_salt = payu_config.get('merchant_salt')
surl = payu_config.get('success_url')
furl = payu_config.get('failure_url')
mode = payu_config.get('mode')

# Create Payu Object for making transaction
# The given arguments are mandatory
payu = Payu(merchant_key, merchant_salt, surl, furl, mode)


# Payu checkout page
def home(request):
    return render(request , 'home.html')

@csrf_exempt
def paydem(request):
        # Making Checkout form into dictionary
        # The dictionary data  should be contains following details
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        data = { 'amount': '10', 
            'firstname': firstname, 
            'email': email,
            'phone': phone, 'productinfo': 'test', 
            'lastname': 'test', 'address1': 'test', 
            'address2': 'test', 'city': 'test', 
            'state': 'test', 'country': 'test', 
            'zipcode': 'tes', 'udf1': '', 
            'udf2': '', 'udf3': '', 'udf4': '', 'udf5': ''
        }
        # No TransactioN ID's, Create new with paywix, it's not mandatory
        # Create your own
        # Create transaction Id with payu and verify with table it's not existed
        txnid = payu.generate_txnid()
        data.update({"txnid": txnid})
        payu_data = payu.transaction(**data)
        return render(request, 'paydem.html', {"posted": payu_data})
    else:
        return render(request , 'paydem.html')


@csrf_exempt
def success(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_transaction(data)
    return JsonResponse(response)

@csrf_exempt
def failure(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    response = payu.verify_transaction(data)
    return JsonResponse(response)