#!/usr/bin/env python3

import sys
import logging.config

import bottle
from bottle import get, post, request, response, template, redirect
import uuid , requests


# Set up app and logging
app = bottle.default_app()
app.config.load_config('./etc/app.ini')

logging.config.fileConfig(app.config['logging.config'])

KV_URL = app.config['sessions.kv_url']

# Disable Resource warnings produced by Bottle 0.12.19 when reloader=True
#
# See
#  <https://docs.python.org/3/library/warnings.html#overriding-the-default-filter>
#
if not sys.warnoptions:
    import warnings
    warnings.simplefilter('ignore', ResourceWarning)


@get('/')
def show_form():
    #get the sessions
    sid = request.get_cookie('sid')
    #count1 = 0, count2 = 0


# if not sid make sid equal uuid4
    if not sid:

        sid = uuid.uuid4() 
        #set count
        set_count = {'count1' :'0' , 'count2' :'0'}
        response.set_cookie('sid',str(sid))
        #print(sid)
        res_cookie = requests.put(KV_URL,json={str(sid): set_count})
        #print('Hello2', res_cookie)
        #code modify from Professor code
        #https://requests.readthedocs.io/en/master/user/quickstart/ method for requests
        if sid:
            #moved it below# #query_url = KV_URL +'/'+str(sid) 
            res_data = requests.get(KV_URL + "/sid").json()
            #print('hello',res_data)

    response.set_cookie('sid',str(sid))

    #count1 = request.get_cookie('count1', default='0')
    #count2 = request.get_cookie('count2', default='0')
    
    query_url = KV_URL +'/'+str(sid)
    count1 = requests.get(query_url).json()[str(sid)]["count1"] #use query_url to get json sessionid current values
    count2 = requests.get(query_url).json()[str(sid)]["count2"]


    count1 = int(count1) + 1

    #response.set_cookie('count1', str(count1))

    update_cookie = requests.put(KV_URL, json={str(sid): {'count1':str(count1), 'count2': str(count2)}})

    return template('counter.tpl', counter1=count1, counter2=count2, sid=sid)


@post('/increment')
def increment_count2():
    sid = request.get_cookie('sid') #get cookie from client
    response.set_cookie('sid', str(sid)) #set it
    query_url = KV_URL +'/'+str(sid)
    count1 = requests.get(query_url).json()[str(sid)]["count1"]
    count2 = requests.get(query_url).json()[str(sid)]["count2"]
    count2 = int(count2) + 1
    update_cookie = requests.put(KV_URL, json={str(sid): {'count1': str(count1), 'count2': str(count2)}})

    return redirect('/')


@post('/reset')
def reset_counts():

    sid = request.get_cookie('sid')
    response.delete_cookie('sid')
    query_url = KV_URL + '/' + sid
    res_del = requests.delete(query_url)


    return redirect('/')
