from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import QuotePost, QuoteComment
from .forms import QuoteForm, QuoteCommentForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class AboutQuoteView(TemplateView):
    template_name = 'quoteapp/about-quote.html'


class QuoteListView(ListView):
    model = QuotePost
    template_name = 'quoteapp/quote-list.html'

    def get_queryset(self):
        return QuotePost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class QuoteDetailView(DetailView):
    model = QuotePost


class CreateQuotePostView(CreateView):
    login_required = True
    form_class = QuoteForm
    model = QuotePost
    fields = ['text']


class UpdateQuotePostView(UpdateView):
    login_required = True
    form_class = QuoteForm
    model = QuotePost
    fields = ['text']


class DeleteQuotePostView(DeleteView):
    model = QuotePost
    success_url = reverse_lazy('list')


class DraftQuoteListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    redirect_field_name = 'list'
    model = QuotePost

    def get_queryset(self):
        return QuotePost.objects.filter(published_date__isnull=True).order_by('created_date')


class QuoteCommentsView(ListView):
    model = QuoteComment
    template_name = 'quoteapp/quote-comments.html'

    def get_queryset(self):
        return QuoteComment.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


