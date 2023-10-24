import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from . import signup_module
from anvil import BlobMedia
# them with @anvil.server.callable.

@anvil.server.callable
def add_amigo(full_name, mobile_no, email, dob, gender, photo_blob):
  app_tables.amigos.add_row(amigos_id=signup_module.generate_user_id(),
                            full_name=full_name,
                            mobile_no=mobile_no,
                            email=email,
                            dob=dob,
                            gender=gender,
                            photo=photo_blob)





