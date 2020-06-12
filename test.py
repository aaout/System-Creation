import numpy as np
import sympy as sym

a, b = sym.symbols("a, b")
eq = 1/2 *((b)**2 + (a - 1/2)**2 + (a  - 3/2)**2)
eq1 = sym.diff(eq, a)
eq2 = sym.diff(eq, b)

ans = sym.solve([eq1, eq2])
print("a:",float(ans[a]))
print("b:",float(ans[b]))
