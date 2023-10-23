from ._anvil_designer import homeTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class home(homeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    

  def home_link_click(self, **event_args):
    open_form('home')

  def SignUp_link_click(self, **event_args):
    open_form('sign_up')

  def login_link_click(self, **event_args):
    open_form('login')

  def about_link_click(self, **event_args):
    open_form('about')

    



