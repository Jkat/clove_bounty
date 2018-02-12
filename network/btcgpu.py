from clove.network.bitcoin import Bitcoin


class BTCGPU(Bitcoin):
    """
    Class with all the necessary BTCGPU network information based on
    https://github.com/btcgpu/btcgpu/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'btcgpu'
    symbols = ('BTCGPU', )
    seeds = (
        'eu-dnsseed.bitcoingold-official.org',
        'dnsseed.bitcoingold.org',
        'dnsseed.btcgpu.org',
    )
    port = 8338


class BTCGPUTestNet(BTCGPU):
    """
    Class with all the necessary BTCGPU testing network information based on
    https://github.com/btcgpu/btcgpu/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-btcgpu'
    seeds = (
        'eu-test-dnsseed.bitcoingold-official.org',
        'test-dnsseed.bitcoingold.org',
        'test-dnsseed.btcgpu.org',
        'btg.dnsseed.minertopia.org',
    )
    port = 18338
