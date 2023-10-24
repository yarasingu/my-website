import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

def generate_user_id():
  table_data = app_tables.amigos.search()
  if table_data:
    return highest_amigos_id+1
  else:
    return 1000
    


def find_highest_amigos_id():
    full_table = app_tables.amigos.search()
    highest_id = 999  
    
    for row in full_table:
        amigos_id = row['amigos_id']
        if amigos_id > highest_id:
            highest_id = amigos_id

    return highest_id

highest_amigos_id = find_highest_amigos_id()

