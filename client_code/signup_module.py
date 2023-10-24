import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

def generate_user_id():
  full_table = app_tables.amigos.search(tables.order_by("amigos_id" ,ascending=False))
  print(full_table["amigos_id"][0])


generate_user_id()