import marshal
import zlib
import base64
from sys import stdout
from uncompyle6.main import decompile
import dis
gamer = []

asd = marshal.loads(zlib.decompress(base64.b64decode(b'=oFE/yHAD8AFkhBqI1hqOlmS+5WTHah7Cba2LGPMiAqRiYoSJ7lZRF0aWE/kPRMO1QcJKmykBhZMFGSkRmZoFGSliAEPFTMAsDETDAkZLxJe'[::-1])))
decompile('BYTE CODE VERSION HERE, for example: 3.9', asd, stdout)




#  dump [TEST]
gamer.append(asd)
dump = marshal.dumps(asd)
#print(dump)
#  dump [TEST]



#Testing
#print(dis.dis(asd))
