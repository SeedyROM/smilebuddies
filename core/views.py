from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    user = request.user
    return render(request, 'core/dashboard.html', {'user': user})
