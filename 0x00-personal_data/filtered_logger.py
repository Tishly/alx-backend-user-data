#!/usr/bin/env python3
"""
Regex-ing function
"""

import re


def filter_datum(fields: list, redaction: str,
                 message: str, separator: str) -> str:
    """ A function that returns the log message obfuscated """
    for i in fields:
        message = re.sub(f'{i}=.*?{separator}',
                         f'{i}={redaction}{separator}', message)
    return message
