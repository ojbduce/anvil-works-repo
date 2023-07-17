from ._anvil_designer import ContactTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Contact(ContactTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_submit_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.text_box_name.text
    email = self.text_box_email.text
    feedback = self.text_area_feedback.text
    score_str = self.drop_down_1.selected_value
    score = int(score_str)
    submit = anvil.server.call('add_feedback', name, email, feedback, score)
    alert("Feedback received. Thanks!")
    return submit

