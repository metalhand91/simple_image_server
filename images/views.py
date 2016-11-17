from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET

from .models import SimpleImage


@require_GET
def get_all(request):
    all_images = SimpleImage.objects.all()
    images_list = []
    for image in all_images:
        images_list.append({image.id: image.img.url})
    response={'data': images_list}
    return JsonResponse(response)


@require_GET
def get_image(request, image_id):
    image = get_object_or_404(SimpleImage, pk=image_id)
    return HttpResponse(image.img.url)
    

