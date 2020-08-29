from survey.models import Form
from survey.serializers import FormSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from survey.serializers import UserSerializer
from rest_framework import permissions
from survey.permissions import IsUserOrReadOnly



class FormList(generics.ListCreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

    def perform_create(self, serializer):
        serializer.save(User=self.request.user)
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FormDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsUserOrReadOnly]



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
