

def my_handler(event, context):
    # return {"message" : "what's up"}
    dat = event['queryStringParameters']

    try:
      message = 'Hello {} {}!'.format(dat['first_name'],
                                      dat['last_name'])
      # message = 'Hello {} {}!'.format(event['first_name'],
      #                                 event['last_name'])
    except KeyError:
      return {
               'statusCoode': 200,
               'body': str(event)
             }
    return {
             'statusCoode': 200,
             'body': message
           }

    # return {
    #          'message': message
    #        }
