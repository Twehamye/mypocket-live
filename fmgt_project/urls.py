
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fmgt_app.urls')),
]

# config Admin Page
admin.site.site_header = "EYEKONIC PANEL"
admin.site.site_title = "EYEKONIC WEBSITE"
admin.site.index_title = "Welcome To The Administration Area" 