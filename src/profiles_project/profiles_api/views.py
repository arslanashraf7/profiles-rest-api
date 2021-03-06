from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from rest_framework import viewsets
# Create your views here.
from . import models
from . import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

class HelloApiView(APIView):
    """Test api view"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
         """This returns the data that we want to return"""

         an_apiView = [
            'Uses HTTP methods as functions(ger, port,put,patch,delete).',
            'It is similar to traditional Django view.',
            'Gives you the most control over your logic.',
            'Is mapped manually to Urls.',
         ]


         return Response({'message': 'Hello!', 'an_apiView': an_apiView})

    def post(self, request):
        """This is a test post function"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Updating the objects"""

        return Response({'methond': 'put'})

    def patch(self, request, pk=None):
        """This is a patch test request"""

        return Response({'method': 'patch'})

    def delete(self, request, pk=None):
        """Delete test request"""

        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test viewset api"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """This is the get list function test pf a viewset"""

        a_viewset = [
        'This works for list,create,retrieve,update,partial update',
        'Automatically maps to the urls using routers',
        'Provides more functionality with less code'
        ]

        return Response({'message' : 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """This is to create new objects in system """

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Used to get an object with Id"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Used to update an Object . Single?"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of an ibject"""

        return Response({'http_method' : "PATCH"})

    def destroy(self, request, pk=None):
        """Handles deletion of an Object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles create,read and updatation of profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns authtoken"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token"""

        return ObtainAuthToken().post(request)

class ProfileFeedViewSet(viewsets.ModelViewSet):
    """This will handle the requests(create,read,update,delete)
     for user profile feed item class"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFieldItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated,)

    def perform_create(self, serializer):
        """Sets the user profilr to the logged in user"""

        serializer.save(user_profile=self.request.user)
