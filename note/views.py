from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from note.models import Note
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

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

class NoteListView(ListView):
	model = Note
	context_object_name = 'all_notes'
# def add_note(request):
# 	if request.method == "POST":
# 		title = request.POST.get("title")
# 		description = request.POST.get("description")
# 		note = Note(title=title, description=description)
# 		note.save()
# 		return redirect('all_notes')
# 	else:
# 		return render(request, 'add_note.html')

@csrf_exempt
def add_note(request):
	if request.method == "POST":
		title = request.POST.get("title")
		description = request.POST.get("description")
		note = Note(title=title, description=description)
		note.save()
		return JsonResponse({"status": 200})

@login_required
def notes(request):
	# notes = ["daily works", "schedule", "meetings details"]
	notes = Note.objects.all()
	response = render(request, 'notes.html', {"notes": notes})
	response.set_cookie("name", "sai kumar")
	request.session["test_name"] = "testing"
	return response

# @login_required
def notes_api(request):
	# notes = ["daily works", "schedule", "meetings details"]
	notes = Note.objects.all()
	notes_json = serializers.serialize('json', notes)
	return JsonResponse({"status": 200, "notes": notes_json})

@login_required
def note_details(request, id):
	# note = Note.objects.get(id=id)
	note = get_object_or_404(Note, id=id)
	# user_name = request.session["user_name"]
	# name = request.COOKIES
	# print("\n\n\n\n", name)
	# print("\n\n\n\n", user_name)
	# return render(request, 'note_details.html', {"note": note})
	note = serializers.serialize('json', [note])
	return JsonResponse({'note': note})

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

@csrf_exempt
def note_update_store(request, id):
	note = get_object_or_404(Note, id=id)
	import pdb;pdb.set_trace()
	title = request.PUT.get("title")
	description = request.PUT.get("description")
	note.title = title
	note.description = description
	note.save()
	messages.success(request, "record updated successfully")
	return redirect('all_notes')
