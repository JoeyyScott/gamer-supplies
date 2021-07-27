from django.shortcuts import render, redirect

# Create your views here.


def view_crate(request):
    """ Crate page view """

    return render(request, 'crate/crate.html')


def add_to_crate(request, item_id):
    """ Add a quantity of the specified supply to the shopping crate """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    crate = request.session.get('crate', {})

    if item_id in list(crate.keys()):
        crate[item_id] += quantity
    else:
        crate[item_id] = quantity

    request.session['crate'] = crate
    return redirect(redirect_url)
