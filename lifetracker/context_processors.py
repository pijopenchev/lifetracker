from django.conf import settings


def populate_username(request):
    user = request.user
    if user:
        return {'lt_username': user.username}
    else:
        return {'lt_username':''}
