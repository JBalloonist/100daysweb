from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect

from .models import Quote
from .forms import QuoteForm


def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/quote_list.html', {'quotes': quotes})

def quote_detail(request):
    try:
        Quote.objects.get(pk=pk)
    except Quote.DoesNotExist:
        raise Http404


def quote_new(request, pk):
    pass


def quote_edit(parameter_list, pk):
    pass


def quote_delete(request, pk):
    pass