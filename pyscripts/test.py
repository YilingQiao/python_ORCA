import torch
import pyorca

a = pyorca.Vector2(0.1, 1.2)
b = pyorca.Vector2()
print(b.x())
print(a.y())
print(pyorca.absSq(a))
print((2.0*a).x())
print((a*2.0).x())
vec = pyorca.V_Vec2()

vec.append(a)
vec.append(a)

print(vec)
#pyorca.Blocks()