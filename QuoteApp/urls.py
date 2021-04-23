from django.urls import path
from . import views

app_name = 'quote'
urlpatterns = [
    path('', views.QuoteListView.as_view(), name='list'),
    path('<int:pk>', views.QuoteDetailView.as_view(), name='detail'),
    path('newquote/', views.CreateQuotePostView.as_view(), name='new'),
    path('update/<int:id>/', views.UpdateQuotePostView.as_view(), name='update'),
    path('delete/<int:id>/', views.DeleteQuotePostView.as_view(), name='delete'),
    path('drafts/', views.DraftQuoteListView.as_view(), name='draft'),
    path('<int:pk>/comment/', views.quote_comment_view, name='comment'),
    path('comment/<int:id>/approve/', views.quote_comment_approve, name='comment-approve'),
    path('comment/<int:id>/delete', views.quote_comment_delete, name='delete'),
    path('<int:id>/publish', views.quote_post_publish, name='publish'),
    path('about/', views.AboutQuoteView.as_view(), name='about'),
]
