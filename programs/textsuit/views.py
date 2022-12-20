from django.shortcuts import render, redirect
from .models import Pablic
from .forms import PablicForm
from django.views.generic import DetailView, UpdateView, DeleteView


def textsuit_home(request):
    news = Pablic.objects.order_by('-date')[:3]
    return render(request, 'textsuit/textsuit_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Pablic
    template_name = 'textsuit/details_view.html'
    context_object_name = 'pablic'


class NewsUpdateView(UpdateView):
    model = Pablic
    template_name = 'textsuit/create.html'
    form_class = PablicForm


class NewsDeleteView(DeleteView):
    model = Pablic
    success_url = '/textsuit/'
    template_name = 'textsuit/delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = PablicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('textsuit_home')
        else:
            error = 'Неверное заполнение'
    form = PablicForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'textsuit/create.html', data)
# Create your views here.
