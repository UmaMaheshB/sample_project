from django.shortcuts import render
from django.http import HttpResponse
from note.models import Note

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

def notes(request):
	# notes = ["daily works", "schedule", "meetings details"]
	notes = Note.objects.all()
	return render(request, 'notes.html', {"notes": notes})

def note_details(request, id):
	notes = ["daily works", "schedule", "meetings details"]
	return HttpResponse(notes[id])