# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 21:20:15 2020

@author: Rafet
 
"""

import tkinter as tk
f = input("Enter the 'maze.txt' or 'maze2.txt': ")
fileObj = open(f, "r")           
        
class stack: 
  def __init__(self):
    
    self.firstLine = list(map(int, fileObj.readline().strip().split()))
    self.rows = self.firstLine[0]
    self.col = self.firstLine[1]
    
    
    self.end = list(map(int, fileObj.readline().split()))
    self.start = list(map(int, fileObj.readline().split())) 

    self.maze = [] 
    self.visited = []
    
    for i in range(self.rows):
      self.maze.append(list(fileObj.readline().strip("\n")))
      self.visited.append([0 for i in range(self.col)])       
    #print(maze)
    #print(visited)
  def solve_maze(self):
    stack = [self.start]
    while(stack):
      row, column = stack[-1] 
    
      if(stack[-1] == self.end):
          break 
      elif(self.maze[row][column] == "*"): 
        stack.pop()
        
      # control up
      elif(row > 0 and not self.visited[row - 1][column]):
        stack.append([row - 1, column])
      # control down
      elif(row < self.rows - 1 and not self.visited[row + 1][column]): 
        stack.append([row + 1, column])
      # control rıght
      elif(column > 0 and not self.visited[row][column - 1]):
        stack.append([row, column - 1])
      # control left
      elif(column < self.col - 1 and not self.visited[row][column + 1]):
        stack.append([row, column + 1])
      else: 
        stack.pop()        
          
      self.visited[row][column] = 1 


    while(stack):
      row , column = stack[-1]
      self.maze[row][column] = "1"
      stack.pop()
      

      self.form = tk.Tk()

      for k in range(self.rows):
          for d in range(self.col):
              if self.maze[k][d] == "1":
                    self.label = tk.Label(self.form,relief=tk.RAISED,width=2,height=1,bg="red")        
                    self.label.grid(row=k,column=d)
                    #red is true way
              elif self.maze[k][d] == "*":
                    self.label = tk.Label(self.form,relief=tk.RAISED,width=2,height=1,bg="black")        
                    self.label.grid(row=k,column=d)
                    # black is wall
              elif self.maze[k][d] == "!":
                    self.label = tk.Label(self.form,relief=tk.RAISED,width=2,height=1,bg="yellow")        
                    self.label.grid(row=k,column=d) 
                    # yellow is wrong way
      self.form.mainloop()
      
      
      
      for i in range(self.rows):
          for j in range(self.col):
              if self.maze[i][j] == '.':                  
                  self.maze[i][j] = '!'
      

s = stack() 
s.solve_maze() 

for i in range(s.rows):
    for j in range(s.col):
       print(s.maze[i][j], end = "")
    print()

