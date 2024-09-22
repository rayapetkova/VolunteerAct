from django.shortcuts import render


def category_page(request, pk):
    return render(request, 'categories/category_page.html')