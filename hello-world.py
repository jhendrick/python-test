from rook.serverless import serverless_rook

import rook
rook.start(token="987cb968bd451072e2fae4ec9a3afa3741261cb58813059d1aa4daf122c9be49", labels={"env":"kubeless"})

@serverless_rook  
def hello(event, context):
  print event
  return event['data']
