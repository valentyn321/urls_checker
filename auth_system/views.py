from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm


class RegisterTemplateView(TemplateView):
    template_name = 'auth_system/register.html'
    form = UserCreationForm

    def get(self, request):
        return render(request, self.template_name, {"form": self.form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid:
            user = form.save()
            user.save()
            return redirect("main_page")
        else:
            return render(request, self.template_name, {"form": self.form})
