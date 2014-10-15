from django.conf.urls import patterns, include, url
from django.templatetags.static import static
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'deck.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'playing_cards.views.cards', name='cards'),
    url(r'^card_filters/$', 'playing_cards.views.card_filters', name='card_filters'),
    url(r'^faq/$', 'playing_cards.views.faq', name='faq'),
    url(r'^profile/$', 'playing_cards.views.profile', name='profile'),
    url(r'^deal_5/$', 'playing_cards.views.deal_5', name='deal_5'),
    url(r'^blackjack/$', 'playing_cards.views.blackjack', name='blackjack'),
    url(r'^poker/$', 'playing_cards.views.poker', name='poker'),
    url(r'^all_hearts/$', 'playing_cards.views.all_hearts', name='all_hearts'),
    url(r'^register/$', 'playing_cards.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^war/$', 'playing_cards.views.war', name='war'),
    url(r'^leaderboard/$', 'playing_cards.views.leaderboard', name='leaderboard'),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)