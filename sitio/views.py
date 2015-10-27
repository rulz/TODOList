from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse, reverse_lazy

from todo.models import Task


class TaskListView(ListView):
    model = Task
    template_name = 'todo2/task_list.html'

    # def get_queryset(self):
    #     q = super(TaskListView, self).get_queryset(self)
    #     return q.filter(delete=False)

task_list = TaskListView.as_view()

class TaskCreateView(CreateView):
    model = Task
    template_name = 'todo2/task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('task_list')

task_create = TaskCreateView.as_view()

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'todo2/task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('task_list')

task_update = TaskUpdateView.as_view()

class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo2/task_detail.html'
    success_url = reverse_lazy('task_list')

task_detail = TaskDetailView.as_view()

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo2/task_delete.html'
    success_url = reverse_lazy('task_list')

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     success_url = self.get_success_url()
    #     self.object.status = True
    #     self.object.save()

    #     return HttpResponseRedirect(success_url)

task_delete = TaskDeleteView.as_view()