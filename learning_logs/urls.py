"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from learning_logs import views

urlpatterns = [
    path('',views.index,name='index'),
    path('topics/',views.topics,name='topics'),
    path('topics/<int:id>/',views.topic,name='topic'),
    path('new_topics/',views.new_topic,name='new_topic'),
    path('new_entry/<int:topic_id>/',views.new_entry,name = 'new_entry'),
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),
]

app_name = 'learning_logs'