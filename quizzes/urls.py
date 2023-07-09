from django.urls import path
from . import views

urlpatterns = [
     path("", views.home, name="home"),
     path("home", views.home, name="home"),
     path("quizzes", views.quizzes, name="quizzes"),
     path("quizzes/<int:categoryID>/", views.quizzes, name="quizzes"),
     path("newQuiz", views.newQuiz, name="newQuiz"),
     path("quiz/<int:quizID>/", views.quiz, name="quiz"),
     path("leaderboard", views.leaderboard, name="leaderboard"),
     path("profile/<int:userID>/", views.profile, name="profile"),
     path("login", views.login_view, name="login"),
     path("logout", views.logout_view, name="logout"),
     path("register", views.register, name="register"),

     # APIs
     path("getQuizzes", views.getQuizzes, name="getQuizzes"),
     path("getQuizzes/<int:categoryID>", views.getQuizzes, name="getQuizzes"),
     path("getUsers", views.getUsers, name="getUsers")
]