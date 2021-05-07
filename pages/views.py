from django.shortcuts import render


def about_view(request):
    return render(request, 'index.html')


def change_view(request):
    return render(request, 'change.html')


def search_view(request):
    return render(request, 'search.html')


def explore_view(request):
    return render(request, 'explore.html')
