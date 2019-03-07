from gi.repository import Gtk
class Game(Gtk.Window):
  Gtk.Window.___init___(self, title="P-Game")
  self.become_server_button = Gtk.Button(label="Become a server")
  self.connect_confirm_button = Gtk.Button(label="Connect to server")
  self.become_server_button.connect("clicked", self.become_server)
  self.connect_confirm_button.connect("clicked", self.connect_server)
  self.add(self.become_server_button, self.connect_server_button)
  def become_server(self, widget):
    #insert code to accept connections
  def connect_server(self, widget):
    #insert code to connect to ip/domain entered in textfield.

window = Game()
