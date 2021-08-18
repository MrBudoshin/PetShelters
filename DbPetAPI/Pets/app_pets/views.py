from abc import ABC

from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View, generic
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin

from .models import Profile, Pet
from .forms import RegisterForm, CreatePet
from .serializer import PetSerializer


class PetList(generic.ListView):
    """
    List of pets
    """
    model = Pet
    template_name = 'app_pets/base_petlist.html'
    context_object_name = 'pets'


class PetDetail(generic.DetailView):
    """
    Detail information about pets
    """
    model = Pet
    template_name = 'app_pets/base_petdetail.html'
    context_object_name = 'pets_detail'


class PetUpdate(UserPassesTestMixin, generic.UpdateView, ABC):
    """
    Update information about pets
    """
    model = Pet
    template_name = 'app_pets/base_petupdte.html'
    form_class = CreatePet
    success_url = reverse_lazy('pet_list')

    def test_func(self):
        return self.request.user.groups.filter(name__in=['Admin', 'Nursery']).exists()


class DeletePet(UserPassesTestMixin, generic.DeleteView, ABC):
    """
    Delete pet
    """
    model = Pet
    template_name = 'app_pets/base_delete.html'
    context_object_name = 'delete'
    success_url = reverse_lazy('pet_list')

    def test_func(self):
        return self.request.user.groups.filter(name__in=['Admin']).exists()


class PetCreate(UserPassesTestMixin, View, ABC):
    """
    Add new pet
    """
    def test_func(self):
        return self.request.user.groups.filter(name__in=['Admin', 'Nursery']).exists()

    def get(self, request, *args, **kwargs):
        create_pet = CreatePet()
        return render(request, 'app_pets/base_petcreate.html', context={'create_pet': create_pet})

    def post(self, request, *args, **kwargs):
        create_pet = CreatePet(request.POST)
        if create_pet.is_valid():
            Pet.objects.create(**create_pet.cleaned_data)
            return HttpResponseRedirect('/')
        else:
            return render(request, 'app_pets/base_petcreate.html', context={'create_pet': create_pet})


class LoginViews(LoginView):
    """
    Login
    """
    template_name = 'app_pets/base_login.html'
    next_page = reverse_lazy('pet_list')


class LogoutViews(LogoutView):
    """Logout"""
    next_page = reverse_lazy('pet_list')


class RegistrationView(View):
    """Registration user"""

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'app_pets/base_registr.html', {'form': form})

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                name = form.cleaned_data.get('first_name')
                surname = form.cleaned_data.get('last_name')
                mail = form.cleaned_data.get('mail')
                phone = form.cleaned_data.get('phone')
                Profile.objects.create(
                    users=user,
                    first_name=name,
                    last_name=surname,
                    mail=mail,
                    phone=phone,
                )
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                form = RegisterForm()
                return render(request, 'app_pets/base_registr.html', {'form': form})


class PetListView(ListModelMixin, RetrieveModelMixin, GenericAPIView):
    """
    View pet list information

    """
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def get(self, request):
        return self.list(request)


class PetDetailView(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """
    View to get detail information  update/delete model

    """
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
