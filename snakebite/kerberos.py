# -*- coding: utf-8 -*-
# Copyright (c) 2015 Bolke de Bruin
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
'''
kerberos.py - A very light wrapper around gssapi

This package contains a class to read a kerberos principal

May 2015 (original implementation with krbV)

Bolke de Bruin (bolke@xs4all.nl)

Nov 2019 (implementation with gssapi for Python3)

Luca Toscano (toscano.luca@gmail.com)

'''

import gssapi

class Kerberos:
    def __init__(self):
        self.credentials = gssapi.Credentials(usage='initiate')

    def user_principal(self):
        return str(self.credentials.inquire().name)

