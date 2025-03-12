from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datacenter.working_with_duration import get_duration, is_visit_long, format_duration


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    all_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []

    for visit in all_visits:
        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visit_long(visit)
        })

        
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
