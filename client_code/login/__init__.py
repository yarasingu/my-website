from ._anvil_designer import loginTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class login(loginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def login_submit_click(self, **event_args):
    open_form('home')

  def signup_home_link_click(self, **event_args):
    open_form('home')


