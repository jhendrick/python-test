from rook.serverless import serverless_rook

@serverless_rook  
def hello(event, context):
  from rook import auto_start
  print event
  rook.flush()
  return event['data']
