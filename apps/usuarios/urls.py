from django.urls import path
from .classes import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from . import views

urlpatterns = [
    path('', views.home_usuario, name="home_usuario"),
    path('logout/', views.user_logout, name="user_logout"),
    path('register/', views.register, name="register"),
    path('edit_profile/<int:user_id>/', views.edit_profile, name="edit_profile"),
    path('salvarProfile/<int:user_id>/', views.salvarProfile, name="salvarProfile"),
    path('alterarSenha/', views.alterarSenha, name="alterarSenha"),
    path('resetPassword/', password_reset, name="resetPassword"),
    path('resetPassword/password_reset_done/', password_reset_done, name="password_reset_done"),
    path('reset/<uidb64>/<token>/', password_reset_confirm, name="password_reset_confirm"),
    path('reset/done/', password_reset_complete, name="password_reset_complete"),
]