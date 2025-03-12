from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.work_with_duration import format_duration


def storage_information_view(request):
    # Программируем здесь

    remaining_visitors = Visit.objects.filter(leaved_at=None)

    present_time = localtime()
    non_closed_visits = []

    for visit in remaining_visitors:
        visitor_passcard = visit.passcard

        residence_time =  present_time - localtime(visit.entered_at)

        non_closed_visits.append({

                'who_entered': visitor_passcard,
                'entered_at': visit.entered_at,
                'duration': format_duration(residence_time.seconds),
            })
            
        

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
