from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from songs.models import Song
from songs.serializers import SongSerializer
from rest_framework import status
from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from .models import Song
from rest_framework.views import APIView
from rest_framework.response import Response

# -------Request---------
# Q1:
def search_song(request, song_name):
    """
    a function that search a song based on its name
    """
    song_info = Song.objects.filter(song_name=song_name)
    serializer = SongSerializer(song_info, many=True)
    return HttpResponse(serializer.data)

def filter_songs_year(request):
    """
    a function that filters all the songs that were released in a given year
    """
    request_data = JSONParser().parse(request)
    song_released_date = request_data.get('released_date', None)
    songs = Song.objects.filter(released_date=date(song_released_date).year)
    serializer = SongSerializer(songs, many=True)
    return HttpResponse(serializer.data)

#  Q2: You can parse the data from the request easier with request.data
def get_all_songs(request):
    """
    a function that gets all songs from db
    """
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return HttpResponse(serializer.data, status=status.HTTP_200_OK)
    
@csrf_exempt
def add_song(request):
    """
    a function that add a parent to db
    """
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        serializer = SongSerializer(data = request_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=status.HTTP_201_CREATED)
        
    
@csrf_exempt
def update_song(request):
    """
    a function that updates a song 
    """
    if request.method == 'PUT':
        request_data = JSONParser().parse(request)
        pk = request_data.get('song_id', None)
        song = get_object_or_404(Song, song_id=pk)
        serializer = SongSerializer(song, data=request_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=status.HTTP_200_OK)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@csrf_exempt
def remove_song(request, song_id):
    """
    a function that removes a song from db
    """
    if request.method == 'DELETE':
        song = get_object_or_404(Song, song_id=song_id)
        song.delete()
        return HttpResponse(status=status.HTTP_200_OK)
    return HttpResponse(status=status.HTTP_404_NOT_FOUND)

# Q3: request.query_params, is like writing request.GET. And we want to
# use it because an Http method type can include other parameters than GET method, and it is more correct.
def get_song(request, song_id):
    """
    a function that gets a song from db based on id
    """
    if request.method == 'GET':
        song_info = get_object_or_404(Song, song_id=song_id)
        serializer = SongSerializer(song_info, many=False)
        return HttpResponse(serializer.data, status=status.HTTP_200_OK)
    return HttpResponse(status=status.HTTP_404_NOT_FOUND)


# -------Responses---------

# Q4:
# Both HttpResponse and Response are used to send http responses to clients, but they are a bit differnt. 
# first, they come from different packages, and HttpResponse, is usually used in web pages and in django core framwork, for rending
# HTML content, and Response() is used for API responsed such as json or xml, and it is found in Django REST framework, for builiding web API's.

# -------Views---------

# Q5: both class-based views and function-based views are views that handle HTTP requests and responses. they are different though in terms
# of structure, functionallity, and organization. Function-based views take request as an argument and return response, they are easy to work with and understand
# for small views. class-based views, are common for behavior of reusing patterns and codelines by providing a built-in generic views, that
# can be updated. 

class SearchSongByName(APIView):
    def get(self, request, song_name):
        song_info = Song.objects.filter(song_name=song_name)
        serializer = SongSerializer(song_info, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ListSongs(APIView):
    def get(self, request):
        """
        a function that gets all songs from db
        """
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return HttpResponse(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request):
        pk = request.data.get('song_id', None)
        try:
            song = Song.objects.get(song_id=pk)
        except Song.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SongSerializer(song, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_song(request):
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def remove_song(request, song_id):
    song = get_object_or_404(Song, song_id=song_id)
    song.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

        

    

# Q6: you can do it with ifs. so for example:
# if request.method == 'GET':
# elif request.method == 'POST':
# this is an example of what you can write in one function to achieve that.

# -------Serializers---------

# Q7: The function save() knows when to save a new object or update it with checking if the primary key of that object 
# is in db or not, if it is the function will update the object, and if not it will add it to db.

# Q8: you can print the serializers' error, incase the validation didn't work, with the attribute error; so serializers.errors

# Q9: this code line, is for when we want to raise an exception if the validation didn't work. it returns a 400 response if the data was invalid.
# A better way of doing it is with a custom field-level validation which can be written like that:
# raise serializers.ValidationError("ERORRRR")
# and we also need to add in serializers.py .validate_<field_name>

# Q10: ANSWER IN SERIALIZERS.PY

# Q11: You can update only one field from db with POST request with partial=True, for example:
# serializer = SongSerializer(song, data={"song_name": "New song name"}, partial=True)

# Q12: depth attribute is related to the relationships between tables in db. so for example if you have a grandpa, father, and son
# and you want to the grandpa to be connected to the father only, then the depth = 1, if you want it to be connected to the child as well
# the depth = 2

# Q13: ANSWER IN SERIALIZERS.PY

# Q14:read-only fields are fields that the user can only get and not update. you use it by adding read_only=True for the field, or if you
# have many field you cana dd a new field in class Meta; read_only_fields =['field_name']

# Q15:  SerializerMethodField is a field that we use when defining a serializer, with it we can include custom fields that are not directly connected
# to model fields.  SerializerMethodField is usually useful when you need to include additional information in validated output.
# an example in serializers.py

# -------Serializer Relations---------

# Q16: SlugRelatedField is a way of targeting a specific field in a relationship. you write it like that:
#   album = serializers.SlugRelatedField(
#       many=True, read_only=True, slug_field='song_name'
#   )
# so when you call album attribute it will look like that: {'album':'song_name','song_name'}
# so when you add data it will not include the album attribute, but only when you retrieve it.
 
# Q17: both select_related and prefetch_related are used access db with minimum queries possible. select_related is used to get data from db 
#  in one single query with foreign key relationships. it is mostly used when we want to include data from table in query without making multiple
# queries to db.
# prefetch_related is used to get data from few db tables mostly in many-to-many and many-to-one relationships. it is a way of organizing queries and reducing
# the number of queries used because there are many tables.
# album = Album.objects.prefetch_related('song_set').all()

# Q18: with the serializer we can get for each user their entire messages. 
# class MessageSerializer(serializers.ModelSerializer):
#   class Meta:
        # model = Message
        # fields = '__all__'
    
# class UserSerializer(serializers.ModelSerializer):
#   messages = MessageSerializer(many=True, read_only=True)
#   class Meta:
        # model = User
        # fields = '__all__'


# Q19: Writable nested serializers are serializers that have a relationship with other serializers. Writable nested serializers are
# read only and if we want to create or update something using the serializer, we need to add create() and update() functions to the serializer.
# there is a project in github that provides us a way of having the serializer know when to create and update objects without us writing the functions
# for that. 
