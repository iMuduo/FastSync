#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Muduo
'''
    Fast Sync
'''
import sys
import argparse
from . import sender
from . import receiver

def print_version():
    print('''\033[32m
            + ------------------------------------------ +
            |           FastSync 0.1.0.4 is free         |
            + ------------------------------------------ +
            |                                            |
            |    ☺  -------------------------->  ☺       |
            |                                            |
            |   You could donate to the Alipay account   |
            |                                            |
            |            49668929@qq.com                 |
            |                                            |
            |         ~~~~Thank you!~~~~~~~              |
            |                                            |
            |            Author : Muduo                  |
            |                                            |
            + ------------------------------------------ +
    \033[0m''')

    # sys.exit(0)

print_version()

def sending():
    parser = argparse.ArgumentParser()
    parser.add_argument('send_path',
                        type=str,
                        help='sending end local path like /home/work/workspace')
    parser.add_argument('receive_uri',
                        type=str,
                        help='receiving end uri like http://127.0.0.1:8888/home/work/workspace')
    parser.add_argument('secret_key',
                        type=str,
                        help='secret key',
                        default='',
                        nargs='?')

    args = parser.parse_args()

    sender.sending(args.send_path, args.receive_uri, args.secret_key)

def receiving():
    parser = argparse.ArgumentParser()
    parser.add_argument('port',
                        type=int,
                        help='receiving service port')
    parser.add_argument('secret_key',
                        type=str,
                        help='secret key',
                        default='',
                        nargs='?')
    args = parser.parse_args()

    receiver.receiving(args.port, args.secret_key)
