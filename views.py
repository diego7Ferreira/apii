from django.shortcuts import render
from django.http import JsonResponse
import urllib


# Create your views here.

def home(request):
    #Recebe uma url e a palavra a ser contata no site
    siteUrl = request.POST.get('site')
    palavra = request.POST.get('palavra')

    #Armazena todo html do site em forma forma de string 
    html_string = str(urllib.request.urlopen(siteUrl).read())
    
    #Conta a ocorrências da 'palavra' e armagena em um dicionario
    resposta = {'ocorrencias' : html_string.count(palavra)}

    #Retorna a o dicionario como JSON
    return JsonResponse(resposta)