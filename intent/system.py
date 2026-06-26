from datetime import datetime


def current_time():
    return f"The current time is {datetime.now().strftime('%I:%M %p')}."


def current_date():
    return f"Today is {datetime.now().strftime('%d %B %Y')}."


def exit_system():
    return "__EXIT__"