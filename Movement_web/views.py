from django.http import FileResponse

from events.models import Photo


def return_media(request, filename):
    if Photo.objects.get(image=f'{filename}'):
        return FileResponse(Photo.objects.get(image=f'{filename}').image)