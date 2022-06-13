from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from note.models import Note
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
# def helloworld(request):
# 	return HttpResponse("Hello World!")

# def notes(request):
# 	notes = ["daily works", "schedule", "meetings details"]
# 	html = """
# 	<table border="2">
# 	<tr>
# 	<td>1</td><td>{}</td>
# 	</tr>
# 	<tr>
# 	<td>2</td><td>{}</td>
# 	</tr>
# 	<tr>
# 	<td>3</td><td>{}</td>
# 	</tr>
# 	</table>
# 	""".format(*notes)
# 	print(html)
# 	return HttpResponse(html)

# class AddNote(View):
# 	def get(self, request):
# 		return render(request, 'add_note.html')

# 	def post(self, request):
# 		title = request.POST.get("title")
# 		description = request.POST.get("description")
# 		note = Note(title=title, description=description)
# 		note.save()
# 		return redirect('all_notes')

class AddNote(View):
	def get(self, request):
		form = NoteModelForm()
		return render(request, 'add_note.html', {"form": form})

	def post(self, request):
		# title = request.POST.get("title")
		# description = request.POST.get("description")
		# note = Note(title=title, description=description)
		# note.save()
		form_with_data = NoteModelForm(request.POST)
		if form_with_data.is_valid():
			form_with_data.save()
			return redirect('all_notes')
		else:
			return HttpResponse("while saving data got errors")

# def add_note(request):
# 	if request.method == "POST":
# 		title = request.POST.get("title")
# 		description = request.POST.get("description")
# 		note = Note(title=title, description=description)
# 		note.save()
# 		return redirect('all_notes')
# 	else:
# 		return render(request, 'add_note.html')

@login_required
def notes(request):
	# notes = ["daily works", "schedule", "meetings details"]
	notes = Note.objects.all()
	return render(request, 'notes.html', {"notes": notes})

@login_required
def note_details(request, id):
	# note = Note.objects.get(id=id)
	note = get_object_or_404(Note, id=id)
	return render(request, 'note_details.html', {"note": note})

def note_delete(request, id):
	note = get_object_or_404(Note, id=id)
	note.delete()
	messages.success(request, "deleted successfully...")
	return redirect('all_notes')

@login_required
def note_update(request, id):
	note = get_object_or_404(Note, id=id)
	if request.method == "GET":
		return render(request, 'note_update.html', {"note": note})
	else:
		title = request.POST.get("title")
		description = request.POST.get("description")
		note.title = title
		note.description = description
		note.save()
		messages.success(request, "record updated successfully")
		return redirect('all_notes')
