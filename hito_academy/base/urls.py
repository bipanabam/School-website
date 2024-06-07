from django.urls import path
from .views import HomePage, CoursePage, GalleryPage, TeacherPage, AboutPage, ContactPage, send_message, NewsPage


urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("course/", CoursePage.as_view(), name="course"),
    path("teachers/", TeacherPage.as_view(), name="teachers"),
    path("gallery/", GalleryPage.as_view(), name="gallery"),
    path("about/", AboutPage.as_view(), name="about"),
    path("contact/", ContactPage.as_view(), name="contact"),
    path("sent/", send_message, name="send_message"),
    path("news/", NewsPage.as_view(), name="news"),
    ]
