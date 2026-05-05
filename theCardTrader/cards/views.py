from django.shortcuts import render

# Create your views here.



def cartas(request):
    return render(request,'cards/cartas.html')


def cartas_detalhamento(request):
    return render(request,'cards/cartas_detalhes.html')

def decks_detalhamento(request):
    return render(request,'cards/decks_detalhes.html')