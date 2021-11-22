from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView, UpdateView
from .models import Todo
from .forms import LoginForm, RegisterForm,RecordForm



class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

@method_decorator(login_required, name = 'dispatch')
class TodoListView(ListView):
    model = Todo
    template_name = 'to_do_app/to_do.html'

    def get_search_query(self, query):
        qobj = Q()
        search_query = []
        if query:
            query = query[0].split(',')
            for q in query:
                try:
                    key, value = q.split(':')
                    search_query.append(Q(**{key: value}))
                except Exception as e:
                    qobj |= Q(title__icontains = q)
                    qobj |= Q(category__icontains = q)
                    qobj |= Q(due_date__icontains = q)
        return qobj, search_query

    def get_queryset(self):
        query = self.request.GET.getlist('query', 0)
        queryset = super(TodoListView, self).get_queryset()
        qobj, search_query = self.get_search_query(query)
        queryset = Todo.objects.all()
        return queryset.filter(*search_query, qobj).distinct() if query else queryset

@method_decorator(login_required, name = 'dispatch')
class TodoDeleteView(DeleteView):
    model = Todo
    success_url = "/to_do/to-do-list/"

@method_decorator(login_required, name = 'dispatch')
class TodoCreateView(CreateView,SuccessMessageMixin):
    model = Todo
    form_class = RecordForm
    success_url = '/to_do/to-do-list'
    success_message = "Record Created"

    def form_valid(self, form):
        messages.success(self.request, 'form is valid')
        form.instance.user = self.request.user
        form.save()
        return super(TodoCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('to_do_list')

@method_decorator(login_required, name = 'dispatch')
class TodoUpdateView(UpdateView,SuccessMessageMixin):
    model = Todo
    form_class = RecordForm
    success_url = '/to_do/to-do-list'
    success_message = "Record Updated"

    def form_valid(self, form):
        messages.success(self.request, 'form is valid')
        form.instance.user = self.request.user
        form.save()
        return super(TodoUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('to_do_list')


