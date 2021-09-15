def check(var):
    if var.isdigit():
        return int(var)
    else:
        return None


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
