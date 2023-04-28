from . import views
from django.urls import path
app_name='mimeapp'
urlpatterns = [
path('html', views.htmldisplay),
path('xml', views.xmldisplay),
path('excel', views.exceldisplay),

]