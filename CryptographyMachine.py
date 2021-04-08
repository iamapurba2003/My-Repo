from typing import AnyStr

def basicCryptograph(message: str = ..., mode: str = ['Encrypt', 'Decrypt', None]) -> AnyStr :
    """
    This function `Encrypts` or `Decrypts` a `message` by specifying the `mode` to either decrypt or encrypt a user-given message.

    Args:
    `message: str` : This should contain the `message` given by user.

    `mode: str` : This should contain the `mode` in string(`str`) format. The displayed list is given for the preview of the available mode specification.
    """
    keys = """a@%$bc^de!f*g&(h,i"';:.-\| ~₹jkl/m5n6o1p9q7r2s8t0uvwxy3z+#*)=_`"""
    values = keys[::-1]
    encryptionDict = dict(zip(keys, values))
    decryptionDict = dict(zip(values, keys))

    if mode == "Encrypt":
        modMessage = "".join([encryptionDict[letter] for letter in message.lower()])
        return modMessage
    
    if mode == "Decrypt":
        modMessage = "".join([decryptionDict[letter] for letter in message.lower()])
        return modMessage.capitalize()


print(basicCryptograph("Hii, there!", "Encrypt"))