# Esqueleto del proto-programa para la sol. de la ecuación de difusión
from pde import ScalarField, CartesianGrid
from sympy import Piecewise
from sympy.abc import x

xc = 9770
xd = 10329
xf = 10600

#grid = CartesianGrid([[xc, xf]], 50)

grid = CartesianGrid([[0, 4]], 32)
field = ScalarField.from_expression(grid, "Piecewise((x**2, x>2), (1+x, x<=2))")

#f_ini = 1 - ((xf - x) / (xf - xd)) ** 2
#field = ScalarField.from_expression(grid,"Piecewise((1 - ((10600 - x) / (10600 - 10329)) ** 2, x >= 10329), (0, True))")  # generate initial condition
# Define boundary conditions
# bc_lower = {"value": 0}
# bc_upper = {'type': 'mixed', 'value': 1 / rf, 'const': 0}
# bc = [bc_lower, bc_upper]

# Expanded definition of the PDE
# yr = 365 * 24 * 60 * 60
# dif = 3.65 * 10 ** (-9) * yr
# mult = " -0.5 * (1/(x**2))"
# term_1 = f"({dif})* laplace(s)"
# term_2 = f"({dif})*({mult})*s"
# eq = PDE({"s": f"{term_1} + {term_2}"}, bc)
# result = eq.solve(field, t_range=10 ** 3, dt=1)

# result.plot()
