from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'august.views.home', name='home'),
    # url(r'^august/', include('august.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^ask/', include('ask.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^online/', include('online.urls')),
    url(r'^disk/', include('disk.urls'))
    # url(r'^tinymce/', include('tinymce.urls')),
)

# django_debug_toolbar
# from django.conf import settings
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += patterns('',
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     )


