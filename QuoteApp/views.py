from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import QuotePost, QuoteComment
from .forms import QuoteForm, QuoteCommentForm
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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
    template_name = 'quoteapp/quote_detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        quote_like = get_object_or_404(QuotePost, id=self.kwargs['pk'])
        data['sum_like'] = quote_like.sum_likes()
        data['sum_comment'] = quote_like.sum_comments()
        return data


class CreateQuotePostView(CreateView):
    login_required = True
    model = QuotePost
    fields = ['text', 'tag']
    success_url = reverse_lazy('quote:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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


def quote_post_like(request, pk):
    quote = get_object_or_404(QuotePost, id=request.POST.get('quotepost_id'))
    if quote.likes.filter(id=request.user.id).exists():
        quote.likes.remove(request.user)
    else:
        quote.likes.add(request.user)

    return HttpResponseRedirect(reverse('quote:detail', args=[str(pk)]))


###############################


@login_required()
def quote_comment_view(request, pk):
    quote = get_object_or_404(QuotePost, pk=pk)
    if request.method == 'POST':
        form = QuoteCommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.quote = quote
            obj.save()
            return redirect('quote:detail', pk=quote.pk)
    else:
        form = QuoteCommentForm()

    return render(request, 'quoteapp/comment_form.html', {'form': form})


@login_required()
def quote_comment_approve(request, pk):
    comment = get_object_or_404(QuoteComment, pk=pk)
    comment.approve()

    return redirect('quoteapp:detail', pk=comment.quote.pk)


@login_required()
def quote_comment_delete(request, pk):
    comment = get_object_or_404(QuoteComment, pk=pk)
    quote_pk = QuoteComment.quote.pk
    comment.delete()

    return redirect('quoteapp:detail', pk=quote_pk)


@login_required()
def quote_post_publish(request, pk):
    quote = get_object_or_404(QuotePost, pk=pk)
    quote.publish()
    return redirect('quoteapp:detail', pk=pk)
