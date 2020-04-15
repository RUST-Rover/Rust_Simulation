import numpy as np

M_0 = np.array([0.79, 1])
m_dot = np.array([281, 1])
eta_inlet = np.array([0.96, 1])
pi_fan = np.array([1.65, 1])
eta_fan = np.array([0.92, 1])
bypass_ratio = np.array([5, 1])
eta_LPC = np.array([0.91, 1])
eta_HPC = np.array([0.88, 1])
eta_LPT = np.array([0.91, 1])
eta_HPT = np.array([0.93, 1])
eta_mech = np.array([0.99, 1])
eta_cc = np.array([0.995, 1])
pi_LPC = np.array([1.3, 1])
pi_HPC = np.array([13, 1])
eta_nozzle = np.array([0.98, 1])
pi_cc = np.array([0.96, 1])


def T_04(T_03):    return T_03 + 650


T_amb = np.array([219, 1])
P_amb = np.array([23842, 1])
R = 287
LHV = 43 * 10 ** 6
cp_air = 1000
cp_gas = 1150
k_air = 1.4
k_gas = 1.33

# Part 1
a = (k_air * R * T_amb) ** 0.5
V_0 = M_0 * a
T_00 = T_amb + (V_0 ** 2) / (2 * cp_air)
print("T_00 = " + str(T_00))

# Part 2
P_00 = P_amb * (T_00 / T_amb) ** (k_air / (k_air - 1))
print("P_00 = " + str(P_00))

# Part 3
T_02 = T_00
T_021 = T_02 + (T_02 / eta_fan) * ((pi_fan ** ((k_air - 1) / k_air)) - 1)
print("T_021 = " + str(T_021))

# Part 4
P_02 = P_amb * (1 + eta_inlet * (V_0 ** 2 / (2 * cp_air * T_amb))) ** (k_air / (k_air - 1))
P_021 = P_02 * pi_fan
print("P_021 = " + str(P_021))

# Part 5
m_dot_HOT = m_dot / (bypass_ratio + 1)
m_dot_COLD = m_dot - m_dot_HOT
print("m_dot_HOT = " + str(m_dot_HOT))
print("m_dot_COLD = " + str(m_dot_COLD))

# Part 6
T_025 = T_021 + (T_021 / eta_LPC) * ((pi_LPC ** ((k_air - 1) / k_air)) - 1)
print("T_025 = " + str(T_025))

# Part 7
P_025 = P_021 * pi_LPC
print("P_025 = " + str(P_025))

# Part 8
T_03 = T_025 + (T_025 / eta_HPC) * ((pi_HPC ** ((k_air - 1) / k_air)) - 1)
print("T_03 = " + str(T_03))

# Part 9
P_03 = P_025 * pi_HPC
print("P_03 = " + str(P_03))

# Part 10
T_04 = T_04(T_03)
print("T_04 = " + str(T_04))

# Part 11
P_04 = P_03 * pi_cc
print("P_04 = " + str(P_04))

# Part 12
W_fan = m_dot * cp_air * (T_021 - T_02)
W_LPC = m_dot_HOT * cp_air * (T_025 - T_021)
W_HPC = m_dot_HOT * cp_air * (T_03 - T_025)
print("W_fan = " + str(W_fan))
print("W_LPC = " + str(W_LPC))
print("W_HPC = " + str(W_HPC))

# Part 13
W_HPT = W_HPC / eta_mech
m_dot_f = (m_dot_HOT * cp_gas * (T_04 - T_03)) / (LHV * eta_cc)
T_045 = ((W_HPT / ((m_dot_HOT + m_dot_f) * cp_gas)) - T_04) * -1
print("T_045 = " + str(T_045))

# Part 14
P_045 = P_04 * (1 - (1 - (T_045 / T_04)) / eta_HPT) ** (k_gas / (k_gas - 1))
print("P_045 = " + str(P_045))

# Part 15
W_LPT = (W_LPC + W_fan) / eta_mech
T_05 = ((W_LPT / ((m_dot_HOT + m_dot_f) * cp_gas)) - T_045) * -1
print("T_05 = " + str(T_05))

# Part 18
P_05 = P_045 * (1 - (1 - (T_05 / T_045)) / eta_LPT) ** (k_gas / (k_gas - 1))
print("P_05 = " + str(P_05))

# Part 19
pi_cr_nozzle = ((1 - (k_gas - 1) / (eta_nozzle * (k_gas + 1))) ** (k_gas / (k_gas - 1))) ** -1
comp_ratio_nozzle = P_05 / P_00
print("pi_cr = " + str(pi_cr_nozzle))
print("comp_ratio_nozzle = " + str(comp_ratio_nozzle))

# Part 20
pi_cr_fan = ((1 - (k_air - 1) / (eta_nozzle * (k_air + 1))) ** (k_air / (k_air - 1))) ** -1
comp_ratio_fan = P_021 / P_00
print("pi_cr = " + str(pi_cr_fan))
print("comp_ratio_fan = " + str(comp_ratio_fan))

# Part 21
TR_cr = (k_gas + 1) / 2
T_8 = T_05 / TR_cr
print("T_8 = " + str(T_8))

# Part 22
P_8 = P_05 / pi_cr_nozzle
print("P_8 = " + str(P_8))

# Part 23
TR_cr = (k_air + 1) / 2
T_18 = T_021 / TR_cr
print("T_18 = " + str(T_18))

# Part 22
P_18 = P_021 / pi_cr_fan
print("P_18 = " + str(P_18))

# Part 23
V_8 = (k_gas * R * T_8) ** 0.5
print("V_8 = " + str(V_8))

# Part 24
V_18 = (k_air * R * T_18) ** 0.5
print("V_18 = " + str(V_18))

# Part 25
T_fan = m_dot_COLD * (V_18 - V_0) + ((m_dot_COLD * R * T_18) * (P_18 - P_amb)) / (P_18 * V_18)
T_core = (m_dot_HOT + m_dot_f) * (V_8 - V_0) + (((m_dot_HOT + m_dot_f) * R * T_8) * (P_8 - P_amb)) / (P_8 * V_8)
T_tot = T_fan + T_core
print("T_fan = " + str(T_fan))
print("T_core = " + str(T_core))
print("T_tot = " + str(T_tot))

# Part 26
SFC = (m_dot_f) / T_tot
print("SFC = " + str(SFC))
