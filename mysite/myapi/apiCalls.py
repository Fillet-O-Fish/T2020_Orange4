
from rest_framework import serializers
from .models import user


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = ('name', 'userid', 'creditAccList','depositAccList')
