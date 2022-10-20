import json
from django.http import JsonResponse
from django.core import serializers

from .models import Movies


def movies_list(request):
    if (request.method == 'GET'):
        movies = list(Movies.objects.all().values())
        return JsonResponse({"data": movies}, status=200)
    if (request.method == 'POST'):
        body = json.loads(request.body)
        movie = Movies(name=body["name"], description=body["description"])
        movie.save()
        return JsonResponse({"data": body}, status=201)


def get_set_movie(request, id):
    if (request.method == 'GET'):
        movie = Movies.objects.get(id=id)
        print(json.loads(movie))
        return JsonResponse({"data": get_serialized_json(movie)}, status=200)
    if (request.method == 'POST'):
        body = json.loads(request.body)
        movie = Movies(name=body["name"], description=body["description"])
        movie.save()
        return JsonResponse({"data": body}, status=201)


def get_serialized_json(obj):
    return json.loads(serializers.serialize("json", [obj]))
