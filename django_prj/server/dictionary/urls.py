from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^word/create/$', views.WordView.as_view({'post': 'create'})),
    url(r'^word/update/(?P<w_name>\w+)/$', views.WordView.as_view({'put': 'update'})),
    url(r'^word/(?P<w_name>\w+)/$', views.WordView.as_view({'get': 'retrieve'})),

    url(r'^wordtags/create/$', views.WordTagsView.as_view({'post': 'create'})),
    url(r'^wordtags/delete/(?P<pk>\w+)/$', views.WordTagsView.as_view({'delete': 'destroy'})),
    url(r'^wordtags/$', views.WordTagsView.as_view({'get': 'list'})),

    url(r'^sentence/create/$', views.SentenceView.as_view({'post': 'create'})),
    url(r'^sentence/update/(?P<pk>\d+)/$', views.SentenceView.as_view({'put': 'update'})),
    url(r'^sentence/delete/(?P<pk>\w+)/$', views.SentenceView.as_view({'delete': 'destroy'})),
    url(r'^sentence/(?P<pk>\d+)/$', views.SentenceView.as_view({'get': 'retrieve'})),
    url(r'^sentence/$', views.SentenceView.as_view({'get': 'list'})),

    url(r'^sentencetags/create/$', views.SentenceTagsView.as_view({'post': 'create'})),
    url(r'^sentencetags/delete/(?P<pk>\w+)/$', views.SentenceTagsView.as_view({'delete': 'destroy'})),
    url(r'^sentencetags/$', views.SentenceTagsView.as_view({'get': 'list'})),

    url(r'^sentencetags/create/$', views.SentenceTagsView.as_view({'post': 'create'})),
    url(r'^sentencetags/delete/(?P<pk>\w+)/$', views.SentenceTagsView.as_view({'delete': 'destroy'})),
    url(r'^sentencetags/$', views.SentenceTagsView.as_view({'get': 'list'})),

    url(r'^grammar/create/$', views.GrammarView.as_view({'post': 'create'})),
    url(r'^grammar/update/(?P<pk>\d+)/update/$', views.GrammarView.as_view({'put': 'update'})),
    url(r'^grammar/delete/(?P<pk>\d+)/$', views.GrammarView.as_view({'delete': 'destroy'})),
    url(r'^grammar/(?P<pk>\d+)/$', views.GrammarView.as_view({'get': 'retrieve'})),

    url(r'^distinguish_word/create/$', views.DistinguishWordView.as_view({'post': 'create'})),
    url(r'^distinguish_word/update/(?P<pk>\d+)/$', views.DistinguishWordView.as_view({'put': 'update'})),
    url(r'^distinguish_word/delete/(?P<pk>\d+)/$', views.DistinguishWordView.as_view({'delete': 'destroy'})),
    url(r'^distinguish_word/(?P<pk>\d+)/$', views.DistinguishWordView.as_view({'get': 'retrieve'})),

    url(r'^word_to_sentence/create/$', views.WordToSentenceView.as_view({'post': 'create'})),
    url(r'^word_to_sentence/update/(?P<wtg_word>\w+)/$', views.WordToSentenceView.as_view({'put': 'update'})),
    url(r'^word_to_sentence/(?P<wtg_word>\w+)/$', views.WordToSentenceView.as_view({'delete': 'destroy'})),
    url(r'^word_to_sentence/$', views.WordToSentenceView.as_view({'get': 'list'})),

    url(r'^etyma/create/$', views.EtymaView.as_view({'post': 'create'})),
    url(r'^etyma/update/(?P<pk>\w+)/$', views.EtymaView.as_view({'put': 'update'})),
    url(r'^etyma/delete/(?P<pk>\w+)/$', views.EtymaView.as_view({'delete': 'destroy'})),
    url(r'^etyma/(?P<pk>\w+)/$', views.EtymaView.as_view({'get': 'retrieve'})),

    url(r'^soundmark/create/$', views.SoundmarkView.as_view({'post': 'create'})),
    url(r'^soundmark/update/(?P<s_name>\w+)/$', views.SoundmarkView.as_view({'put': 'update'})),
    url(r'^soundmark/(?P<s_name>\w+)/$', views.SoundmarkView.as_view({'get': 'retrieve'})),
    url(r'^soundmark/$', views.SoundmarkView.as_view({'get': 'list'})),

    url(r'^relative_word/create/$', views.RelativeWordView.as_view({'post': 'create'})),
    url(r'^relative_word/delete/(?P<pk>\d+)/$', views.RelativeWordView.as_view({'delete': 'destroy'})),
    url(r'^relative_word/$', views.RelativeWordView.as_view({'get': 'list'})),

    url(r'^relative_sentence/create/$', views.RelativeSentenceView.as_view({'post': 'create'})),
    url(r'^relative_sentence/(?P<pk>\d+)/update/$', views.RelativeSentenceView.as_view({'delete': 'destroy'})),
    url(r'^relative_sentence/$', views.RelativeSentenceView.as_view({'get': 'list'})),
]
