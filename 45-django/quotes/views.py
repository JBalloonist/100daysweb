from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect

from .models import Quote
from .forms import QuoteForm


def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/quote_list.html', {'quotes': quotes})

def quote_detail(request):
    quote = get_object_or_404(Quote, pk=pk)
    return render(request, 'quotes/quote_detail.html', {'quote': quote})


def quote_new(request, pk):
    pass


def quote_edit(parameter_list, pk):
    pass


def quote_delete(request, pk):
    pass