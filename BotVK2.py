import os
import subprocess
import vk_api
import random
import time
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkApi
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id
import requests
from io import BytesIO


# API-ключ созданный ранее
token = "02d9d1c7172d61be930c18b395a36138a8ed377c161e0b24201022b4a1448562b80317f1df17e84de5b81"
TOKEN = '02d9d1c7172d61be930c18b395a36138a8ed377c161e0b24201022b4a1448562b80317f1df17e84de5b81'
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)
# Работа с сообщениями
longpoll = VkLongPoll(vk)

f = open('EttiURLsFile.txt')

URLget1 = []
URLgeting1 = []
URLget2 = []
URLgeting2 = []

URLvideos = ['https://vk.com/video-173056137_456239457''https://vk.com/video-173056137_456239430','https://vk.com/video-173056137_456239424','https://vk.com/video-173056137_456239400','https://vk.com/video-173056137_456239388','https://vk.com/video-173056137_456239429']

for j in f:
    URLgeting1.append(j)
URLget1 = [i.strip() for i in URLgeting1]



def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0})

def upload_photo(upload, url):
    img = requests.get(url).content
    f = BytesIO(img)

    response = upload.photo_messages(f)[0]

    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']

    return owner_id, photo_id, access_key
def send_photo(vk, peer_id, owner_id, photo_id, access_key):
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.messages.send(
        random_id=get_random_id(),
        peer_id=peer_id,
        attachment=attachment
    )
def main():
    vk_session = VkApi(token=TOKEN)
    vk = vk_session.get_api()
    upload = VkUpload(vk)
    send_photo(vk, PEER_ID, *upload_photo(upload, URL))



# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
        
            # Сообщение от пользователя
            request = event.text
            
            # Каменная логика ответа




            if request == "1":

                number = random.randint(0,41)

                write_msg(event.user_id, "Минутку...")
                print('ID' + str(event.user_id) + ': фото этти номер - ' + str(number))

                PEER_ID = event.user_id


                URL = URLget1[number]


                if __name__ == '__main__':
                    main()








            elif request == "2":

              #  number = random.randint(0,1)

               # write_msg(event.user_id, "Минутку...")
               # print('ID' + str(event.user_id) + ': фото хентай номер - ' + str(number))

                #PEER_ID = event.user_id

                write_msg(event.user_id, "Это команда прямо сейчас находится на стадии теста , и скоро будет работать")

                #URL = URLget2[number]


                #if __name__ == '__main__':
                 #   main()








            elif request == "3":
                number = random.randint(0,4)
                write_msg(event.user_id, URLvideos[number])









            else:
                print ('ID ' + str(event.user_id) + ': ' + request)
                write_msg(event.user_id, "Привет, братик :) \n Вот команды: \n 1 - картинки этти \n 2 - картинки хентай \n 3 - видео")
                