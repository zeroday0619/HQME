import re


def cleanText(readData) -> str:
    r"""
    Cleans text from unwanted characters.

    Args:
        readData (str): Text to be cleaned.

    Returns:
        str: Cleaned text.
    """
    return re.sub("[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`'…》]", "", readData)
