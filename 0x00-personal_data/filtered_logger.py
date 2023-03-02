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
    # return re.sub(f"({'|?'.join(fields)})", redaction, message, flags=re.I)
    # return re.sub("(" + separator.join(fields) + ")=(.*?)" + separator,
    # "\\1=" + redaction + separator, message)
    # return re.sub(fr'({separator}|^)({"|".join(fields)})(?={separator}|$)',
    # f'\g<1>{redaction}', message)
    r = fr'({separator}|^)({"|".join(fields)})=[^{separator}]*({separator}|$)'
    return re.sub(r, f'\g<1>\\2={redaction}\g<3>', message)
