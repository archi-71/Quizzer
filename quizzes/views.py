from pydoc import describe
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse
import datetime

from .models import User, Category, Quiz, Result, Question, Answer

def home(request):
    return render(request, "quizzes/home.html", {"categories": Category.objects.all()})

def quizzes(request, categoryID=None):
    if categoryID != None:
        category = Category.objects.get(pk=categoryID)
    else:
        category = None
    return render(request, "quizzes/quizzes.html", {
            "categories": Category.objects.all(), 
            "filterCategory": category
        })


def getQuizzes(request, categoryID=None):
    if categoryID != None:
        quizzes = Quiz.objects.filter(category=Category.objects.get(pk=categoryID)).order_by("-timestamp")
    else:
        quizzes = Quiz.objects.all().order_by("-timestamp")

    return JsonResponse([quiz.serialize() for quiz in quizzes], safe=False)


def newQuiz(request):
    if request.method == "POST":
        request.user.quizzesCreated += 1
        category = Category.objects.get(pk=int(request.POST["category"]))
        quiz = Quiz(creator=request.user, 
                    category=category, 
                    name=request.POST["name"], 
                    description=request.POST["description"], 
                    questionNumber = 0,
                    timestamp=datetime.datetime.now())
        quiz.save()
        for key in request.POST:
            data = key.split("-")
            if data[0] == "question":
                question = Question(quiz=quiz, number=int(data[1]), question=request.POST[key])
                question.save()
                quiz.questionNumber += 1
                quiz.save()
            elif data[0] == "answer":
                answer = Answer(number=int(data[1]), answer=request.POST[key], correct=False)
                answer.save()
                question.answers.add(answer)
            elif data[0] == "correct":
                answer.correct = True
                answer.save()

        return HttpResponseRedirect(reverse("quizzes"))
    return render(request, "quizzes/newQuiz.html", {"categories": Category.objects.all()})


def quiz(request, quizID):
    quiz = Quiz.objects.get(pk=quizID)
    questions = Question.objects.filter(quiz=quiz)
    results = {}
    score = 0
    percentage = 0

    if request.method == "POST" and request.session['canPostResults']:
        request.session['canPostResults'] = False
        if request.user.is_authenticated:
            request.user.quizzesCompleted += 1
        for key in request.POST:
            if key.isnumeric():
                question = questions.get(number=int(key))
                answer = question.answers.get(number=int(request.POST[key]))
                results[question.number] = {"result": answer.correct}
                if answer.correct:
                    score += 1
                    if request.user.is_authenticated:
                        request.user.correctAnswers += 1
                        request.user.save()
                elif request.user.is_authenticated:
                    request.user.incorrectAnswers += 1
                    request.user.save()
                for i in range(1, len(question.answers.all())+1):
                    if question.answers.get(number=i).correct:
                        results[question.number][i] = "correct"
                    elif answer.number == i:
                        results[question.number][i] = "incorrect"
                    else:
                        results[question.number][i] = "none"
        percentage = round((score/len(questions)) * 1000) / 10
        if request.user.is_authenticated:
            result = Result(user=request.user, quiz=quiz, percentage=percentage)
            result.save()

            allResults = Result.objects.filter(user=request.user)
            if request.user.quizzesCompleted != 0:
                averages = {}
                total = 0
                for result in allResults:
                    quiz = result.quiz
                    if quiz.category.name in averages:
                        averages[quiz.category.id][0] += 1
                        averages[quiz.category.id][1] += result.percentage
                    else:
                        averages[quiz.category.id] = [1, result.percentage]
                    total += result.percentage

                request.user.averageScore = round((total / request.user.quizzesCompleted) * 10) / 10

                bestAverage = -1
                worstAverage = 101
                for category in averages:
                    average = averages[category][1] / averages[category][0]
                    if (average) > bestAverage:
                        bestAverage = average
                        bestCategory = category
                    if (average) < worstAverage:
                        worstAverage = average
                        worstCategory = category
                request.user.bestCategory = Category.objects.get(pk=bestCategory)
                request.user.worstCategory = Category.objects.get(pk=worstCategory)
                request.user.save()
    else:
        request.session['canPostResults'] = True

    return render(request, "quizzes/quiz.html", {
        "categories": Category.objects.all(),
        "quiz":quiz,
        "questions":questions,
        "results": results,
        "score": f"{score} / {len(questions)}",
        "percentage": percentage
    })


def leaderboard(request):
    return render(request, "quizzes/leaderboard.html", {"categories": Category.objects.all(), })


def getUsers(request):
    users = User.objects.all()
    return JsonResponse([user.serialize() for user in users], safe=False)


def profile(request, userID):
    profile = User.objects.get(pk=userID)
    return render(request, "quizzes/profile.html", {
        "categories": Category.objects.all(), 
        "profile": profile
})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "quizzes/login.html", {
                "message": "Invalid username and/or password.",
                "categories": Category.objects.all()
            })
    else:
        return render(request, "quizzes/login.html", {"categories": Category.objects.all()})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "quizzes/register.html", {
                "message": "Passwords must match.",
                "categories": Category.objects.all()
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, )
            user.save()
        except IntegrityError:
            return render(request, "quizzes/register.html", {
                "message": "Username already taken.",
                "categories": Category.objects.all()
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "quizzes/register.html", {"categories": Category.objects.all()})