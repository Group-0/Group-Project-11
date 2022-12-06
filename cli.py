#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import requests
import json


CMD_LIST = {
	'md5': 'Return a MD5 hash of an input string',
	'factorial': 'Return the factorial of an input integer',
    'fibonnaci': 'Display an array of integers that are less than or equal to the input number',
    'isprime': 'Determines if input number is prime or not prime',
    'slackalert': 'Post input on Slack',
    'keyval': 'POST, PUT, GET, DELETE key-value pairs'
}

API_URL = "http://34.134.70.125/"

def md5(stringinput):
    url = f'{API_URL}md5/{stringinput}'
    r = requests.get(url)
    j = r.json()
    print(j)

def factorial(number):
    url = f'{API_URL}factorial/{number}'
    r = requests.get(url)
    j = r.json()
    print(j)

def fibonnaci(number):
    url = f'{API_URL}fibonacci/{number}'
    r = requests.get(url)
    j = r.json()
    print(j)

def isprime(number):
    url = f'{API_URL}is-prime/{number}'
    r = requests.get(url)
    j = r.json()
    print(j)

def slackalert(stringinput):
    url = f'{API_URL}slack-alert/{stringinput}'
    r = requests.get(url)
    j = r.json()
    print(j)

def keyval_pp(command, key, value):
    url = "http://34.134.70.125:4000/keyval"
    if command == 'post':
        response = requests.post(url, json={'key': key, 'value': value})
    elif command == 'put':
        response = requests.put(url, json={'key': key, 'value': value})
    j = response.json()
    print(j)

def keyval_gd(command, key):
    url = f'{API_URL}keyval/{command, key}'
    if command == 'get':
        response = requests.get(url)
    elif command == 'delete':
        response = requests.delete(url)
    j = response.json()
    print(j)

parser = argparse.ArgumentParser(
	    description='Enter command to run followed by [<options>] [value]',
	    usage='''cli.py COMMAND [<args>],

    commands:
    md5                  Return a MD5 hash of an input string
    factorial            Return the factorial of an input integer
    fibonnaci            Display an array of integers that are less than or equal to the input number
    isprime              Determines if input number is prime or not prime
    slackalert           Post input on Slack
    keyval               POST, PUT, GET, DELETE key-value pairs
''')

parser.add_argument('COMMAND', nargs='?', default=None, help='Subcommand to run')
parser.add_argument('-m', nargs='?', type=str, default=None, help='Enter a string as input to convert it to a MD5 hash')
parser.add_argument('-f', type=int, help='Enter a number you wish to find their factorial')
parser.add_argument('-fc', type=int, help='Display an array of integers that are less than or equal to the input number')
parser.add_argument('-p', type=int, help='Enter a number to determine if it is prime or not')
parser.add_argument('-s', type=str, help='Add desired string input to send as a Slack alert')
parser.add_argument('-c', choices=['post','put','get','delete'], help='Enter which command you would like to use to store/retrieve key-value variables: post, put, get, delete')
parser.add_argument('-k', help='Key of key-value pair')
parser.add_argument('-v', help='Value of key-value pair')

args = parser.parse_args()

if not args.COMMAND or not args.COMMAND in CMD_LIST:
		print('Unrecognized command')
		parser.print_help()
		exit(1)

if args.m:
    md5(args.m)

if args.f:
    factorial(str(args.f))

if args.fc:
    fibonnaci(str(args.fc))

if args.p:
    isprime(str(args.p))

if args.s:
    slackalert(args.s)

if ((args.c == 'post') or (args.c == 'put')) and args.k and args.v:
    keyval_pp(args.c, str(args.k), str(args.v))
elif ((args.c == 'get') or (args.c == 'delete')) and args.k:
    keyval_gd(args.c, str(args.k))
