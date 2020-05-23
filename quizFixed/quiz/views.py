from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from quiz.models import Round, Quiz, Answer
from quiz.forms import AnswerForm, UserForm, UserProfileInfoForm

#import scipy.stats as ss
# Create your views here.

def get_scores(quiz_id):

    answers = Answer.objects.filter(quiz_id=quiz_id)
    users = set([ra.username for ra in answers])
    scores = []

    for user in users:
        score = 0
        for answer in answers:
            if answer.username == user:
                score += answer.get_round_score()
        scores.append({'user':user,'score':score,'placing':''})

    all_scores = [s['score'] for s in scores]
    all_scores.sort(reverse=True)
    scores_placings = [all_scores.index(x) for x in all_scores]
    scores_zip = zip(all_scores,scores_placings)
    scores_dict = {}
    for tup in scores_zip:
        if tup[0] not in scores_dict:
            scores_dict[tup[0]] = tup[1] + 1

    for score in scores:
        score['placing'] = scores_dict[score['score']]

    return scores

def index(request):
    return render(request,'quiz/index.html')

@login_required
def quiz_play(request, quiz_id):

    quiz = Quiz.objects.filter(quiz_id=quiz_id)[0]
    quiz_status = quiz.status
    round_number = quiz.current_round
    round = Round.objects.filter(quiz_id=quiz_id,round_number=round_number)[0]
    username = request.user.username
    submitted = False
    q_and_a = {}
    scores = []

    if quiz_status == 'WA':

        sub_answers = Answer.objects.filter(quiz_id=quiz_id,round_number=round_number,username=username)

        if sub_answers:

            submitted = True

        else:

            if request.method == "POST":

                form_data = request.POST.copy()
                form_data.update({'quiz_id':quiz})
                form_data.update({'round_number':round_number})
                form_data.update({'username':username})

                if form_data['answer1'].lower() in round.true_answer1.lower():
                    form_data['correct1'] = True
                if form_data['answer2'].lower() in round.true_answer2.lower():
                    form_data['correct2'] = True
                if form_data['answer3'].lower() in round.true_answer3.lower():
                    form_data['correct3'] = True
                if form_data['answer4'].lower() in round.true_answer4.lower():
                    form_data['correct4'] = True
                if form_data['answer5'].lower() in round.true_answer5.lower():
                    form_data['correct5'] = True
                if form_data['answer6'].lower() in round.true_answer6.lower():
                    form_data['correct6'] = True
                if form_data['answer7'].lower() in round.true_answer7.lower():
                    form_data['correct7'] = True
                if form_data['answer8'].lower() in round.true_answer8.lower():
                    form_data['correct8'] = True
                if form_data['answer9'].lower() in round.true_answer9.lower():
                    form_data['correct9'] = True
                if form_data['answer10'].lower() in round.true_answer10.lower():
                    form_data['correct10'] = True

                answers = AnswerForm(data=form_data)
                answers.is_valid()
                answers.save()
                submitted = True

            else:

                answers = AnswerForm(initial={'quiz_id':quiz,'round_number':round_number,'username':username})
                q_and_a = {'round':round,'answers':answers}

    elif quiz_status == 'SA':

        round_answers = Answer.objects.filter(quiz_id=quiz_id,round_number=round_number)
        users = [ra.username for ra in round_answers]
        q_and_a = [{'question':round.question1,'answer':round.true_answer1,'users':users,'correct':[ra.correct1 for ra in round_answers]},
            {'question':round.question2,'answer':round.true_answer2,'users':users,'correct':[ra.correct2 for ra in round_answers]},
            {'question':round.question3,'answer':round.true_answer3,'users':users,'correct':[ra.correct3 for ra in round_answers]},
            {'question':round.question4,'answer':round.true_answer4,'users':users,'correct':[ra.correct4 for ra in round_answers]},
            {'question':round.question5,'answer':round.true_answer5,'users':users,'correct':[ra.correct5 for ra in round_answers]},
            {'question':round.question6,'answer':round.true_answer6,'users':users,'correct':[ra.correct6 for ra in round_answers]},
            {'question':round.question7,'answer':round.true_answer7,'users':users,'correct':[ra.correct7 for ra in round_answers]},
            {'question':round.question8,'answer':round.true_answer8,'users':users,'correct':[ra.correct8 for ra in round_answers]},
            {'question':round.question9,'answer':round.true_answer9,'users':users,'correct':[ra.correct9 for ra in round_answers]},
            {'question':round.question10,'answer':round.true_answer10,'users':users,'correct':[ra.correct10 for ra in round_answers]}]

        scores = get_scores(quiz_id)

    else:

        q_and_a = {}

    context = {'quiz_id':quiz_id,
               'quiz_status':quiz_status,
               'round_number':round_number,
               'submitted':submitted,
               'q_and_a':q_and_a,
               'scores':scores}

    return render(request,'quiz/quiz_play.html',context=context)

@login_required
def quiz_admin(request):
    return

@login_required
def quiz_create(request):
    return

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'quiz/registration.html',
        {'user_form':user_form,
         'profile_form':profile_form,
         'registered':registered})

def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied")

    else:

        return render(request,'quiz/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def user_profile(request):

    changed = False

    if request.method == 'POST':

        profile_form = UserProfileInfoForm(data=request.POST)

        if profile_form.is_valid():

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            changed = True

    else:
        user = dir(request.user)
        profile_form = UserProfileInfoForm({'screen_name':request.user.userprofileinfo.screen_name})

    return render(request, 'quiz/user_profile.html',
                  context={'profile_form':profile_form,'changed':changed})
