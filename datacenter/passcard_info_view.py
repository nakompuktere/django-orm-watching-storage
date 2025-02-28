from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404

def get_duration(remaining_visitors):
    present_time = localtime()
    entered_at_time = localtime(remaining_visitors.entered_at)
    leaved_at_time = localtime(remaining_visitors.leaved_at)
    delta = leaved_at_time - entered_at_time
    return delta.seconds

def is_visit_long(visit):
    duration_time = get_duration(visit)
    if duration_time > 3600:
        return True
    else:
        return False

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    all_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in all_visits:
        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': get_duration(visit),
            'is_strange': is_visit_long(visit)
        })

        
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
