from django.urls import path

from web_basics_exam_retake.core.views import home_page, create_profile_page, dashboard_page, create_game_page, \
    details_game_page, edit_game_page, delete_game_page, details_profile_page, edit_profile_page, delete_profile_page

urlpatterns = (
    path('', home_page, name='home page'),
    path('profile/create',  create_profile_page, name='create profile'),
    path('dashboard/', dashboard_page, name='dashboard page'),
    path('game/create', create_game_page, name='create game'),
    path('game/details/<int:pk>', details_game_page, name='game details'),
    path('game/edit/<int:pk>',  edit_game_page, name='game edit'),
    path('game/delete/<int:pk>', delete_game_page, name='game delete'),
    path('profile/details/', details_profile_page, name='profile details'),
    path('profile/edit/', edit_profile_page, name='profile edit'),
    path('profile/delete/', delete_profile_page, name='profile delete'),
)