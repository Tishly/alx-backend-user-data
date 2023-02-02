#!/usr/bin/env python3
"""
Regex-ing function
"""

import re

def filter_datum(fields: list, redaction: str, message: str, seperator: str):
    """
    A function that returns the log message obfuscated
    Args:
        - fields: a list of strings representing all fields to obfuscate
        - redaction: a string representing by what the field will be obfuscated
    """
    return re.sub(f"({'|'.join(fields)})", redaction, message, flags=re.I)
