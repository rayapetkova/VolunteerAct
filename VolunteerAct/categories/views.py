from django.shortcuts import render
from django.views.generic import DetailView

from VolunteerAct.categories.models import Category


class CategoryDetailsView(DetailView):
    model = Category
    template_name = 'categories/category_page.html'
