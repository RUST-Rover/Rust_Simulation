from math import pi
import numpy as np


def Critical_Stress(height, width, t, sigma_y = 240*10**6, E = 69*10**9, v = 0.33, n = 0.6, alpha = 0.8):
    def sigma_cc_over_sigma_y(b, C = 4, t = t, sigma_y = sigma_y, E = E, v = v, n = n, alpha = alpha):
        sigma_cc_over_sigma_y = alpha*((C*(pi**2)*E*t**2)/(sigma_y*12*(1-v**2)*b**2))**(1-n)
        return sigma_cc_over_sigma_y
    area = height*width-(height-2*t)*(width-2*t)
    area_no_corners = area-(t**2)*4
    side_lengths = np.array([height-2*t, width-2*t])
    side_sigma_cc_over_sigma_y = sigma_cc_over_sigma_y(side_lengths)
    for i in range(len(side_sigma_cc_over_sigma_y)):
        if side_sigma_cc_over_sigma_y>=1:
            side_sigma_cc_over_sigma_y[i]=1
    side_sigma_cc = side_sigma_cc_over_sigma_y*sigma_y
    sigma_cc = (2*t*side_lengths[0]*side_sigma_cc[0]+2*t*side_lengths[1]*side_sigma_cc[1])/area_no_corners
    return sigma_cc

def Euler_Stress(height, width, t, L, E = 69*10**9, C = 0.25):
    area = height*width-(height-2*t)*(width-2*t)
    I = (height**3*t)/6+(width**3*t)/6+(width-2*t)*t*((height/2)-t/2)**2
    P = C*(pi**2*E*I)/L
    sigma = P/area
    return sigma