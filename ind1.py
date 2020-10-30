#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

# 20 вариант
# Дано предложение. Определить, сколько в нем одинаковых соседних букв.

if __name__ == '__main__':
    a = input("Введите предложение: ")
    b = ''
    count = 1
    for i in range(len(a)):
        if a[i] == b:
            count += 1
        else:
            b = a[i]

    print(f"Соседских букв: {count}")