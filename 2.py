from bottle import route, run, request


@route('/')
def hello():

    response = "<html><body><h1>Hello Word!</body></html>"
    return response

@route('/currency')
def get_currency():
    request_input = request.query
    if 'today' in request.query:
        currency_reply = request("<nbu>?")

        return "Today exchange rate is" + currency_reply
    if 'yesterday' in request.query:
        currency_reply = request("<nbu>?")

        return "Today exchange rate is" + currency_reply

    return "Unknown query. Supported queries are /currency?today or currency/yesterday"

if __name__ == '__main__':
    run(port=8000)