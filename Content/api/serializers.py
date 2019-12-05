from ..models import Content
from rest_framework import serializers

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('attraction_name', 'description', 'is_landmark') # if not declared, all fields of the model will be shown
        