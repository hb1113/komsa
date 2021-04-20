from django.urls import path
from . import views

app_name = 'quote'
urlpatterns = [
    path('', views.QuoteListView.as_view(), name='list'),
    path('<int:id>', views.QuoteDetailView.as_view(), name='detail'),
    path('newquote/', views.CreateQuotePostView.as_view(), name='new'),
    path('update/<int:id>/', views.UpdateQuotePostView.as_view(), name='update'),
    path('delete/<int:id>/', views.DeleteQuotePostView.as_view(), name='delete'),
    path('drafts/', views.DraftQuoteListView.as_view(), name='draft'),
    path('about/', views.AboutQuoteView.as_view(), name='about'),
]
