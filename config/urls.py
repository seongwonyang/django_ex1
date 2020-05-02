from django.contrib import admin
# from django.urls import path

# Django의 내장함수를 import
from django.conf.urls import re_path

# 각 url에 매핑시킬 뷰들을 bookmark의 views.py에서 가져와 import
from bookstore.views import BookstoreListView, BookstoreDetailView


"""
re_path(regex, view, name): re_path()는 주로 세 개의 인자를 사용합니다.
                            regex는 정규식, view는 해당 url 패턴에 매핑시킬 뷰,
                            name은 해당 url 패턴에 붙일 이름을 의미합니다.
"""
urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^admin/', admin.site.urls),

    re_path(r'^bookstore/$', BookstoreListView, name='list'),
    re_path(r'^bookstore/(?P<pk>[d]\d+)/$', BookstoreDetailView, name='detail'),
]
