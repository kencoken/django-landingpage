from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'landingpage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'userreg.views.register',
        name='register'),
    url(r'^success/$', 'userreg.views.registration_success',
        name='registration_success'),
    url(r'^admin/', include(admin.site.urls)),
)
