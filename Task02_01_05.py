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
    print(f'Ты ходишь первый {first}, а ты второй {second}')
    return(first, second)
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


#game('al', 'ma')

def bot(num):
    if num > 28 and num <= 2021:
        stride = randint(1, 28)
    else:
        stride = num
    return stride
#print(bot(17))

def ii_bot(count_candies, move):
    move_bot = None 
    if count_candies == 2021:
        move_bot = 20
        return move_bot
    elif count_candies == 2001:
        print('Я не хочу играть')
    else:
        move_bot = 29-move
        return move_bot
#print(ii_bot(1001, 28))