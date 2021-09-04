# -*- coding: utf-8 -*-
import time
import vk
import vk_api
import requests
import random
from requests import *
from threading import Thread
from vk_api.longpoll import VkLongPoll, VkEventType
import colorama
from colorama import Fore, Back, Style
import os

clear = lambda : os.system('cls')
colorama.init()
valid_pass = "8398-7484-8434-5394"
print(Fore.GREEN + "\n***WELCOME TO FUCKER BOTNET***\n")
print(Fore.YELLOW + "[CONSOLE] ENTER BOTNET PASSWORD: ")
botnet_pass = input("")
if botnet_pass == valid_pass:
    delay = input("[CONSOLE] ENTER BOTNET DELAY: \n")
    clear()

    print('''
$$$$$$$$\ $$\   $$\  $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\  
$$  _____|$$ |  $$ |$$  __$$\ $$ | $$  |$$  _____|$$  __$$\ 
$$ |      $$ |  $$ |$$ /  \__|$$ |$$  / $$ |      $$ |  $$ |
$$$$$\    $$ |  $$ |$$ |      $$$$$  /  $$$$$\    $$$$$$$  |
$$  __|   $$ |  $$ |$$ |      $$  $$<   $$  __|   $$  __$$< 
$$ |      $$ |  $$ |$$ |  $$\ $$ |\$$\  $$ |      $$ |  $$ |
$$ |      \$$$$$$  |\$$$$$$  |$$ | \$$\ $$$$$$$$\ $$ |  $$ |
\__|       \______/  \______/ \__|  \__|\________|\__|  \__| BOTNETv3
                                                            
''')
    print(Fore.YELLOW + '[CONSOLE] FUCKER BOTNET STARTED')
    print(Fore.YELLOW + '[CONSOLE] BOTS LOGS:\n')

    def antikick(token2):
        while True:
            try:
                session = vk_api.VkApi(token=token2) 
                longpoll = VkLongPoll(session)
                vk = session.get_api()
                for event in longpoll.listen():
                    if event.type == VkEventType.CHAT_UPDATE:
                        if event.type_id == 8:
                            x = event.info["user_id"]
                            y = event.chat_id
                            try:
                                vk.messages.addChatUser(
                                chat_id=y,
                                user_id=x
                                )    
                            except vk_api.exceptions.ApiError:
                                print(Fore.RED + '[ERROR] MODULE ANTIKICK {-ADDUSER}')
            except:
                print(Fore.RED + '[ERROR] MODULE ANTIKICK {-UNKNOWN}, TOKEN ' + str(token2))
                time.sleep(2)

    def spam(token1):
        VK_API_VERSION = '5.95'
        asa = open('message.txt',encoding = 'utf-8')
        data1 = asa.read()
        stra = data1
        while True:
            try:
                session1 = vk.Session(access_token = token1)
                api = vk.API(session1, v = VK_API_VERSION)
                longPoll = api.messages.getLongPollServer()
                server, key, ts = 'https://'+longPoll['server'], longPoll['key'], longPoll['ts']
            

        
                while True:

                    longPoll = post('%s'%server, data = {'act': 'a_check',
                                             'key': key,
                                             'ts': ts,
                                             'wait': 25}).json()


                    try:
                        if longPoll['updates'] and len(longPoll['updates']) != 0:
                            for update in longPoll['updates']:
                                if len(update) == 7 and update[0] == 4:

                                    sym = update[6]
                                    if sym[0] == '+':
                                            api.messages.joinChatByInviteLink(link = sym[1:])
                                    if sym[0] == 'b' and sym[1] == 'a' and sym[2] == 'n':
                                        try:
                                            api.account.ban(owner_id = int(sym[3:]))
                                        except:
                                            time.sleep(1)
                                    if sym[0] == '_':
                                        while 1==1:
                                            api.wall.post(owner_id = int(sym[1:]),friends_only = 0,message = stra)
                                            print(Fore.GREEN + '[SUCCESS] POST SENT TO THE WALL')
                                            time.sleep(int(delay))
                                    if update[6] == 'raid' or update[6] == 'start' or update[6] == '.' or update[6] == 'fuck' or update[6] == 'spam' or update[6] == 'FUCKER':
                                        try:
                                            api.messages.editChat(chat_id = update[3] - 2000000000, title = '!FUCKBOTS RAIDS!')
                                            time.sleep(0.5)
                                            a=api.photos.getChatUploadServer(chat_id=update[3] - 2000000000,crop_x=10,crop_y=25)['upload_url']
                                            img = {'photo': ('photo.jpg', open('photo.jpg', 'rb'))}
                                            response = requests.post(a, files=img)
                                            result = json.loads(response.text)['response']
                                            api.messages.setChatPhoto(file=result)
                                            print(Fore.GREEN + '[SUCCESS] TITLE OR PHOTO CHANGED')
                                        except:
                                            print(Fore.RED + '[ERROR] MODULE EDIT_CONFERENCE {-YOU ARE NOT AN ADMINISTRATOR OR THE PHOTO IS INCORRECTLY SPECIFIED}')
                                        time.sleep(random.randint(0,2)+random.random())
                                        try:
                                            while 1==1:
                                                api.messages.send(peer_id = update[3],random_id = 0,message = stra,attachment = "")
                                                print(Fore.GREEN + '[SUCCESS] MESSAGE SEND TO CONFERENCE: ',update[3])
                                                time.sleep(int(delay))
                                        except:
                                            time.sleep(5)
                                            ts = longPoll['ts']
                                    ts = longPoll['ts']
                    except:
                        time.sleep(3)
                        ts = longPoll['ts']
                 
                               
            except:
                print(Fore.RED + '[ERROR] MODULE SPAM {-UNKNOWN}, TOKEN ' + str(token1))




    tokens = len(open('token.txt').readlines())
    f = open('token.txt')
    c = 0
    data = f.read()
    while c != tokens:
        tok = data.split('\n')[c]
        c = c+1
        print(Fore.YELLOW + '[CONSOLE] FUCKERBOT STARTED, NUMBER',c,'-',tok)
        try:
            w = Thread(target = antikick, args = (tok,))
            w.start()
            w = Thread(target = spam, args = (tok,))
            w.start()
        except:
            time.sleep(1)

else:
    print(Fore.RED + "[ERROR] INCORRECT PASSWORD")
    time.sleep(5)
    pass