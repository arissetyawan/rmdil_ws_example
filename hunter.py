import requests
import json
from flask import Flask, render_template

app = Flask('hunter')
api_key = 'a30daebb1d5972aa0231f7a440a40540b9bb28f2'

@app.route('/')
def index():
    url = 'https://api.hunter.io/v2/domain-search?domain=stripe.com&api_key='+api_key
    # ensuring url are concated correctly with api key
    print(url)
    response = requests.get(url)
    headers = response.headers
    text = response.text
    original_json = response.json()
    print(headers)  
    print(text)  
    print(json)  

    # if you are using POST
    # response = requests.post(url, data={'parameter1': 'bla bla', 'parameter1': 'bla'})
    # we call api/ws json then we display it into html 

    # for example i need to get the emails and display it into html
    emails = original_json['data']['emails'][0]['value'] #{{json.dumps(original_json['data']['emails'], indent=4, sort_keys=True)}}
    return render_template('index.html', original_json=original_json, emails= emails)

if __name__ == '__main__':
    app.run()