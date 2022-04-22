import matplotlib.pyplot as plt
import math


# x_values = [1, 2, 3, 4]
# y_values = [5, 4, 6, 2]

# chart = plt.plot(x_values, y_values)
# plt.show()
# print("Finish")

# Initial distribution of the field
def si(r):
    rf = 10600
    rd = 10329

    if r >= rd:
        f_ini = 1 - ((rf - r) / (rf - rd)) ** 2
    else:
        f_ini = 0
    return f_ini


#print(si(10600))


# temperature *accr: accretion rate, units Msun/yr*)


def temp(m_accr):
    d = math.log10(m_accr)
    a = 7.887 + 0.528 * (1 - math.exp(-(0.899 * (d + 11))))
    return 10 ** a


#print(temp(3 * 10 ** (-10)))


# density Urpin & Geppert (1994) Figure 1
# Units g/cm^3, the coordinate r is measured in metres

def den(r):
    rf = 10600
    rc = 9770
    rd = 10329

    pos = rf - r
    den1 = 1.609456 * 10 ** 6 + 7920 * pos ** 3
    den2 = pos ** 4.9494066

    if pos <= 100:
        density = den1
    else:
        density = den2
    return density


#print(den(9000))


# Conductity. Urpin & Geppert (1995). We consider that the core
# composed of iron 56
# A = 56 mass number
# Z = 26 charge number

# Conductivity due to phonons c_ph, units: 1/s

def c_ph(r, m_accr):
    z_ph = 26
    a_ph = 56
    x_ph = ((z_ph * den(r)) / (10 ** 6 * a_ph)) ** (1. / 3.)

    td = 2.4 * 10 ** 6 * math.sqrt(2 * z_ph / a_ph) * x_ph ** (3 / 2)
    return 1.21 * 10 ** 28 * (x_ph / temp(m_accr)) ** 2 * math.sqrt(temp(m_accr) ** 2 + 0.084 * td ** 2)


# Conductivity due to impurities

def c_imp(r):
    q = 0.01  # Urpin & Geppert 1995, fig 1
    l_imp = 2
    z_imp = 30
    a_imp = 130

    x_imp = ((z_imp * den(r)) / (10 ** 6 * a_imp)) ** (1. / 3.)
    return 8.53 * 10 ** 21 * x_imp * (z_imp / (l_imp * q))


#print(c_ph(9770, 3 * 10 ** (-10)))
#print(c_imp(9000))


# Total conductivity

def c_tot(r, m_accr):
    return 1 / ((1 / c_ph(r, m_accr)) + (1 / c_imp(r)))


#print(c_tot(9000, 3 * 10 ** (-10)))
