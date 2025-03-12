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