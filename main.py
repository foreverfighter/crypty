#!/usr/bin/env python

from cryptography.fernet import Fernet


def encrypt(s):
    """Takes UTF-8 string and spits UTF-8 token"""
    key = Fernet.generate_key()
    f = Fernet(key)
    bytes = s.encode('utf8')
    token = f.encrypt(bytes)
    s_key = key.decode('utf8')
    s_token = token.decode('utf8')
    return s_key, s_token


def decrypt(key, token):
    """Takes token in UTF-8 (or bytestring) and spits UTF-8 string"""
    try:
        f = Fernet(key)
    except TypeError:
        key = key.encode('utf8')
        f = Fernet(key)
    try:
        bytes = f.decrypt(token)
    except TypeError:
        token = token.encode('utf8')
        bytes = f.decrypt(token)
    s = bytes.decode('utf8')
    return s
