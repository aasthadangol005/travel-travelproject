from django.views.generic import *


class HomeView(TemplateView):
	template_name='travelapp/home.html'