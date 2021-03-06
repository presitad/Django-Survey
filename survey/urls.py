
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from survey import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'form', views.FormViewSet)
router.register(r'question', views.QuestionViewSet)
router.register(r'choice', views.ChoiceViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

