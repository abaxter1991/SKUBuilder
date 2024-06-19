from django.shortcuts import render


def integrations(request):
    context = {}

    return render(request, 'integrations/integrations.html', context)


def sync_faire_orders(request):
    pass
