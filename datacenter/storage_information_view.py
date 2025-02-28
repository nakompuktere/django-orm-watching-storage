from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    # Программируем здесь

    remaining_visitors = Visit.objects.filter(leaved_at=None)

    present_time = localtime()
    entered_at_time = localtime(remaining_visitors[0].entered_at)

    delta =  present_time - entered_at_time
    

    for visit in remaining_visitors:
        visiter = visit.passcard
        print(visiter)


    non_closed_visits = [
        {
            'who_entered': visiter,
            'entered_at': entered_at_time,
            'duration': delta.seconds,
        }
    ]
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
