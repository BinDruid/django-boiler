from django.shortcuts import redirect
from django.views.generic import TemplateView


class ViewHome(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(ViewHome, self).get_context_data(**kwargs)
        context["pageTitle"] = "صفحه اصلی"
        return context


def handle_erro_404(request, exception):
    return redirect("home")
