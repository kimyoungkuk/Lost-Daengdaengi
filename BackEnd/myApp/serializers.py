from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class Owner_postSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner_post
        fields = '__all__'

class Dog_shelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog_shelter
        fields = '__all__'

class Finder_postSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finder_post
        fields = '__all__'

class NearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner_post
        fields = ('lat', 'lng',)

class GetImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finder_post
        fields = ('image',)

#class ReportSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Report
#        fields = '__all__'

#class MatchingSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Matching
#        fields = '__all__'
