"""
В данной программе реализован простейший пример реализации светофора.
Светофор работает не бесконечно, а имеет некоторе количество повторов.
Повторы регулируются параметрами 'stop'.
"""

import time
import colorama
from colorama import Fore, Back, Style
colorama.init()


class TrafficLight():
    __color = ["red", "yellow", "green", "yellow"]
    color_back = [Back.RED, Back.YELLOW, Back.GREEN, Back.YELLOW]

    def running(self, stop = 2):
        print("Светофор начинает работу!")
        i = 0
        rep = 0
        while rep < stop:
            print(TrafficLight.color_back[i] + Fore.BLACK + TrafficLight.__color[i] + Back.RESET)
            time.sleep(7) if i % 2 == 0 else time.sleep(2)
            i += 1
            if i == 4:
                i = 0
                rep += 1
        print(Fore.RESET)


    def pause(self, stop = 5):
        rep = 0
        while rep < stop:
            print(f"{Fore.BLACK + TrafficLight.color_back[1] + TrafficLight.__color[1] + Back.RESET}")
            time.sleep(2)
            rep += 1


traffic_light_1 = TrafficLight()
traffic_light_1.running()
print("Цикл кончился, светофор встал на паузу.")
traffic_light_1.pause()