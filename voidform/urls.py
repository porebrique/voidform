from django.conf.urls import *
from django.conf import settings
from django.views.generic import TemplateView, RedirectView
import karhu
#from django.contrib import admin





#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'voidform.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^files(?P<path>/.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                       
 #   url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="index"),
    
    (r'', include('karhu.urls')),    # Required for karhu
    
) #+ karhu.urls.urlpatterns
