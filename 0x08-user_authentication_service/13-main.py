#!/usr/bin/env python3
"""
Main file
"""
from auth import Auth
from user import User

from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


auth = Auth()

user = auth.register_user("test@test.com", "PwdHashed")
print(user.id)

session_id = auth.create_session(user.email)

user_from_session = auth.get_user_from_session_id(session_id)

print(user_from_session.id)

auth.destroy_session(user_from_session.id)

user_from_session_again = auth.get_user_from_session_id(session_id)
print(user_from_session_again)
