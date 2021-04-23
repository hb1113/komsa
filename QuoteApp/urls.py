from django.urls import path
from . import views

app_name = 'quote'
urlpatterns = [
    path('', views.QuoteListView.as_view(), name='list'),
    path('<int:pk>', views.QuoteDetailView.as_view(), name='detail'),
    path('newquote/', views.CreateQuotePostView.as_view(), name='new'),
    path('update/<int:pk>/', views.UpdateQuotePostView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteQuotePostView.as_view(), name='delete'),
    path('drafts/', views.DraftQuoteListView.as_view(), name='draft'),
    path('<int:pk>/comment/', views.quote_comment_view, name='comment'),
    path('comment/<int:pk>/approve/', views.quote_comment_approve, name='comment-approve'),
    path('comment/<int:pk>/delete', views.quote_comment_delete, name='delete'),
    path('<int:pk>/publish', views.quote_post_publish, name='publish'),
    path('about/', views.AboutQuoteView.as_view(), name='about'),
]
