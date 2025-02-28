from datacenter.models import Passcard
from django.shortcuts import render


def active_passcards_view(request):
    # Программируем здесь
      
    active_passcardss = Passcard.objects.filter(is_active=True)

    context = {
        'active_passcards': active_passcardss,  # люди с активными пропусками
    }
    return render(request, 'active_passcards.html', context)
