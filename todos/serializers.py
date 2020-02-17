#Step 40
#We’re specifying which model to use and the specific fields on it we want
#to expose. Remember that id is created automatically by Django so we
#didn’t have to define it in our Todo model but we will use it in our
#detail view.
# todos/serializers.py
from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = Todo
