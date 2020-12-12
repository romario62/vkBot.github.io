# -*- coding: utf-8 -*- 
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import time

token = "your_token"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
global response
global id
def roll():
    shot = random.randint(0,100)
    print(shot)
    return shot
d = roll()
print(int(d))

def ring ():
    s = 1
    while s == 1 :
        if d < 71:
            x = u'Поздравляю, твой приз - купон на 300 рублей. Узнай у менеджера как забрать его.'
        elif d > 70 and d < 96:
            x = u'Поздравляю, твой приз - купон на 500 рублей. Узнай у менеджера, как забрать его.'
        elif d > 94:
            x = u"Поздравляем! \n Вы выиграли букет «Комплимент» \n Получить его Вы сможете при следующем заказе, показав данное сообщение"
        s = 2       
    return x

def sms(user_id, a, m):
    vk_session.method('messages.send', {'user_id':user_id,'message':m, 'attachment':a, 'random_id':0})

def attach():
    attachment = None
    while attachment == None:
        if d < 71:
            attachment = 'photo-133710955_456239536'
        elif (d > 70) and (d < 96):
            attachment = 'photo-133710955_456239535'
        elif d > 95:
            attachment = 'photo-133710955_456239537'
        print(attachment)
    return attachment

def search(id):
        n = 0
        with open('id.txt') as p:
            searchvar = str(id)+'\n'
            print(searchvar + ' tut')
            for line in p:
                if searchvar in line:
                    n = 1
                    f.close()
        print(n)
        return n

try:
    while True:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                id = event.user_id
                d = roll()
                print(int(d))
                print(event.user_id)
                response = event.text.lower()
                if event.from_user and not (event.from_me):
                    if response == "#крафт_лотерея":
                        if search(id) == 0:
                            sms(event.user_id,m= u"Ты хочешь попытать свою удачу в Крафт-лотерее? \n Напиши да, если хочешь.",a= None)
                            flag1 = 1
                            f = open('id.txt','a')
                            f.write(str(event.user_id) + '\n')
                            f.close()
                        elif search(id) == 1:
                            sms(event.user_id, m=u"Извини, но у тебя закончились попытки.", a = None)
                    elif ("да" in response or "хочу" in response or "участвую" in response) and (flag1 == 1):
                        sms(event.user_id,m = ring(),a = attach())
                        flag1 = 0
                    elif ("нет" in response or "не хочу" in response) and flag1 ==1:
                        sms(event.user_id, m=u"Поняли! Хорошего дня!", a=None)
                        flag1 = 0
except Exception as l:
    print("Something wrong!")
    f = open('logs.txt','a')
    f.write(str(l) + '\n')
    f.close()       
    
