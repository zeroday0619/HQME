import re


def cleanText(readData: str) -> str:
    r"""
    Cleans text from unwanted characters.

    Args:
        readData (str): Text to be cleaned.

    Returns:
        str: Cleaned text.
    """
    cleanTxt = re.sub("[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`'…》]", "", readData)
    return cleanTxt
