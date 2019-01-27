#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configparser import ConfigParser


class App(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.config = ConfigParser()
            cls._instance.config.read('./sample.ini')

        return cls._instance


def main():
    app = App()
    print('名前は', app.config['cat']['name'])
    print('名前は', app.config['dog']['name'])

    app2 = App()
    print('名前は', app2.config['cat']['name'])
    print('名前は', app2.config['dog']['name'])

    print(app is app2)


if __name__ == '__main__':
    main()