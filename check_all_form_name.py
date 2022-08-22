# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 16:52:40 2022

@author: FPG01
"""

import win32gui

import win32con

hWndList = []

win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList)

temp = []
for hwnd in hWndList:

    clsname = win32gui.GetClassName(hwnd)
    
    title = win32gui.GetWindowText(hwnd)
    temp.append(title)
    
temp = list(set(temp))
