import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def add_feedback(name,email,feedback,score):
  app_tables.feedback.add_row(
  name= name,
  email= email,
  feedback = feedback,
  score = score,
  created = datetime.now()
  )
 