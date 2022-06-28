from django.urls import path
from note.views import *


urlpatterns = [
    path('new/', AddNote.as_view(), name="add_note"), 
    path('new/api/', add_note, name="add_note"), 
    path('all/', notes, name="all_notes"), 
    path('api/', notes_api, name="notes_api"), 
    path('list/', NoteListView.as_view(), name="notes_list"), 
    path('<int:id>/', note_details, name="note_details"), 
    path('<int:id>/delete', note_delete), 
    path('<int:id>/edit', note_update, name="note_update"), 
    path('<int:id>/update', note_update_store, name="note_update_store"), 

    # path('save/', save_note), 
]