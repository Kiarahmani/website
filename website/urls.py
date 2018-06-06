from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache
from website import settings
from website import views as website_views

admin.autodiscover()

urlpatterns = [
    url(r'^signup/', website_views.signup_view),
    url(r'^login/', website_views.login_view),
    url(r'^auth/', website_views.auth_and_login),
    url(r'^signupin/', website_views.sign_up_in),
    url(r'^$', website_views.home),
    url(r'^logout/', website_views.logout_view),

    url(r'^new_result/', website_views.new_result),
    url(r'^result/', website_views.result),

    url(r'^edit_project/', website_views.edit_project),
    url(r'^project/', website_views.project),
    url(r'^delete_project/', website_views.delete_project),
    url(r'^update_project/', website_views.update_project),

    url(r'^benchmark_conf/', website_views.benchmark_configuration),
    url(r'^edit_benchmark_conf/', website_views.edit_benchmark_conf),
    url(r'^get_benchmark_data/', website_views.get_benchmark_data),
    url(r'^get_benchmark_conf_file/', website_views.get_benchmark_conf_file),
    url(r'^update_benchmark/', website_views.update_benchmark_conf),

    url(r'^get_data/', website_views.get_timeline_data),
    url(r'^get_recent_data/', website_views.get_recent_data),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', never_cache(serve)),
    ]
