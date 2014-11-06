#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import argparse

class pyIncomingSlack:
    def __init__(self, token_url, user_name, icon = ''):
        self.token_url = token_url
        self.user_name = user_name
        self.icon      = icon
    def send(self, message, title = '', color = ''):
        params = {'username' : self.user_name}
        if color != '':
            params['color'] = color
        if title != '':
            fields = {
                'title'  : title
                ,'value' : message
            }
            params['fallback'] = message
            params['fields'] = '[' + json.dumps(fields) + ']'
        else:
            params['text'] = message
        try:
            if self.icon[0] == ':':
                icon_key = 'icon_emoji'
            else:
                icon_key = 'icon_url'
            params[icon_key] = self.icon
        except:
            pass
        params = json.dumps(params)
        params = params.replace('"[', '[')
        params = params.replace(']"', ']')
        params = params.replace('\\', '')
        response = requests.post(self.token_url, data = params)
        return response

def main():
    argument_parser = argparse.ArgumentParser(description='This script send message for Slack.')
    argument_parser.add_argument('-t', '--token-url', type=str, required=True, help='You get Webhook URL from https://my.slack.com/services/new/incoming-webhook')
    argument_parser.add_argument('-u', '--user-name', type=str, required=True, help='User name for writing message.')
    argument_parser.add_argument('-m', '--message'  , type=str, required=True, help='Send detail message body.')
    argument_parser.add_argument('-i', '--icon'     , type=str, default='', help='Use emoji, like ":ghost:". Use image file, like "http://hogehoge/hoge.png"')
    argument_parser.add_argument('-T', '--title'    , type=str, default='', help='Send detail message body.')
    argument_parser.add_argument('-c', '--color'    , type=str, default='', help='color parameter "good", "warning", "danger" or hex color code(ex:"#36a64f"). This parameter require to add title parameter')
    args = vars(argument_parser.parse_args())
    token_url = args['token_url']
    user_name = args['user_name']
    message   = args['message']
    icon      = args['icon']
    title     = args['title']
    color     = args['color']
    if icon != '':
        slack_instance = pyIncomingSlack(token_url, user_name, icon)
    else:
        slack_instance = pyIncomingSlack(token_url, user_name)
    if title !='':
        slack_instance.send(message, title, color)        
    else:
        slack_instance.send(message)

if __name__ == '__main__':
    main()
