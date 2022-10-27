# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг
# после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более 
#чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько 
#конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import *
import os

player_1 = input('Игрок №1: ')
player_2 = input('Игрок №2: ')

def lot(play_1, play_2):
    lots = randint(1, 2)
    if lots == 1:
        first = play_1
        second = play_2
    else:
        first = play_2
        second = play_1
    return f'Ты ходишь первый {first}, а ты второй {second}'

print(lot(player_1, player_2))

def game(play_1, play_2):
    count_candies = 2021
    max_move = 28
    count = 0
    while count_candies > 0:
        if count == 0:
            move = int(input (f'Твой ход {play_1}: ' ))
            if move > max_move or move < 0:
                move = int(input('Уверен? Попробуй ещё раз: '))
            count_candies -= move
        if count_candies > 0:
            print(f'Осталось {count_candies} конфет')
            count = 1
        else:
            print(f'Ты выиграл {play_1}!')
        if count == 1:
            move = int(input (f'Теперь твой ход {play_2} : ' ))
            if move > max_move or move < 0:
                move = int(input('Уверен? Попробуй ещё раз: '))
            count_candies -= move
        if count_candies > 0:
            print(f'Осталось {count_candies} конфет')
            count = 0
        else:
            print(f'Ты выиграл {play_2}!')

game('al', 'ma')

