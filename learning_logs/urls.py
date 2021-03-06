"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""Определяет схемы URL для learning_logs."""
from django.conf.urls import url
from . import views

urlpatterns = [
    # Домашняя страница
    url(r'^$', views.index, name='index'),

    # Вывод всех тем.
    url(r'^topics/$', views.topics, name='topics'),

    # Страница с подробной информацией по отдельной теме
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # Страница для добавления новой темы
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    
    # Страница для добавления новой записи
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # Страница для редактирования записи
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
    name='edit_entry'),
]
app_name = 'learning_logs'
