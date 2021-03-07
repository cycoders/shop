from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['fname', 'lname', 'image', 'biography', 'age', 'email', 'phone', 'address', 'postcode']
