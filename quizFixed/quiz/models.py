from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):

    quiz_id = models.IntegerField(unique=True,primary_key=True)
    started = models.BooleanField(default=False)

    def __str__(self):
        return 'Quiz ' + str(self.quiz_id)

    def get_rounds(self):
        rounds = Round.objects.filter(quiz_id=self.quiz_id)
        return rounds

class Round(models.Model):

    status_choices = [
        ('WA', 'Waiting for Answers'),
        ('SA', 'Showing Answers'),
        ]

    quiz_id = models.ForeignKey('Quiz',on_delete=models.CASCADE)
    round_number = models.IntegerField()
    round_status = models.CharField(max_length=2, default='WA', choices=status_choices)
    pic_round = models.BooleanField(default=False)

    question1 = models.CharField(max_length=256)
    true_answer1 = models.CharField(max_length=50)
    question2 = models.CharField(max_length=256)
    true_answer2 = models.CharField(max_length=50)
    question3 = models.CharField(max_length=256)
    true_answer3 = models.CharField(max_length=50)
    question4 = models.CharField(max_length=256)
    true_answer4 = models.CharField(max_length=50)
    question5 = models.CharField(max_length=256)
    true_answer5 = models.CharField(max_length=50)
    question6 = models.CharField(max_length=256)
    true_answer6 = models.CharField(max_length=50)
    question7 = models.CharField(max_length=256)
    true_answer7 = models.CharField(max_length=50)
    question8 = models.CharField(max_length=256)
    true_answer8 = models.CharField(max_length=50)
    question9 = models.CharField(max_length=256)
    true_answer9 = models.CharField(max_length=50)
    question10 = models.CharField(max_length=256)
    true_answer10 = models.CharField(max_length=50)

    picture1 = models.ImageField(upload_to='quiz_pics',blank=True)
    picture2 = models.ImageField(upload_to='quiz_pics',blank=True)
    picture3 = models.ImageField(upload_to='quiz_pics',blank=True)
    picture4 = models.ImageField(upload_to='quiz_pics',blank=True)
    picture5 = models.ImageField(upload_to='quiz_pics',blank=True)
    picture6 = models.ImageField(upload_to='quiz_pics',blank=True)
    picture7 = models.ImageField(upload_to='quiz_pics',blank=True)
    picture8 = models.ImageField(upload_to='quiz_pics',blank=True)
    picture9 = models.ImageField(upload_to='quiz_pics',blank=True)
    picture10 = models.ImageField(upload_to='quiz_pics',blank=True)

    def __str__(self):
        return str(self.round_number)

    def list_questions(self):

        return [self.question1, self.question2, self.question3, self.question4, self.question5,
                self.question6, self.question7, self.question8, self.question9, self.question10]

    def list_answers(self):

        return [self.true_answer1, self.true_answer2, self.true_answer3,
                self.true_answer4, self.true_answer5, self.true_answer6,
                self.true_answer7, self.true_answer8, self.true_answer9,
                self.true_answer10]

class Answer(models.Model):

    quiz_number = models.IntegerField()
    round_number = models.IntegerField()
    username = models.CharField(max_length=50)

    answer1 = models.CharField(max_length=50,blank=True)
    correct1 = models.BooleanField(default=False)
    answer2 = models.CharField(max_length=50,blank=True)
    correct2 = models.BooleanField(default=False)
    answer3 = models.CharField(max_length=50,blank=True)
    correct3 = models.BooleanField(default=False)
    answer4 = models.CharField(max_length=50,blank=True)
    correct4 = models.BooleanField(default=False)
    answer5 = models.CharField(max_length=50,blank=True)
    correct5 = models.BooleanField(default=False)
    answer6 = models.CharField(max_length=50,blank=True)
    correct6 = models.BooleanField(default=False)
    answer7 = models.CharField(max_length=50,blank=True)
    correct7 = models.BooleanField(default=False)
    answer8 = models.CharField(max_length=50,blank=True)
    correct8 = models.BooleanField(default=False)
    answer9 = models.CharField(max_length=50,blank=True)
    correct9 = models.BooleanField(default=False)
    answer10 = models.CharField(max_length=50,blank=True)
    correct10 = models.BooleanField(default=False)

    def __str__(self):
        return self.username + ': ' + str(self.quiz_number) + ' Round ' + str(self.round_number)

    def get_round_score(self):

        score = self.correct1 + self.correct2 + self.correct3 + self.correct4 + self.correct5 + \
                self.correct6 + self.correct7 + self.correct8 + self.correct9 + self.correct10

        return score

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    screen_name = models.CharField(max_length=20)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
