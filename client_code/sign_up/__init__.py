from ._anvil_designer import sign_upTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class sign_up(sign_upTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def signup_home_link_click(self, **event_args):
    open_form('home')
    

  def signup_submit_click(self, **event_args):
    full_name = self.full_name_text.text
    mobile_no = self.mobile_no_text.text
    email = self.emmail_text.text
    dob = self.dob_date.date
    gender = self.dropdown_for_gender.selected_value
    photo_blob = self.photo_uploader_file.file
    anvil.server.call('add_amigo', full_name, mobile_no, email, dob, gender, photo_blob)
    alert("you data was submit sucessfully")
    open_form('home')

