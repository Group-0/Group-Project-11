#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
import argparse
import requests
import json


CMD_LIST = {
	'md5': 'Return a MD5 hash of an input string',
	'factorial': 'Return the factorial of an input integer',
    'fibonnaci': 'Display an array of integers that are less than or equal to the input number',
    'isprime': 'Determines if input number is prime or not prime',
    'slack_alert': 'Post input on Slack'
}

def md5(stringinput):
    url = "http://34.134.70.125:4000/md5/" + stringinput
    r = requests.get(url)
    j = r.json()
    print(j)

def factorial(number): 
    url = "http://34.134.70.125:4000/factorial/" + number
    r = requests.get(url)
    j = r.json()
    print(j)

def isprime(number):
    url = "http://34.134.70.125:4000/is-prime/" + number
    r = requests.get(url)
    j = r.json()
    print(j)


## if __name__ == '__main__':

parser = argparse.ArgumentParser(
	    description='Enter command',
	    usage='''cli.py COMMAND [<args>],

    commands:
    md5                  Return a MD5 hash of an input string
    factorial            Return the factorial of an input integer
    fibonnaci_sequence   Display an array of integers that are less than or equal to the input number
    isprime              Determines if input number is prime or not prime
    slack_alert          Post input on Slack

''')

parser.add_argument('COMMAND', nargs='?', default=None, help='Subcommand to run')
parser.add_argument('-m', nargs='?', type=str, default=None, help='md5 run')
parser.add_argument('-f', type=int, help='Enter a number you wish to find their factorial')
parser.add_argument('-isprimenumber', type=int, help='Enter a number to determine if it is prime or not')


args = parser.parse_args()

if not args.COMMAND or not args.COMMAND in CMD_LIST:
		print('Unrecognized command')
		parser.print_help()
		exit(1)

if args.m:
    md5(args.m)

if args.f:
    factorial(str(args.f))

if args.isprimenumber:
    isprime(str(args.isprimenumber))

