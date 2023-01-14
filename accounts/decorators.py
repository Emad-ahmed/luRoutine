from django.http import Http404


def role_required(permission=[]):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            for pers in permission:
                if pers == 'admin' and (request.user.bind_account.role == 'admin' or request.user.is_staff):
                    return view_func(request, *args, **kwargs)
                else:
                    raise Http404

        return wrap

    return decorator
