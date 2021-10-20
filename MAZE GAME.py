# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 04:20:15 2020

@author: cirpan
"""
import tkinter as tk

file = input("Select the file of txt your options are 'maze.txt' or 'maze2.txt':")
file = open(file, "r")
                      
class stack: 
  def __init__(self):
    self.n , self.m = map(int, file.readline().split())    
    self.start = list(map(int, file.readline().split()))
    self.end = list(map(int, file.readline().split())) 

    self.MAZE = [] 
    self.visited = []
    
    for i in range(self.n):
      self.MAZE.append(list(file.readline()))
      self.visited.append([0 for i in range(self.m)])       
    
  def depth_first_search(self): #Labirentten çıkışın bulunabilmesi için dfs algoritması kullanıyoruz.
    stack = [self.start]
    while(stack):
      row, column = stack[-1] 
      
      if(stack[-1] == self.end): #Eğer çıkış noktasına geldiysek 
          break # döngüyü durduruyorum
      elif(self.MAZE[row][column] == "*"): 
        stack.pop()        
      # GO UP
      elif(row > 0 and not self.visited[row - 1][column]):
        stack.append([row - 1, column])
      # GO DOWN
      elif(row < self.n - 1 and not self.visited[row + 1][column]): 
        stack.append([row + 1, column])
      # GO RIGHT
      elif(column > 0 and not self.visited[row][column - 1]):
        stack.append([row, column - 1])
      # GO LEFT
      elif(column < self.m - 1 and not self.visited[row][column + 1]):
        stack.append([row, column + 1])
      else: 
        stack.pop()       
      #print(stack) ##stack'e giren çıkan tüm noktalar sırasıyla görülebilir.    
     
      self.visited[row][column] = 1 
         
#Bu satırlar kodun en önemli bölümüdür.
#Ulaşmak için cirpanrafet@gmail.com a mail atın.
      
    for a in range(self.n):
        for b in range(self.m):
            if self.MAZE[a][b] == '.':                  
                self.MAZE[a][b] = '!'
                
    self.form = tk.Tk()
    self.form.title('MAZE GAME SOLUTION')
                       
    for i in range(self.n):
        for j in range(self.m):
            if self.MAZE[i][j] == "*":
               self.label = tk.Label(self.form,relief=tk.RAISED,width=4,height=2,bg="black")
               self.label.grid(row=i,column=j)
            elif self.MAZE[i][j] == "1":
               self.label = tk.Label(self.form,relief=tk.RAISED,width=4,height=2,bg="yellow")
               self.label.grid(row=i,column=j)
            elif self.MAZE[i][j] == "!":
               self.label = tk.Label(self.form,relief=tk.RAISED,width=4,height=2,bg="blue")
               self.label.grid(row=i,column=j) 

    self.form.mainloop()
     
s = stack() #Oluşturulan Class'ı çağırıyoruz
s.depth_first_search() 

for i in range(s.n):
    for j in range(s.m):
      print(s.MAZE[i][j], end = "")
    print()
