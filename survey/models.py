from django.db import models
from django.contrib.auth.models import User
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from rest_framework import serializers

class Form(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        if self.title:
            return self.title


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)

    def __str__(self):
        if self.question_text:
            return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class UserSerializer(serializers.ModelSerializer):
    form = serializers.PrimaryKeyRelatedField(many=True, queryset=Form.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'form']