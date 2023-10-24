import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

def generate_user_id():
  full_table = app_tables.amigos.search()
  for row in full_table:
    print(row['amigos_id'])



generate_user_id()