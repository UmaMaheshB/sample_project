from django.urls import path
from note.views import *


urlpatterns = [
    path('new/', AddNote.as_view()), 
    path('all/', notes, name="all_notes"), 
    path('<int:id>/', note_details), 
    path('<int:id>/delete', note_delete), 
    path('<int:id>/edit', note_update), 

    # path('save/', save_note), 
]