from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import Issue

def index(request):
	issue_list = Issue.objects.order_by('created')
	template = loader.get_template('tickets/index.html')
	context = {
		'issue_list': issue_list,
	}
	return HttpResponse(template.render(context, request))

def detail(request, issue_id):
	return HttpResponse("Just one issue, %s." % issue_id)

def enter_time(request, issue_id):
	return HttpResponse("You can enter time for %s." % issue_id)
