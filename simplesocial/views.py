from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "simplesocial/index.html"    

class TestPage(TemplateView):
    template_name = "simplesocial/test.html"

class ThanksPage(TemplateView):
    template_name = "simplesocial/thanks.html"