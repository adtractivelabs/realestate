from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from rstate import settings

urlpatterns = [
    path('',include('rportal.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog-site/',include('rblog.urls')),
    path('admin/',admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
