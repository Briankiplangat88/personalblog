import urllib.request,json




# def get_blogQuotes():
#     """
#     Function that gets the json response to our url request
#     """
#     get_response = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
#     return get_response

#     import urllib.request,json
def get_blogQuotes():
    get_response=[]
    get_quotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'
    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response=json.loads(get_quotes_data)
        id= str(get_quotes_response['id'])
        quote=str(get_quotes_response['quote'])
        author=str(get_quotes_response['author'])
        new_list=[id,quote,author]
        get_response.append(new_list)
    return get_response[0]