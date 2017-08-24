# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 12:45:01 2017

@author: Rohan Bapat
"""



import random 
#Create 3 objects (door) out of which 1 randomly contains value 1 (car), while 2 objects contain randomly 0 (goat) 
def create_doors():
    ls = [0,0,1]
    random.shuffle(ls)
    return ls

def user_select_door():
    selected = random.randint(0,2)
    return selected

def reveal_door(doors,selected):    
    if doors[selected] == 1:
        not_selected = [index for index,value in enumerate(doors) if index!=selected]
        revealed = not_selected[random.randint(0,1)]
        return revealed
    else:
        return 3-selected-doors.index(1)   

def switch_option1():
    selected = 1
    return selected

def switch_option2(selected, revealed):
    switch = random.randint(0,1)
    if switch==1:
        selected = 3-selected-revealed    
    return selected

def win_prob(doors,selected):
    if doors[selected] == 1:
        return (selected,1)
    else:
        return (selected,0)

n_iter = int(input("Enter the number of iterations required: "))

did_not_switch_win = 0 
switch_win = 0

for i in range(n_iter):    
    doors = create_doors()
    selected = user_select_door()
    revealed = reveal_door(doors,selected)
    new_selected = switch_option2(selected, revealed)
    win_loss = win_prob(doors, new_selected)
    if(win_loss[0]==0):
        did_not_switch_win +=1
    else:
        switch_win += 1

print("Won when did not switch: %d\nWon when switched: %d"%(did_not_switch_win, switch_win))
    



    
    