#!/usr/bin/python3

import hashlib
import base64
import uuid
import bcrypt
from db import DB
from user import User
from typing import Union

"""Auth module"""

def _hash_password(self, password: str) -> str:
    """"
    Convert password to hash
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
