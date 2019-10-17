"""
在python或者其他语言中，2.0 - 1.1 != 0.9

使用decimal.Decimal可以解决这个问题。
"""

import decimal

print(2.0 - 1.1)
x = decimal.Decimal("2.0") - decimal.Decimal("1.1")
print(x)

