import time
import jwt


key = 'secret'
encoded = jwt.encode({'some': 'payload', 'exp': time.time() + 1}, key, algorithm='HS256')
print(encoded)

# time.sleep(2)
decoded = jwt.decode(encoded, key, algorithms='HS256')
print(decoded)