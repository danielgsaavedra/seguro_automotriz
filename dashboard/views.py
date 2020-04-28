from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Taller


# Create your views here.

class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'


class SiniestrosView(TemplateView):
    template_name = 'dashboard/siniestros.html'

# class TallerView(TemplateView):
#     template_name = 'dashboard/taller.html'


def TallerView(request):
    taller = Taller.objects.all().order_by('id_taller')
    context = {'taller': taller}
    return render(request, 'dashboard/taller.html', context)

