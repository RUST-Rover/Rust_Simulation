import numpy as np

T_amb = np.array([285, 285])
p_0 = np.array([99500, 100300])
V_0 = np.array([240, 220])
m_dot = np.array([32, 38])
eta_inlet = np.array([0.98, 0.98])
pi_comp = np.array([8, 8])
eta_comp = np.array([0.89, 0.89])
pi_cc = np.array([0.99, 0.99])
eta_cc = np.array([0.99, 0.99])
LHV_f = np.array([43000000, 43000000])
T_04 = np.array([1300, 1300])
eta_turb = np.array([0.95, 0.95])
eta_mech = 0.99
cp_air = 1000
cp_gas = 1150
k_air = 1.4
k_gas = 1.33






# Part 1
T_00 = T_amb + (V_0**2)/(2*cp_air)
print("T_00 = "+str(T_00))

# Part 2
p_00 = p_0*(T_00/T_amb)**(k_air/(k_air-1))
print("p_00 = "+str(p_00))

# Part 3
T_02 = T_00
print("T_02 = "+str(T_02))

# Part 4
p_02 = p_0*(1+eta_inlet*(V_0**2/(2*cp_air*T_amb)))**(k_air/(k_air-1))
print("p_02 = "+str(p_02))

# Part 5
T_03 = (((pi_comp**(((k_air/(k_air-1))**-1))-1)/eta_comp)+1)*T_02
print("T_03 = "+str(T_03))


# Part 6
p_03 = p_02*pi_comp
print("p_03 = "+str(p_03))

# Part 7
W_comp = m_dot*cp_air*(T_03-T_02)
print("W_comp = "+str(W_comp))

# Part 8
p_04 = p_03*pi_cc
print("p_04 = "+str(p_04))

# Part 9
m_dot_f = (m_dot*cp_gas*(T_04-T_03)) / (LHV_f*eta_cc)
print("m_dot_f = "+str(m_dot_f))

# Part 10
W_turb = W_comp/eta_mech
print("W_turb = "+str(W_turb))

# Part 11
T_05 = ((W_turb / (m_dot*cp_gas))-T_04)*-1
print("T_05 = "+str(T_05))

# Part 12
p_05 = p_04*(1-(1-(T_05/T_04))/eta_turb)**(k_gas/(k_gas-1))
print("p_05 = "+str(p_05))


"""
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
T_045 = (((pi_H**(((k_gas/(k_gas-1))**-1))-1)/eta_HPT)+1)*T_04
print("T_045 = "+str(T_045))"""
