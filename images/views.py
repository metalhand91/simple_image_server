from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.http import require_GET

from .models import SimpleImage


@require_GET
def get_all(request):
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    
    simple_images = SimpleImage.objects.all()
    
    if limit:
        simple_images = simple_images[int(offset) : int(offset)+int(limit)] 
    count = simple_images.count()
    images_list = []
    
    for image_obj in simple_images:
        images_list.append({
            'id': image_obj.id,
            'url': image_obj.img.url,
            'title': image_obj.title,
            'description': image_obj.description,
        })
    response={
        'data': images_list,
        'meta': {
            'offset': offset,
            'limit': limit,
            'count': count,
        }
    } 
    return JsonResponse(response)


@require_GET
def get_image_url(request):
    image_id = request.GET.get('id')
    image = get_object_or_404(SimpleImage, pk=image_id)
    return HttpResponse(image.img.url)


@require_GET
def get_image_obj(request):
    image_id = request.GET.get('id')
    image_obj = get_object_or_404(SimpleImage, pk=image_id)
    response = {
        'id': image_obj.id,
        'url': image_obj.img.url,
        'title': image_obj.title,
        'description': image_obj.description,
    }
    return JsonResponse(response)


@require_GET
def get_image(request):
    image_id = request.GET.get('id')
    image = get_object_or_404(SimpleImage, pk=image_id)
    return HttpResponseRedirect(image.img.url)
    

