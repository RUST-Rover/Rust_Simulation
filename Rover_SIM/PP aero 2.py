import numpy as np

M_0 = np.array([0.77, 0.78])
m_dot = np.array([70, 78])
eta_inlet = np.array([0.99, 0.98])
eta_LPC = np.array([0.87, 0.9])
eta_HPC = np.array([0.93, 0.88])
eta_LPT = np.array([0.87, 0.92])
eta_HPT = np.array([0.89, 0.92])
eta_mech = np.array([0.99, 0.99])
eta_cc = np.array([0.99, 0.98])
pi_LPC = np.array([1.59, 1.43])
pi_HPC = np.array([8.6, 9])
pi_cc = np.array([0.95, 0.94])
T_4 = np.array([1300, 1300])
T_amb = np.array([213, 219])
p_amb = np.array([23842, 23842])
R = np.array([287, 287])
LHV = np.array([43, 43])
cp_air = np.array([1000, 1000])
cp_gas = np.array([1150, 1150])
k_air = np.array([1.4, 1.4])
k_gas = np.array([1.33, 1.33])

# Part 1
T_00 = T_amb*(1+((k_air-1)/2)*M_0**2)
print("T_00 = "+str(T_00))

# Part 2
p_00 = p_amb*(T_00/T_amb)**(k_air/(k_air-1))
print("p_00 = "+str(p_00))

# Part 3
T_02 = T_00
print("T_02 = "+str(T_02))

# Part 4
p_02 = p_amb*(1+eta_inlet*((k_air-1)/2)*M_0**2)**(k_air/(k_air-1))
print("p_02 = "+str(p_02))

# Part 5
T_025 = (((pi_LPC**(((k_air/(k_air-1))**-1))-1)/eta_LPC)+1)*T_02
print("T_025 = "+str(T_025))

# Part 6
p_025 = p_02*pi_LPC
print("p_025 = "+str(p_025))

# Part 7
T_03 = (((pi_HPC**(((k_air/(k_air-1))**-1))-1)/eta_HPC)+1)*T_025
print("T_03 = "+str(T_03))

# Part 8
p_03 = p_025*pi_HPC
print("p_03 = "+str(p_03))

# Part 9
T_04 = T_4
print("T_04 = "+str(T_04))

# Part 10
p_04 = p_03*pi_cc
print("p_04 = "+str(p_04))

# Part 11
W_LPC = m_dot*cp_air*(T_025-T_02)
W_HPC = m_dot*cp_air*(T_03-T_025)
W_HPT = W_HPC/eta_mech
W_LPT = W_LPC/eta_mech
T_045 = T_04 - W_HPT/(m_dot*cp_gas)
T_05 = T_045 - W_LPT/(m_dot*cp_gas)
print("T_045 = "+str(T_045))
print("T_05 = "+str(T_05))

# Part 12
p_045 = p_04*(1-(1-T_045/T_04)/eta_HPT)**(k_gas/(k_gas-1))
print("p_045 = "+str(p_045))
""""""
p_045 = 197163.931
T_045 = 1082.3014
T_05 = 1048.917

# Part 12
p_05 = p_045*(1-(1-T_05/T_045)/eta_LPT)**(k_gas/(k_gas-1))
print("p_05 = "+str(p_05))

