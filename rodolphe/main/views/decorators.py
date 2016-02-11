from django.shortcuts import render_to_response
from django.conf import settings
from functools import wraps


def lock_view(request, *args, **kwargs):
    return render_to_response('auth.html', {})

def vospapiers(f):
    @wraps(f)
    def petit_wrap(request, *args, **kwargs):
        if settings.PASSWORD:
            if settings.PASSWORD in request.get_raw_uri():
                request.session["allowed"] = True
            if not request.session.get("allowed", False):
                return lock_view(request, *args, **kwargs)
        return f(request, *args, **kwargs)

    return petit_wrap
