from django.shortcuts import render, redirect
from django.http import HttpResponse
from note.models import Note
from django.views import View

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

class AddNote(View):
	def get(self, request):
		return render(request, 'add_note.html')

	def post(self, request):
		title = request.POST.get("title")
		description = request.POST.get("description")
		note = Note(title=title, description=description)
		note.save()
		return redirect('all_notes')

# def add_note(request):
# 	if request.method == "POST":
# 		title = request.POST.get("title")
# 		description = request.POST.get("description")
# 		note = Note(title=title, description=description)
# 		note.save()
# 		return redirect('all_notes')
# 	else:
# 		return render(request, 'add_note.html')

def notes(request):
	# notes = ["daily works", "schedule", "meetings details"]
	notes = Note.objects.all()
	return render(request, 'notes.html', {"notes": notes})

def note_details(request, id):
	note = Note.objects.get(id=id)
	return render(request, 'note_details.html', {"note": note})