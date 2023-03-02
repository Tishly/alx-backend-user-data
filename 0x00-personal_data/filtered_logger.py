#!/usr/bin/env python3
"""
Regex-ing function
"""

import re


def filter_datum(fields: list, redaction: str,
                 message: str, separator: str) -> str:
    """
    A function that returns the log message obfuscated
    """
    return re.sub(f"({'|?'.join(fields)})", redaction, message, flags=re.I)
    # return re.sub("(" + separator.join(fields) + ")=(.*?)" + separator,
    # "\\1=" + redaction + separator, message)
