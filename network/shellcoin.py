from clove.network.bitcoin import Bitcoin


class ShellCoin(Bitcoin):
    """
    Class with all the necessary ShellCoin network information based on
    https://bitcointalk.org/index.php?topic=1054714.0
    (date of access: 02/19/2018)
    """
    name = 'shellcoin'
    symbols = ('SHELL', )
    nodes = ("153.92.98.55", )
    port = 12454
    message_start = b'\xdd\x2f\x1a\x1d'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }
