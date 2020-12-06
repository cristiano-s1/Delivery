from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import RegistrationForm, UserProfileForm
from .models import UserProfile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def home_usuario(request):
    pass


def user_logout(request):
    logout(request)
    return redirect('/pizzaria/')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            mensagem = "Usuário criado com sucesso!"
            context = {
                'mensagem': mensagem,
            }
            return render(request, "core/index.html", context)
        else:
            mensagem = "Dados inválidos!"
            form = RegistrationForm()
            context = {
                'form': form,
                'mensagem': mensagem,
            }
            return render(request, "usuarios/register.html", context)
    else:
        form = RegistrationForm()
        context = {
            'form': form,
        }
        return render(request, 'usuarios/register.html', context)


def edit_profile(request, user_id):
    usuario = UserProfile.objects.get(user_id=user_id)
    user_dado = User.objects.get(id=user_id)
    context = {
        'usuario': usuario,
        'user_dado': user_dado
    }
    return render(request, "usuarios/edit_profile.html", context)


def salvarProfile(request, user_id):
    usuario = UserProfile.objects.get(user_id=user_id)
    user_dado = User.objects.get(id=user_id)
    telefone = request.POST.get("telefone")
    endereco_completo = request.POST.get("endereco_completo")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    email = request.POST.get("email")
    usuario.user_id = user_id
    usuario.telefone = telefone
    usuario.endereco_completo = endereco_completo
    usuario.save()
    user_dado.id = user_id
    user_dado.first_name = first_name
    user_dado.last_name = last_name
    user_dado.email = email
    user_dado.save()
    return redirect('/pizzaria/')


def alterarSenha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, "core/index.html")
        else:
            return redirect('/pizzaria/')
    else:
        form = PasswordChangeForm(user=request.user)
        context = {
            'form': form
        }
        return render(request, "usuarios/alterarSenha.html", context)

