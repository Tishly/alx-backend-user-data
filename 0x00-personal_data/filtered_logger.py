#!/usr/bin/env python3
"""
Regex-ing function
"""

import re


def filter_datum(fields: list, redaction: str, message: str, seperator: str):
    """
    A function that returns the log message obfuscated
    """
    return re.sub(f"({'|'.join(fields)})", redaction, message, flags=re.I)
