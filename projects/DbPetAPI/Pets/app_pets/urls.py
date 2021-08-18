from django.urls import path

from .views import RegistrationView, LoginViews, LogoutViews, PetCreate, PetList, DeletePet, PetUpdate, PetDetail, \
    PetListView, PetDetailView

urlpatterns = [
    path('', PetList.as_view(), name='pet_list'),
    path('userregistr/', RegistrationView.as_view(), name='registrs'),
    path('login/', LoginViews.as_view(), name='login'),
    path('logout/', LogoutViews.as_view(), name='logout'),
    path('create/', PetCreate.as_view(), name='create'),
    path('delete/<int:pk>/', DeletePet.as_view(), name='delete'),
    path('update/<int:pk>/', PetUpdate.as_view(), name='edit'),
    path('detail/<int:pk>', PetDetail.as_view(), name='detail'),
    path('api_list/', PetListView.as_view(), name='pet_list_api'),
    path('api_detail/<int:pk>/', PetDetailView.as_view(), name='detail_pet_list'),

]