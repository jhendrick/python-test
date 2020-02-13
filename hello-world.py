from rook.serverless import serverless_rook

@serverless_rook  
def hello(event, context):
  print event
  return event['data']
