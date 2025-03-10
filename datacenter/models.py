from django.db import models
from django.utils.timezone import localtime


def get_duration(remaining_visitors):
    present_time = localtime()
    entered_at_time = localtime(remaining_visitors.entered_at)
    leaved_at_time = localtime(remaining_visitors.leaved_at)
    delta = leaved_at_time - entered_at_time
    return delta.seconds

def format_duration(duration):
    hours = duration // 3600
    minutes = duration // 60 % 60

    return f"{hours}ч {minutes}мин"

def is_visit_long(visit, hour=3600):
    duration_time = get_duration(visit)
    return duration_time > hour


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
