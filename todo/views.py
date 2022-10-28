from django.shortcuts import render

# Create your views here.


def get_todo_list(request):
    return render(request, 'todo/todo_list.html')
    # return HttpResponse("<h1>Hello!</h2><p>This is the paragraph below</p>") requires httpresponse imported
