#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Muduo
'''
    FastSync Sender
'''
import requests
import logging
from urlparse import urlparse
from base64 import b64encode
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(filename)s -> (%(threadName)s) [%(funcName)s line:%(lineno)d] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class SenderHandler(FileSystemEventHandler):

    def __init__(self, send_path, receive_uri, secret_key):
        FileSystemEventHandler.__init__(self)
        self.send_path = send_path.rstrip('/')
        result = urlparse(receive_uri)
        self.server = '%s://%s' % (result.scheme, result.netloc)
        self.receive_path = result.path.rstrip('/')
        self.secret_key = secret_key

    def on_created(self, event):
        logging.info('[Create] %s %s' % ('DIR' if event.is_directory else 'FILE', self.mapping(event.src_path)))
        if event.is_directory:        
            response = requests.post('%s/create' % self.server, data={
                'secret_key': self.secret_key,
                'path': self.mapping(event.src_path),
                'is_directory': 'true',
            }).json()
        else:
            response = requests.post('%s/create' % self.server, data={
                'secret_key': self.secret_key,
                'path': self.mapping(event.src_path),
                'data': b64encode(open(event.src_path, 'rb').read()),
            }).json()
        if response['status'] == 0:
            logging.info('[Create] Success')
        else:
            logging.info('[Create] Fail %s' % response['msg'])

    def on_moved(self, event):
        logging.info('[Move] %s %s -> %s' % ('DIR' if event.is_directory else 'FILE', self.mapping(event.src_path), self.mapping(event.dest_path)))       
        response = requests.post('%s/move' % self.server, data={
            'secret_key': self.secret_key,
            'fpath': self.mapping(event.src_path),
            'tpath': self.mapping(event.dest_path),
        }).json()
        if response['status'] == 0:
            logging.info('[Move] Success')
        else:
            logging.info('[Move] Fail %s' % response['msg'])

    def on_deleted(self, event):
        logging.info('[Delete] %s %s' % ('DIR' if event.is_directory else 'FILE', self.mapping(event.src_path)))       
        response = requests.post('%s/delete' % self.server, data={
            'secret_key': self.secret_key,
            'path': self.mapping(event.src_path),
        }).json()
        if response['status'] == 0:
            logging.info('[Delete] Success')
        else:
            logging.info('[Delete] Fail %s' % response['msg'])

    def on_modified(self, event):
        logging.info('[Modify] %s %s' % ('DIR' if event.is_directory else 'FILE', self.mapping(event.src_path)))
        if event.is_directory:        
            response = requests.post('%s/modify' % self.server, data={
                'secret_key': self.secret_key,
                'path': self.mapping(event.src_path),
                'is_directory': 'true',
            }).json()
        else:
            response = requests.post('%s/modify' % self.server, data={
                'secret_key': self.secret_key,
                'path': self.mapping(event.src_path),
                'data': b64encode(open(event.src_path, 'rb').read()),
            }).json()
        if response['status'] == 0:
            logging.info('[Modify] Success')
        else:
            logging.info('[Modify] Fail %s' % response['msg'])

    def mapping(self, path):
        return path.replace(self.send_path, self.receive_path)

def sending(send_path, receive_uri, secret_key):
    observer = Observer()
    observer.schedule(
        SenderHandler(send_path, receive_uri, secret_key),
        send_path,
        recursive=True
    )
    observer.setDaemon(False)
    observer.start()
    logging.info('start sync path: %s -> %s' % (send_path, receive_uri))

if __name__ == '__main__':
    sending('/Users/123/tmp/1', 'http://127.0.0.1:1234/Users/123/tmp/2', '')












