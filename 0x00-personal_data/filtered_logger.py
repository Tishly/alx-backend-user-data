#!/usr/bin/env python3
"""
Regex-ing function
"""

import re


def filter_datum(fields: list, redaction: str,
                 message: str, separator: str) -> str:
    """ A function that returns the log message obfuscated """
    r = fr'({separator}|^)({"|".join(fields)})=[^{separator}]*({separator}|$)'
    return re.sub(r, f'\g<1>\\2={redaction}\g<3>', message)
