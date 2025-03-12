from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.working_with_duration import format_duration


def storage_information_view(request):
    # Программируем здесь

    remaining_visitors = Visit.objects.filter(leaved_at=None)

    present_time = localtime()
    
    non_closed_visits = []

    for visit in remaining_visitors:
        visiter = visit.passcard
        b = localtime(visit.entered_at)


        delta =  present_time - b
        print(visiter)


        non_closed_visits.append({

                'who_entered': visiter,
                'entered_at': visit.entered_at,
                'duration': format_duration(delta.seconds),
            })
            
        

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
