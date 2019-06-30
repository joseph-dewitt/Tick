from django.shortcuts import render

from django.http import Http404
from django.template import loader
from .models import Issue

def index(request):
	issue_list = Issue.objects.order_by('created')
	context = {
		'issue_list': issue_list,
	}
	return render(request, 'tickets/index.html', context)

def detail(request, issue_id):
	try:
		issue = Issue.objects.get(pk=issue_id)
	except Issue.DoesNotExist:
		raise Http404("This issue does not exist")
	return render(request, 'tickets/detail.html', {'issue': issue})

def enter_time(request, issue_id):
	return HttpResponse("You can enter time for %s." % issue_id)
