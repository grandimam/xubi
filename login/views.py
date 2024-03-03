from django.views.generic.edit import FormView

from login.forms import LoginForm


class LoginPageView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/app'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
