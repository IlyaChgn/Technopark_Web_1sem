from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app import views
from askme import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('search/<str:tag_name>/', views.search, name='search'),
    path('hot/', views.show_hot, name='hot'),
    path('ask/', views.ask, name='ask'),
    path('login/', views.log_in, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('settings/', views.settings, name='settings'),
    path('admin/', admin.site.urls),
    path('rate/', views.rate, name='rate'),
    path('correct/', views.correct, name='correct'),
    path('find/', views.find, name='find'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
