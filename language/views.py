from django.views.generic import ListView, DetailView
from language.models import Language


class LanguagesListView(ListView):
    template_name = "list.html"
    context = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object_list = self._queryset()

    @staticmethod
    def _queryset():
        return Language.objects.all()

    def get(self, request, *args, **kwargs):
        self.context.update({
            'languages': self.object_list
        })
        return self.render_to_response(self.context)


class LanguagesDetailView(DetailView):
    template_name = "detail.html"
    context = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.object_list = self._queryset()

    @staticmethod
    def _queryset():
        return Language.objects.all()

    def get(self, request, *args, **kwargs):
        self.context.update({
            'languages': self.object_list
        })
        return self.render_to_response(self.context)
