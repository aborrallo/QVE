# -*- coding: utf-8 -*-
"""
Quantum variational eigensolver demo

@author: a.a.borrallo.rentero
"""

"We import all necessary libreries, also we import VQE from Riguetti to compare with our results"

from pyquil.quil import Program
from scipy import *
import numpy as np
import pyquil.api as api
from pyquil.gates import *
from pyquil.paulis import sZ,RX
from grove.pyvqe.vqe import VQE
from scipy.optimize import minimize
import math
import sympy as sp
from sympy import symbols, Transpose
from sympy.matrices import Matrix, eye, zeros, ones, diag, GramSchmidt,MatMul

qvm = api.QVMConnection()
p=Program()

"This algorithm try to find the smallest eigenvalue of a quantum operator"
"We are goin to try to find the ground state of the next Hamiltonian"

Hamiltonian=Matrix([[1,0],[0,-1]])


phi = sp.symbols('phi')

OperatorToAnsatz=Matrix([[sp.cos(phi /2),sp.sin(phi /2)],[-sp.sin(phi /2),sp.cos(phi /2)]])

InitialiceStateKet=Matrix([1,0])
AnsatzKet=OperatorToAnsatz*InitialiceStateKet
AnsatzBra=Transpose(AnsatzKet)
FunctionToOptimize=AnsatzBra*Hamiltonian*AnsatzKet
def Func(t):
    return FunctionToOptimize[0].evalf(subs={phi: t})
print(Func(5))
#minimize(Func,0)



    




