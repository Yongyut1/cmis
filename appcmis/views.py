from django.shortcuts import render

def pm_view(request):
    return render(request, 'appcmis/pm_view.html')

def pm_view_2(request):
    return render(request, 'appcmis/pm_view_2.html')

def bpd_view(request):
    return render(request, 'appcmis/bpd_view.html')

def aya_view(request):
    return render(request, 'appcmis/aya_view.html')

def s0_view(request):
    return render(request, 'appcmis/s0_view.html')