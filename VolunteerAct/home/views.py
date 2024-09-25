from django.shortcuts import render

from VolunteerAct.categories.models import Category


def home_page(request):
    context = {
        'categories': Category.objects.all()
    }

    return render(request, "home/home_page.html", context=context)