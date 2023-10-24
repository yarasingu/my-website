from ._anvil_designer import all_usersTemplate
Himport anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class all_users(all_usersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

 

