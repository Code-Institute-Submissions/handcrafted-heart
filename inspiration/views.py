from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Inspiration
from .forms import InspirationSharingForm
from django.template.context_processors import csrf
from django.contrib.auth.models import User

# Create your views here.

def get_inspiration(request):
    inspirations = Inspiration.objects.all()
    return render(request, "inspiration.html", {'inspirations': inspirations})
    
@login_required()
def inspiration_content(request, pk):
    if request.method == "GET":
        inspiration = get_object_or_404(Inspiration, pk=pk)
        inspiration.save()
        return render(request, "inspiration_content.html", {'inspiration': inspiration})
    if request.method == "POST":
        inspiration = get_object_or_404(Inspiration, pk=pk)
        inspiration.save()
        return redirect('/inspiration/', {'inspiration': inspiration})


@login_required()
def create_or_edit_inspiration(request, pk=None):
    inspirations = Inspiration.objects.all()
    
    inspiration = get_object_or_404(Inspiration, pk=pk) if pk else None
    if request.method == "POST":
        form = InspirationSharingForm(request.POST, request.FILES, instance=inspiration)
        if form.is_valid():
            if inspiration:
              inspiration.title = form.cleaned_data.get('title')
              inspiration.content = form.cleaned_data.get('content')
              inspiration.published_date = form.cleaned_data.get('published_date')
              inspiration.save()
              return render(request, 'inspiration.html', {'inspirations' : inspirations})
            else:
              inspiration = form.save()
              return redirect('inspiration_content', inspiration.pk)
    else:
        form = InspirationSharingForm(instance=inspiration)
    return render(request, 'inspirationform.html', {'form': form, 'inspiration': inspiration})
    