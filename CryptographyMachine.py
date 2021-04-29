from typing import AnyStr

def basicCryptograph(message: str = ..., mode: str = ['Encrypt', 'Decrypt', None]) -> AnyStr :
    """
    This function `Encrypts` or `Decrypts` a `message` by specifying the `mode` to either decrypt or encrypt a user-given message.

    Args:
    `message: str` : This should contain the `message` given by user.

    `mode: str` : This should contain the `mode` in string(`str`) format. The displayed list is given for the preview of the available mode specification.
    """
    keys = """ aN@E%S$bc^de!fA*g&4O(h,KiJ"';C]:M.-D|~L_₹jk[Zl/Im5n6Wo1Rp9}`{Xq7YrP2BHs8tG0u>?<vwTxVyUF3z+Q#*)="""
    values = """ !@#$%₹^&+-/*()}{][~`"':;.,?_|=<>0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"""
    encryptionDict = dict(zip(keys, values))
    decryptionDict = dict(zip(values, keys))

    if mode == "Encrypt".casefold():
        modMessage = "".join([encryptionDict[letter] for letter in message])
        return modMessage
    
    if mode == "Decrypt".casefold():
        modMessage = "".join([decryptionDict[letter] for letter in message])
        return modMessage

message1 = input("Enter a sentence: ")
moder = input("Enter mode: ")
print(basicCryptograph(message1, moder))