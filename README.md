# py_incoming_slack

## Description

* This Python module post to Channel/Groups in Slack.
* Use 'Incoming WebHooks' in Slack.
* Do not require to make users post only.

## Required module

* requests
* json

## Installation

### Get Webhook URL

1. Access to [https://my.slack.com/services/new/incoming-webhook](https://my.slack.com/services/new/incoming-webhook)
2. Choose a channel into "Post to Channel" pulldown list what you want to post massage.
3. After choose a channel, Click "Incoming WebHooks Integration".
4. You Copy URL into "Webhook URL". 
EX. `https://hooks.slack.com/services/xxxxxxxxx/xxxxxxxxxx/xxxxxxxxxxxxxxxxx`

## Usage

### Import module

```
>>> import incoming_slack
```

### Preliminary preparation

```
incomming_slack()
```

#### Parameter

* Required
	* token_url
	* user_name
* Optional
	* icon

#### Ex

```
>>> slack_instance = incomming_slack(token_url = 'https://hooks.slack.com/services/xxxxxxxxx/xxxxxxxxxx/xxxxxxxxxxxxxxxxx', user_name = 'python_bot')
```

you want to use emoji icon,

```
>>> slack_instance = incomming_slack(token_url = 'https://hooks.slack.com/services/xxxxxxxxx/xxxxxxxxxx/xxxxxxxxxxxxxxxxx', user_name = 'python_bot', icon=":ghost:")
```

you want to use image icon,

```
>>> slack_instance = incomming_slack(token_url = 'https://hooks.slack.com/services/xxxxxxxxx/xxxxxxxxxx/xxxxxxxxxxxxxxxxx', user_name = 'python_bot', icon="http://hogehoge/hoge.png")
```

### Post message

```
.send()
```

#### Parameter

* Required
	* message
* Optional
	* title
	* color (require title parameter)

#### Ex

```
>>> slack_instance.send(message = 'send message')
```

You can choice color parameter 'good', 'warning', 'danger' or hex color code(ex:'#36a64f').

```
>>> slack_instance.send(message = 'send message', title = 'title param', color = 'good')
```

### Shell usage

```
$ ./py_incoming_slack.py -h
usage: untitled.py [-h] -t TOKEN_URL -u USER_NAME -m MESSAGE [-i ICON]
                   [-T TITLE] [-c COLOR]

This script send message for Slack.

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN_URL, --token-url TOKEN_URL
                        You get Webhook URL from
                        https://my.slack.com/services/new/incoming-webhook
  -u USER_NAME, --user-name USER_NAME
                        User name for writing message.
  -m MESSAGE, --message MESSAGE
                        Send detail message body.
  -i ICON, --icon ICON  Use emoji, like ":ghost:". Use image file, like
                        "http://hogehoge/hoge.png"
  -T TITLE, --title TITLE
                        Send detail message body.
  -c COLOR, --color COLOR
                        color parameter "good", "warning", "danger" or hex
                        color code(ex:"#36a64f"). This parameter require to
                        add title parameter 
$ ./py_incoming_slack.py \
-t https://hooks.slack.com/services/xxxxxxxxx/xxxxxxxxxx/ \
-u Python_ghost \
-m "test message" \
-i :ghost: \
-T "Title value" \
-c good
```