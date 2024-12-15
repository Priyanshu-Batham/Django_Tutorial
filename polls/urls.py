from django.urls import path
from . import views

app_name="polls"

# URLconf without generic(class based) views
# urlpatterns = [
#     # ex: /polls/
#     path("", views.index, name="index"),
#     #<converter:pattern_name>
#     # ex: /polls/5/
#     path("<int:question_id>/", views.detail, name="detail"),
#     #the name we are giving here like name="results" will be used to reference this url from any template using {% url %} django tag
#     # ex: /polls/5/results/
#     path("<int:question_id>/results/", views.results, name="results"),
#     # ex: /polls/5/vote/
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]

# URLconf with generic(class based) views
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    #the name "pk" for primary key is mandatory in generic views
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]