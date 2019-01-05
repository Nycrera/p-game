import socketio
import mysql
class Player:
  def __init__(self,name,id,points):
    self.name=name
    self.id=id
    self.points=points
