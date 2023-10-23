import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


def generate_user_id():
  user_table = app_tables.amigos
  max_user_id = user_table.search(tables.order_by("amigos_id", ascending=False))
  if max_user_id and len(max_user_id) > 0 and 'amigos_id' in max_user_id[0]:
    next_user_id = max_user_id[0]['amigos_id'] + 1
  else:
    next_user_id = 1000
  return next_user_id