#!/usr/bin/python

n = int(input())
for i in range(0, n):
    row = input().strip()
    for j in range(0, n):
        if row[j] == 'm':
            robot_x = j
            robot_y = i
        if row[j] == 'p':
            princess_x = j
            princess_y = i
            
for i in range(0, abs(robot_x - princess_x)):
    if princess_x > robot_x:
        print("RIGHT")
    else:
        print("LEFT")
        
for i in range(0, abs(robot_y - princess_y)):
    if princess_y > robot_y:
        print("DOWN")
    else:
        print("UP")