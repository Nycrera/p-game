import socketio
import mysql
class Player:
  def __init__(self,name,id,points,banned,admin,mod):
    self.name=name
    self.id=id
    self.points=points
    self.banned=banned
    self.admin=admin
    self.mod=mod
  
    
