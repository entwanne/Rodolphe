from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from main.views import paging, thread, post, tag, search, about

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', paging.page, name="home"),

    url(r'^view/(?P<post_id>\d+)$', thread.view, name="view"),
    url(r'^new$', thread.new),

    url(r'^raw/(?P<post_id>\d+)$', post.raw, name="raw"),
    url(r'^edit/(?P<post_id>\d+)$', post.edit, name="edit"),
    url(r'^del/(?P<post_id>\d+)$', post.delete, name="delete"),
    url(r'^h/(?P<post_id>\d+)$', post.history, name="history"),

    url(r'^tags$', tag.index),
    url(r'^tag/(?P<pattern>(~?\w+)(\|~?\w+)*)$', tag.search, name="search_tag"),

    url(r'^search$', search.search, name="search"),

    url(r'^about$', about.about, name="about"),
    url(r'^markdown$', about.markdown, name="about"),
    url(r'^render$', about.render),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^captcha/', include('captcha.urls')),

    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt',
                                               content_type='text/plain'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
