# -*- coding: utf-8 -*-

def rk2(y, t, dt, deriv, params):
  
    ddt = dt/2.                         #définition du demi-pas
    d1 = deriv(t,y,params)              #1ere estimation          
    yp = y + d1*ddt
    d2 = deriv(t+ddt,yp,params)         #2eme estimat. 
    return (y + d2 * dt)