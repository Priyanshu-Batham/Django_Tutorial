from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    '''
    Some Field classes have required arguments. 
    CharField, for example, requires that you give it
    a max_length. That’s used not only in the database
    schema, but in validation, as we’ll soon see.
    '''
    pub_date = models.DateTimeField("date published")
    '''
    The first argument "date publised" is optional 
    in all the fields and represents a human-readable
    string. Its only given in above field as other fields
    were already human readable. If this arg is not given
    then django takes the human-readable string as the 
    variable its assigned to, in this case "pub_date"
    '''

    def __str__(self):
        return f"{self.question_text}"
    
    def was_published_recently(self):
        return (self.pub_date >= timezone.now() - datetime.timedelta(days=1)) and (self.pub_date <= timezone.now())

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    '''
    Django supports all the common database relationships:
    many-to-one, many-to-many, and one-to-one.
    '''
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    '''
    A Field can also have various optional
    arguments; in this case, we’ve set the default
    value of votes to 0.
    '''

    def __str__(self):
        return f"{self.choice_text}"
