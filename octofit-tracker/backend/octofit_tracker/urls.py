
import os
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'leaderboard', views.LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')


# API root endpoint that returns the full API URL using $CODESPACE_NAME
@csrf_exempt
def api_root_url(request):
    codespace_name = os.environ.get('CODESPACE_NAME', None)
    if codespace_name:
        api_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    else:
        # fallback for localhost
        api_url = "http://localhost:8000/api/"
    return JsonResponse({"api_url": api_url})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root_url, name='api-root'),
    path('api/', include(router.urls)),
]
