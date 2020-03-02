import os
import subprocess
import vk_api
import random
import time
from vk_api.longpoll import VkLongPoll, VkEventType

stat = 0


status1 = 0
status2 = 0
status3 = 0

users = []
users_money = []

part = 0

manNUM = 0


# API-ключ созданный ранее
token = "be8178cc475050be3a9b6ecfab3dadaa0e58526727e5b9d51f0584f2c683eddc2f677770797be444e4cf7"
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)
# Работа с сообщениями
longpoll = VkLongPoll(vk)
#URL
URL = 'https://static.zerochan.net/Hatsune.Miku.full.1685469.jpg'

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0})


# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
        
            # Сообщение от пользователя
            request = event.text
            
            # Каменная логика ответа


            def fun ():
                for i in range(len(users)):
                    if str(users[i]) == str(event.user_id):
                        ID = i
                        return ID


            if request == "Начать":
                status1 = 1
                status2 = 0
                status3 = 0

                ID_num = 666
                for i in range(len(users)):
                    if str(users[i]) == str(event.user_id):
                        ID_num = i
    
                if ID_num == 666:
                    #здесь будет часть кода которая добавляет новый айди в конец листа
                    users.append(str(event.user_id))
                    users_money.append(5000)
                

                write_msg(event.user_id, "Вы начали игру!")
                write_msg(event.user_id, "Чтобы посмотреть ваш бюджет напишите - Бюджет")
                write_msg(event.user_id, "Чтобы сыграть в рулетку чисел напишите - Загадать")








            elif request == "Бюджет" and status1 == 1:
                status2 = 0
                status3 = 0
                write_msg(event.user_id, users_money[fun()])





            elif request == "Загадать" and status1 == 1:
                status2 = 1
                status3 = 0
                write_msg(event.user_id, "Сделайте ставку, ваш бюджет:")
                write_msg(event.user_id, users_money[fun()])




            elif status2 == 1:
                status2 = 0
                if int(request) <= users_money[fun()]:
                    part = int(request)
                    write_msg(event.user_id, "Загадайте число от 1 до 10")
                    status3 = 1
                    status2 = 0
                   


            elif status3 == 1:
                if (int(request) < 1 or int(request) > 10):
                    write_msg(event.user_id, "Ты тупой? Число от 1 до 10")
                manNUM = int(request)
                rand = random.randint(1, 10)
                if rand == manNUM:
                    users_money[fun()]+= part*5
                    part = 0
                    write_msg(event.user_id, "Вы выиграли, ваша ставка прибавилась к вашему бюджету в пятерном эквиваленте")
                    status3 = 0
                if rand != manNUM:
                    users_money[fun()]-= part
                    part = 0
                    write_msg(event.user_id, "Вы проиграли, вы указали неверно число. Верное число - ")
                    write_msg(event.user_id, rand)
                    status3 = 0







            elif request == "/off":
                file.close()
                print('Подключение админа, отключение сервера...')
                write_msg(event.user_id, 'Сервер отключается')
                exit()

            else:
                status1 = 0
                status2 = 0
                status3 = 0
                write_msg(event.user_id, "Привет, чтобы начать напиши: Начать")

                
