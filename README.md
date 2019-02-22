# Math Genie :octocat: 
Simple [slack](https://slack.com) slash command for solving math problems

## Features :fire:

* Based on [Wolfram|Alpha APIs](http://products.wolframalpha.com/api/)
* Simple to use
* Python3 support
* Can reply to any __math problems__

## Requirements :hammer_and_pick:

* [Python 3.x](https://www.python.org/downloads/)

## Installation :wrench:

```git
git clone https://github.com/TopKeingt/Math-Genie
```
or click [here](https://github.com/TopKeingt/Math-Genie/archive/master.zip) to download respository's zip file.
```
python -m pip install -r requirements.txt
```


## Prerequisite :hammer:

#### Generate The Wolfram App Id
You need to create a wolfram app id (the core of the program to work)
1. Create a wolfram alpha account or sign in [here](https://account.wolfram.com/auth/sign-in)
1. Create an App Id [here](http://developer.wolframalpha.com/portal/myapps/index.html) (only when you signed in)
    1. Click `Get an AppID` and enter your Application Name and Description
    ![screenshot-1](https://user-images.githubusercontent.com/25674728/52746101-c6584780-2fae-11e9-86ac-55644280857f.png)
    1. Copy the APPID and paste to `WOLFRAM_APP_ID` in config.ini
    ![screenshot-3](https://user-images.githubusercontent.com/25674728/52746130-d07a4600-2fae-11e9-83e6-ed0c9a668f83.png)
#### Generate The Slack Api Token
Because the program will run on Slack so you need to get slack api token to able to communicate. 
##### What is Slack ? :pencil:  
> Slack is a collaboration hub for work, no matter what work you do. It’s a place where conversations happen, decisions are made, and information is always at your fingertips. With Slack, your team is better connected.
1. Go to [api.slack.com](https://api.slack.com)
1. Create a new Slack Applications or use your old Slack App (this project only add one slash command to your bot).
1. Copy __Vertification Token__ and paste to `SLACK_VERTIFICATION_TOKEN` in config.ini
    ![screenshot-4](https://user-images.githubusercontent.com/25674728/52746136-d4a66380-2fae-11e9-8317-7b03eade40ce.png)
1. Go to __Slash Commands__
    1. Click __Create New Command__ and fill out the form then save.
      ![screenshot-7](https://user-images.githubusercontent.com/25674728/52746825-74b0bc80-2fb0-11e9-90dd-10ae73ace4c5.png)
1. Go to __OAuth & Permissions__
    1. Select `Send messages as [app's name]` under __Scopes__ and click __Save Changes__
    
    ![screenshot-5](https://user-images.githubusercontent.com/25674728/52746154-d96b1780-2fae-11e9-83f6-40d34784b7c7.png)
    1. Click __Install App to Workspace__ on the very top of the page and authorize your app to communicate with your slack's workspace.
    1. When successfully authorized, it will redirected back to your app page. Copy __OAuth Access Token__ and paste to `SLACK_BOT_TOKEN` in config.ini.
    
    ![screenshot-6](https://user-images.githubusercontent.com/25674728/52746158-db34db00-2fae-11e9-933a-f5d08272e0bc.png)
  
## Usage :plate_with_cutlery:

Now you will able to run the program with python
###### :exclamation: Any missing value in config.ini will break the program. Please follow the instruction above to fill out the configuration.
The example of what *config.ini* should look like:
![code](https://user-images.githubusercontent.com/25674728/53217629-ba136080-3626-11e9-8d12-add96ee972f1.png)
How to run ?
```
$ python main.py --help
usage: main.py [-h] [-p] [-d]

Run the program in [mode]

optional arguments:
  -h, --help         show this help message and exit
  -p, --production   Run the program in production mode
  -d, --development  Run the program in development mode
```
example: 
```
$ python main.py --development
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 232-100-363
 * Running on http://127.0.0.1:3000/ (Press CTRL+C to quit)
```

## Notice :exclamation:
since slack's app doesn't allow slash commands to use local url like `http://127.0.0.1:3000` as __Request Url__ please use [ngrok](https://ngrok.com/) to generate public url.
#### Example Usage
```
$ ngrok http 5000
ngrok by @inconshreveable                                                                               (Ctrl+C to quit)

Session Status                online
Account                       TopKeingt (Plan: Free)
Version                       2.2.8
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://30081a1a.ngrok.io -> localhost:3000
Forwarding                    https://30081a1a.ngrok.io -> localhost:3000

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```
and use `http://[ngrok's id].ngrok.io` as __Request Url__

## Pull requests are welcome :mag_right:
###### Video demonstration coming soon
