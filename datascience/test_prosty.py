

kod="""x = 10
y = 20
z = x + y
print(z)"""

import dis

print(dis.dis(kod))