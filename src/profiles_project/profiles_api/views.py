from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from rest_framework import viewsets
# Create your views here.

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

    def list(self, request):
        """This is the get list function test pf a viewset"""

        a_viewset = [
        'This works for list,create,retrieve,update,partial update',
        'Automatically maps to the urls using routers',
        'Provides more functionality with less code'
        ]

        return Response({'message' : 'Hello!', 'a_viewset': a_viewset})
