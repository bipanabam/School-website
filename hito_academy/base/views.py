from django.shortcuts import render, HttpResponse, reverse
from django.views.generic import TemplateView

import smtplib

MY_EMAIL = "your-email"
MY_PASSWORD = "email-password"


# Create your views here.
class HomePage(TemplateView):
    template_name = "home.html"


class CoursePage(TemplateView):
    template_name = "courses.html"


class TeacherPage(TemplateView):
    template_name = "teachers.html"


class GalleryPage(TemplateView):
    template_name = "gallery.html"


class ContactPage(TemplateView):
    template_name = "contact.html"


def send_message(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Sending the written message
        try:
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=email, to_addrs=MY_EMAIL, msg=f"Subject:{subject}\n\nFull Name: {name}"
                                                                        f"\nEmail: {email}\nMessage: {message}")
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error: {e}")
            return HttpResponse(f'Error: {e}')
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')


class NewsPage(TemplateView):
    template_name = "news.html"


class AboutPage(TemplateView):
    template_name = "about.html"
