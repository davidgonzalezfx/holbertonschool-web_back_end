#!/usr/bin/env python3
""" Main file """

get_page = __import__('web').get_page

url = "http://google.com"

print(get_page(url))