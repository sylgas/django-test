from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView

class StaticView(TemplateView):
    def get_template_names(self):
        return [self.kwargs.get('template_name') + ".html"]

    def get(self, request, *args, **kwargs):
        # if request.user.is_anonymous():
        #     # Auto-login the User for Demonstration Purposes
        #     user = authenticate()
        #     login(request, user)
        return super(StaticView, self).get(request, *args, **kwargs)

class ConnectionView(StaticView):
    context_object_name = 'person'

index = TemplateView.as_view(template_name='index.html')
static = StaticView.as_view()