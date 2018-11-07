from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
     """Test api view"""

     def get(self, request, format=None):
         """This returns the data that we want to return"""

         an_apiView = [
            'Uses HTTP methods as functions(ger, port,put,patch,delete).',
            'It is similar to traditional Django view.',
            'Gives you the most control over your logic.',
            'Is mapped manually to Urls.',
         ]


         return Response({'message': 'Hello!', 'an_apiView': an_apiView})
