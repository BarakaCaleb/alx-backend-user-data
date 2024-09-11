#!/usr/bin/env python3
"""Auth module"""

import hashlib
import base64
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from user import User
from typing import Union


def _hash_password(self, password: str) -> str:
    """"
    Convert password to hash
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
