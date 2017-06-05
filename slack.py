# -*- coding:utf8 -*-

import os
from slacker import Slacker


def post_slack(msg):
    """Post slack message."""
    try:
        token = 'xoxb-189908501990-36tPW6RXAXLkgzCraAdn6Fxy'
        slack = Slacker(token)

        obj = slack.chat.post_message('#test1','Today pakct Book is '+msg)

        print obj.successful#, obj.__dict__['body']['channel'], obj.__dict__['body']['ts']
    except KeyError, ex:
        print 'Environment variable %s not set.' % str(ex)










