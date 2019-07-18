from django.shortcuts import render, redirect
import random, pytz
from datetime import datetime
from time import strftime

# Create your views here.
def index(request):
    if 'activities' not in request.session:
        request.session['activities'] = []
    if 'gold' not in request.session:
        request.session['gold'] = 0
    
    context = {
        'activities': request.session['activities'],
        'gold': request.session['gold']
    }
    return render(request, 'ninjaGold_app/index.html', context)


def process_money(request):
    chi = pytz.timezone('US/Central')
    real_time = datetime.now(chi)

    if request.method == 'POST':
        if request.POST['building'] == "farm":
            winnings = random.randrange(10, 21)
            request.session['gold'] += winnings
            activity = f"<p style='color:green'>Earned {winnings} from {request.POST['building']} at {real_time.strftime('%Y %a %b %d %I:%M %p %Z')}</p>"
            request.session['activities'].insert(0, activity)
            

        elif request.POST['building'] == "cave":
            winnings = random.randrange(5, 11)
            request.session['gold'] += winnings
            activity = f"<p style='color:green'>Earned {winnings} from {request.POST['building']} at {real_time.strftime('%Y %a %b %d %I:%M %p %Z')}</p>"
            request.session['activities'].insert(0, activity)

        elif request.POST['building'] == "house":
            winnings = random.randrange(2, 6)
            request.session['gold'] += winnings
            activity = f"<p style='color:green'>Earned {winnings} from {request.POST['building']} at {real_time.strftime('%Y %a %b %d %I:%M %p %Z')}</p>"
            request.session['activities'].insert(0, activity)

        else:
            winnings = random.randrange(-50, 51)
            request.session['gold'] += winnings
            if winnings < 0:
                activity = f"<p style='color:red'>Earned {winnings} from {request.POST['building']} at {real_time.strftime('%Y %a %b %d %I:%M %p %Z')}</p>"
            else:
                activity = f"<p style='color:green'>Earned {winnings} from {request.POST['building']} at {real_time.strftime('%Y %a %b %d %I:%M %p %Z')}</p>"
            
            request.session['activities'].insert(0, activity)
    return redirect('/')

def reload(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return redirect('/')