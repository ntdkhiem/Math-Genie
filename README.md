# Math Genie
Simple [slack](https://slack.com) slash command for solving math problems

### Features
* Based on [Wolfram|Alpha APIs](http://products.wolframalpha.com/api/)
* Simple to use
* Python3 support
* Can reply to any __math problems__

### Installation
```git
git clone https://github.com/TopKeingt/Math-Genie
```
or click [here](https://github.com/TopKeingt/Math-Genie/archive/master.zip) to download respository's zip file.

### Requirements 
* [Python 3.x](https://www.python.org/downloads/)

### Preparation
#### Generate The Wolfram App Id
You need to create a wolfram app id (the core of the program to work)
1. Create a wolfram alpha account or sign in [here](https://account.wolfram.com/auth/sign-in)
1. Create an App Id [here](http://developer.wolframalpha.com/portal/myapps/index.html) (only when you signed in)
  1. Click `Get an AppID` on top right and enter your Application Name and Description (can be anything) 
  1. Copy the APPID and paste to `WOLFRAM_APP_ID` in config.ini
#### Generate The Slack Api Token
Because the program will run on Slack so you need to get slack api token to able to communicate. 
##### What is Slack ?
> Slack is a collaboration hub for work, no matter what work you do. It’s a place where conversations happen, decisions are made, and information is always at your fingertips. With Slack, your team is better connected.
1. Go to [api.slack.com](https://api.slack.com)
1. Create a new Slack Applications or use your old Slack App (this project only add one slash command to your bot).
1. Copy __Vertification Token__ and paste to `SLACK_VERTIFICATION_TOKEN` in config.ini
1. Go to __OAuth & Permissions__
  1. Select `Send messages as [app's name]` under __Scopes__ and click __Save Changes__
  1. Click __Install App to Workspace__ on the very top of the page and authorize your app to communicate with your slack's workspace.
  1. When successfully authorized, it will redirected back to your app page. Copy __OAuth Access Token__ and paste to `SLACK_BOT_TOKEN` in config.ini
  
### Usage
Now you will able to run the program with python
