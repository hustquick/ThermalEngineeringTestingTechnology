import numpy as np
from sympy import symbols, diff

A_I = 10
A_U = 250
R_I = R_U = 0.5e-2
I_a = 9
U_a = 220

Delta_I = A_I * R_I
Delta_U = A_U * R_U
#
# Delta_P = U * Delta_I + I * Delta_U

P_a = U_a * I_a
S_U = Delta_U / 3
S_I = Delta_I / 3


U, I = symbols('U, I')
P = U*I
P_p_U = float(diff(P, U).subs(U, U_a).subs(I, I_a))
P_p_I = float(diff(P, I).subs(I, I_a).subs(U, U_a))

S_P = np.sqrt(P_p_U**2 * S_U**2 + P_p_I**2 * S_I**2)

lambda_P = 3 * S_P
R_P = lambda_P / P_a
