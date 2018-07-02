from bip32utils import BIP32Key, BIP32_HARDEN
from mnemonic import Mnemonic

# EOS https://github.com/satoshilabs/slips/blob/master/slip-0044.md
coin_type = 194
# 0: receive, 1: change
path = 0
# index
index = 0

seed = 'pride pride pride pride pride pride pride pride pride pride pride pride'

m = BIP32Key.fromEntropy(Mnemonic.to_seed(seed))

m = m.ChildKey(44 + BIP32_HARDEN)
m = m.ChildKey(coin_type + BIP32_HARDEN)
m = m.ChildKey(0 + BIP32_HARDEN)
m = m.ChildKey(path)
m = m.ChildKey(index)

print m.dump()