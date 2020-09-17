from .models import Form,Question,Choice
from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerializer(serializers.HyperlinkedModelSerializer):
    # form = serializers.HyperlinkedRelatedField(many=True, view_name='form-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username']

class FormSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Form
        fields = ['url', 'id', 'pub_date', 'title', 'user']
    
class QuestionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Question
        fields = ['url', 'id', 'form', 'question_text',]

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Choice
        fields = ['url', 'id', 'question', 'choice_text', 'votes','user']
    
    
