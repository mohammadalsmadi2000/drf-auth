from rest_framework import serializers
from .models import Thing,Post
class ThingSerializers(serializers.ModelSerializer):
    class Meta:
        model=Thing
        fields=('id','owner','name','desc','created_at')

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('title','desc')