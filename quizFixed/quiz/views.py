from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from quiz.models import Round, Quiz, Answer
from quiz.forms import AnswerForm, UserForm, UserProfileInfoForm, AdminRoundForm

#import scipy.stats as ss
# Create your views here.

def get_scores(quiz_id):

    answers = Answer.objects.filter(quiz_number=quiz_id)
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

def flip_stage(stage):

    if stage == 'qs':
        stage = 'as'
    else:
        stage = 'qs'
    return stage

def get_next_round(round):

    if round < 9:
        next_round = '0' + str(round + 1)
    else:
        next_round = str(round + 1)
    return next_round

def guess_correct(guess, answer):

    if guess != '' and guess.lower().strip() in answer.lower().strip():
        return True
    else:
        return False

def mark_answers(form_data, round):

    answer_list = round.list_answers()

    for i in range(1,11):
        guess = form_data['answer'+str(i)]
        correct_answer = answer_list[i-1]
        form_data.update({'correct'+str(i): guess_correct(guess, correct_answer)})

    return form_data

def index(request):
    return render(request,'quiz/index.html')

@login_required
def quiz_play(request, quiz_id, round_number, stage):

    quiz_id = int(quiz_id)
    round_number = int(round_number)
    quiz = Quiz.objects.filter(quiz_id=quiz_id)[0]
    round = Round.objects.filter(quiz_id=quiz_id,round_number=round_number)[0]
    total_rounds = len(Round.objects.filter(quiz_id=quiz_id))
    if round_number == total_rounds:
        final_round = True
    else:
        final_round = False
    pic_round = round.pic_round
    username = request.user.username
    submitted = False
    q_and_a = {}
    scores = []
    leader = ''

    if stage == 'qs':

        sub_answers = Answer.objects.filter(quiz_number=quiz_id,round_number=round_number,username=username)
        if round_number < 10:
            next_round = '0' + str(round_number)
        else:
            next_round = str(round_number)

        if sub_answers:
            submitted = True
        else:

            if request.method == "POST":

                form_data = request.POST.copy()
                form_data.update({'quiz_number':quiz_id, 'round_number':round_number, 'username':username})
                form_data = mark_answers(form_data, round)

                answers = AnswerForm(data=form_data)
                errors = answers.errors.as_data()
                answers.is_valid()
                answers.save()
                submitted = True

            else:

                answers = AnswerForm()
                q_and_a = answers

    elif stage == 'as':

        round_answers = Answer.objects.filter(quiz_number=quiz_id,round_number=round_number)
        users = [ra.username for ra in round_answers]
        q_and_a = [{'question':round.question1,'answer':round.true_answer1,'picture':round.picture1,'users':users,'correct':[ra.correct1 for ra in round_answers]},
            {'question':round.question2,'answer':round.true_answer2,'picture':round.picture2,'users':users,'correct':[ra.correct2 for ra in round_answers]},
            {'question':round.question3,'answer':round.true_answer3,'picture':round.picture3,'users':users,'correct':[ra.correct3 for ra in round_answers]},
            {'question':round.question4,'answer':round.true_answer4,'picture':round.picture4,'users':users,'correct':[ra.correct4 for ra in round_answers]},
            {'question':round.question5,'answer':round.true_answer5,'picture':round.picture5,'users':users,'correct':[ra.correct5 for ra in round_answers]},
            {'question':round.question6,'answer':round.true_answer6,'picture':round.picture6,'users':users,'correct':[ra.correct6 for ra in round_answers]},
            {'question':round.question7,'answer':round.true_answer7,'picture':round.picture7,'users':users,'correct':[ra.correct7 for ra in round_answers]},
            {'question':round.question8,'answer':round.true_answer8,'picture':round.picture8,'users':users,'correct':[ra.correct8 for ra in round_answers]},
            {'question':round.question9,'answer':round.true_answer9,'picture':round.picture9,'users':users,'correct':[ra.correct9 for ra in round_answers]},
            {'question':round.question10,'answer':round.true_answer10,'picture':round.picture10,'users':users,'correct':[ra.correct10 for ra in round_answers]}]

        scores = get_scores(quiz_id)
        leader = scores[0]['user']
        next_round = get_next_round(round_number)

    else:

        q_and_a = {}

    context = {'quiz_id':quiz_id,
               'quiz_started':quiz.started,
               'round_status':round.round_status,
               'round_number':round_number,
               'next_round':next_round,
               'pic_round':pic_round,
               'submitted':submitted,
               'q_and_a':q_and_a,
               'scores':scores,
               'leader':leader,
               'stage':stage,
               'final_round':final_round,
               'next_stage':flip_stage(stage)}

    return render(request,'quiz/quiz_play.html',context=context)

@login_required
def quiz_admin(request, quiz_id):

    quiz = Quiz.objects.filter(quiz_id=quiz_id)[0]
    rounds = quiz.get_rounds()
    round_forms = [AdminRoundForm(instance=round) for round in rounds]
    submitted = False

    if request.method == "POST":
        form_data = request.POST.copy()
        target_round = Round.objects.filter(quiz_id=quiz_id,round_number=form_data['round_number'])[0]
        round_change = AdminRoundForm(data=request.POST, instance=target_round)
        #errors = answers.errors.as_data()
        round_change.is_valid()
        round_change.save()
        submitted = True
        #raise Exception

    context = {'rounds':round_forms,'submitted':submitted,'quiz_id':quiz_id}

    return render(request,'quiz/quiz_admin.html',context=context)

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
