#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 21:44:26 2016

@author: siva
"""
def remove_HTML_markup(test_string):
    '''
    This functionn removes this HTML markup from the given string
    '''
    tag = False
    output = ""

    for char in test_string:
        if char == '<': # Start of Markup
            tag = True
        elif char == '>':
            tag = False
        elif not tag:
            output = output + char

    return output


result1 = remove_HTML_markup('<b>Hello HTML Markup Filter</b>')
assert result1 == "Hello HTML Markup Filter"

result2 = remove_HTML_markup('"<b>Hello HTML Markup Filter</b>"')
assert result2 == '"Hello HTML Markup Filter"'

result3 = remove_HTML_markup\
('<a href = "https://www.facebook.com">facebook</a>')
assert result3 == 'facebook'

result4 = remove_HTML_markup('<a href = ">">facebook</a>')
assert result4 == 'facebook'
