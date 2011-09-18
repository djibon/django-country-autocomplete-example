from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'autocomplete_demo.views.home', name='home'),
    # url(r'^autocomplete_demo/', include('autocomplete_demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
                       url(r'^$','demo.views.home',name="demo-home"),
                       url(r'^country-lookup','countries.views.countries_lookup', name="countries_countries_lookup"),
                       url(r'^city-lookup','countries.views.cities_lookup', name="countries_cities_lookup"),
                       
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )

