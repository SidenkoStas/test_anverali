from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CreateUser(CreateView):
    """
    View for creating new users.
    """
    model = CustomUser
    template_name = "users/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("index")


class UserDetail(DetailView):
    """
    View for displaying user details.
    """
    model = CustomUser

    def get_template_names(self):
        if self.object.is_executor:
            return "users/executor_detail.html"
        return "users/user_detail.html"


class UserUpdate(UpdateView):
    """
    View for updating user details.
    """
    model = CustomUser
    template_name = "users/update.html"
    form_class = CustomUserChangeForm
