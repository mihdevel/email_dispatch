from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Email
import hashlib
import smtplib



def unsubscribe_form(request):
  return render(request, 'email_dispatch/unsubscribe_form.html')


def get_hash_with_email(email):
  return hashlib.sha256(bytes(email + str(date.today()), encoding='utf-8')).hexdigest()


def unsubscribe_send(request):
  email = request.POST['email']
  
  if not Email.objects.filter(email=email):
    return HttpResponse('{}, к счастью, а может и нет, но Вы не подписаны на нашу рассылку!'.format(email))

  hash = get_hash_with_email(email)
  url_unsubscribe = 'http://127.0.0.1:8000/unsubscribe?email={}&hash={}'.format(email,hash)
  
  text_email = 'Для того, чтобы отписаться от рассылки перейдите по ссылке\n' \
       '<a href"{}">{}</a>'.format(url_unsubscribe, url_unsubscribe)
  
  # С отправкой письма на email я еще не разобрался,
  # но она должна осуществляться здесь!

  text_return = '{}, мы отправили на вашу эл. почту письмо для подтверждения отписки от рассылки! ' \
                'Пожалуйста, проверьте её!'
  return HttpResponse(text_return.format(email))


def unsubscribe(request):
  email = request.GET['email']
  hash_input =  request.GET['hash']
  my_hash = get_hash_with_email(email)
  
  if hash_input != my_hash:
    return HttpResponse('Ой ошибочка, нами получен не правильный хеш, попробуйте заново отписаться!'.format(email))
  
  email_checked = Email.objects.filter(email=email)

  if not email_checked:
    return HttpResponse('К счастью, а может и нет, но адрес эл. почты "{}" не подписан на нашу рассылку!'.format(email))
  
  email_checked.delete()
  return HttpResponse('{}, спасибо, Вы успешно отписались от нашей рассылки!'.format(email))
