from django.contrib import admin

from posts.models import Reason, Subject, Post


[admin.site.register(klass) for klass in [Reason, Subject, Post]]