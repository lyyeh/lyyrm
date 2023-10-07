"""resourcemanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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

from django.urls import path
from . import associate_views
from .associate_views import recordlist, recorddetail, addrecord

# URL config
urlpatterns = [
    #path('submitted/', associates_views.thank_you),
    path('', associate_views.thank_you, name="home"),
    path('add/', associate_views.associate_add, name="associate-add"),
    path('search/', associate_views.associate_search, name="associate-search"),
    path('list/', associate_views.associate_list, name="associate-list"),
    path('associate/<associate_id>', associate_views.associate_record, name="associate-record"),
    path('update/<associate_id>', associate_views.associate_update, name="associate-update"),
    #path('', associates_views.input_form)
    #path ('', addrecord.as_view(), name='home'),
    #path ('webform/', addrecord.as_view(), name='inputform'),
    #path ('associate/<int:pk>', recorddetail.as_view(), name='recorddetail'),
    #path ('list/', recordlist.as_view(), name='recordlist'),

]
