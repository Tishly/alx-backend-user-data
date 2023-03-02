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
    # regex = fr'({separator}|^)({"|".join(i)})=.*?({separator}|$)'
    # return re.sub(regex, f'\g<1>\\2={redaction}\g<3>', message)
    # return re.sub(fr'({separator}|^)({"|".join(fields)})=([^{separator}]*)({separator}|$)', f'\\1\\2={redaction}\\3\\4', message)
