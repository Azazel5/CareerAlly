from django.shortcuts import render

def user_view(request):
    return render(request, 'user/user.html')