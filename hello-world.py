from rook.serverless import serverless_rook

import rook

@serverless_rook  
def hello(event, context):
  rook.start()
  print event
  rook.flush()
  return event['data']
