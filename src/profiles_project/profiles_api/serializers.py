from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """This class serializes the name"""

    name = serializers.CharField(max_length=10)
