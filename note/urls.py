from django.urls import path
from note.views import *


urlpatterns = [
    path('all/', notes), 
    path('<int:id>/', note_details), 
]