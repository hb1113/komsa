from django.contrib import admin
from .models import QuotePost, QuoteComment
# Register your models here.


admin.site.register(QuotePost)
admin.site.register(QuoteComment)
