from django.utils.timezone import datetime


def get_profile_image(instance, filename):
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day
    hour = datetime.today().hour
    minute = datetime.today().minute
    second = datetime.today().second
    microsecond = datetime.today().microsecond
    now = f"-d-{year}/{month}/{day}-t-{hour}/{minute}/{minute}/{second}/{microsecond}"
    return 'user/profile/image/{}.jpg'.format(now, filename)


def get_notification_image(instance, filename):
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day
    hour = datetime.today().hour
    minute = datetime.today().minute
    second = datetime.today().second
    microsecond = datetime.today().microsecond
    now = f"-d-{year}/{month}/{day}-t-{hour}/{minute}/{minute}/{second}/{microsecond}"
    return 'user/notification/image/{}.jpg'.format(now)


def log_old_file(instance, filename):
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day
    hour = datetime.today().hour
    minute = datetime.today().minute
    second = datetime.today().second
    microsecond = datetime.today().microsecond
    now = f"-d-{year}/{month}/{day}-t-{hour}/{minute}/{minute}/{second}/{microsecond}"
    return 'log/old/image/{}.jpg'.format(now)


def log_new_file(instance, filename):
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day
    hour = datetime.today().hour
    minute = datetime.today().minute
    second = datetime.today().second
    microsecond = datetime.today().microsecond
    now = f"-d-{year}/{month}/{day}-t-{hour}/{minute}/{minute}/{second}/{microsecond}"
    return 'log/new/image/{}.jpg'.format(now)


def get_branch_image(instance, filename):
    year = datetime.today().year
    month = datetime.today().month
    day = datetime.today().day
    hour = datetime.today().hour
    minute = datetime.today().minute
    second = datetime.today().second
    microsecond = datetime.today().microsecond
    now = f"-d-{year}/{month}/{day}-t-{hour}/{minute}/{minute}/{second}/{microsecond}"
    return 'branch/image/{}.jpg'.format(now)
