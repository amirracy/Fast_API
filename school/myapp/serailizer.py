from rest_framework import serializers
from .models import *


class StudentSerailizer(serializers.ModelSerializer):
    class  Meta:
        model=SchoolData
        fields="__all__"
        