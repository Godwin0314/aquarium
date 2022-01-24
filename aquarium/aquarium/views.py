from django.shortcuts import render


def fishmain(request):
    return render(request,'fishmain/fish.html')

def betta_fish(request):
    return render(request,'fishmain/betta_fish.html')

def gourami_fish(request):
    return render(request,'fishmain/gourami_fish.html')

def neon_tetra(request):
    return render(request,'fishmain/neon_tetra.html')

def clown_fish(request):
    return render(request,'fishmain/clown_fish.html')
