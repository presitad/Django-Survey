from survey.models import Form,Question,Choice
from survey.serializers import FormSerializer,QuestionSerializer,ChoiceSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from survey.serializers import UserSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action

class FormViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class QuestionViewSet(viewsets.ModelViewSet):
   
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
class ChoiceViewSet(viewsets.ModelViewSet):
   
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    

    


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


