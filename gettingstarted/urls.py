from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('db_managment/', hello.views.db_managment, name='db_managment'),
    path('db_create_table/', hello.views.db_create_table, name='db_create_table'),
    path('db_delete_table/', hello.views.db_delete_table, name='db_delete_table'),
    path('db_select_all/', hello.views.db_select_all, name='db_select_all'),
    path('db_insert_row/', hello.views.db_insert_row, name='db_insert_row')
]
