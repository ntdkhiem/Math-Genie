import requests
import os
import argparse
import configparser
from urllib.parse import urlencode
from flask import Flask, request
from slackclient import SlackClient

__author__ = 'TopKeingt'
__version__ = '0.0.1'

parser = argparse.ArgumentParser(description='Run the program in [mode]')
parser.add_argument('-p','--production', action='store_true', help="Run the program in production mode")
parser.add_argument('-d','--development', action='store_true', default=True ,help="Run the program in development mode")
args = parser.parse_args()

config = configparser.ConfigParser()
config.read('config.ini')
mode = 'DEVELOPMENT'
if (args.production):
    mode = 'PRODUCTION'

MODE = config[mode]
PORT = MODE.getint('FLASK_PORT', 3000)
DEBUG_MODE = MODE.getboolean('FLASK_DEBUG', True)
SLACK_BOT_TOKEN = MODE.get('SLACK_BOT_TOKEN', ValueError('Please provide a slack_bot_token in config.ini'))
SLACK_VERIFICATION_TOKEN = MODE.get('SLACK_VERIFICATION_TOKEN', ValueError('Please provide a slack_verification_token in config.ini'))
WOLFRAM_APP_ID = MODE.get('WOLFRAM_APP_ID', ValueError('Please provide a wolfram_app_id in config.ini'))

CLIENT = SlackClient(SLACK_BOT_TOKEN)
app = Flask(__name__)


def wolfram_api(query):
    query = urlencode(dict(query=query))[6:]    # encode querystring to url and trims down 'query=' 
    wolfram_url = f'http://api.wolframalpha.com/v2/query?appid={WOLFRAM_APP_ID}&input={query}&output=json'
    result = requests.get(wolfram_url).json()
    if result['queryresult']['success']:
        container = result["queryresult"]["pods"][1]["subpods"]
        res = []
        for subpod_id in range(len(container)):
            res.append(result["queryresult"]["pods"][1]["subpods"][subpod_id]["plaintext"] + '\n')
        return ''.join(res)
    else: 
        raise Exception('Invalid Wolfram App Id')

@app.route("/genie", methods=['POST'])
def wolfram():
    channel = request.form["channel_id"]
    reply = ''
    if request.form["token"] == SLACK_VERIFICATION_TOKEN:
        reply = "*User*: <@{}>\n".format(request.form["user_id"])
        reply += "*Query*: {}\n".format(request.form["text"])
        reply += '*Result*: ' + wolfram_api(request.form["text"])
    else:
        reply = "The token for the slash command doesn't match. Check your script."
    CLIENT.api_call("chat.postMessage", channel=channel, text=reply)
    return ''

if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG_MODE)
