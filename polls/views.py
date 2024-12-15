from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from .models import Question, Choice
from django.views import generic
#for long method
#from django.template import loader

#for short method
from django.shortcuts import render, get_object_or_404

# Create your views here.
#INDEX view as a function
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]

#     context = {
#         "latest_question_list": latest_question_list
#     }
#     #long method
#     #template = loader.get_template("polls/index.html")
#     #return HttpResponse(template.render(context, request))

#     #shortcut
#     return render(request, "polls/index.html", context)

#INDEX view as generic view
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    #default context object name is "<model name>" 
    context_object_name = "latest_question_list"

    def get_queryset(self):
        #return the last five published questions
        return Question.objects.order_by("-pub_date")[:5]

# DETAIL view as function
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
    # return render(request, "polls/detail.html", {"question": question})

#DETAIL view as generic view
class DetailView(generic.DetailView):
    #By default template_name will be "<app name>/<model name>_detail.html"
    model = Question
    template_name = "polls/detail.html"

#RESULT view as function
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})
    
#RESULT view as generic view
class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)    
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    #KeyError if request.POST['choice'] doesn't exists
    except(KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice"
        })
    else:
        '''
        F is used to do update without pulling value in python memory
        we couldv'e done selected_choice.votes += 1 too.
        '''
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))