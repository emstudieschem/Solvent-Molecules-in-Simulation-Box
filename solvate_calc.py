# Calulating the number of molecules of solvent for a cubic simulation box

def calculate_molecules(x, p, Mr):
    # Conversion factors
    nm = 10**(-9)
    kg = 1000
    NA = 6.022 * (10**23) # Avogadro's number

    # Calculate volume of simulation box
    V = (x * nm) ** 3 # [m^3]

    # Calculate mass from solvent density and volume of box
    m = p * V # [kg]
    m = m * kg # [g]

    # Calculate number of moles
    n = m / Mr # [mol]

    # Convert to number of molecules using Avogadro's number, and give result at int
    N = n * NA
    
    return int(N)

# User input of values
x = float(input("Enter length of simulation box side (nm): "))

p = float(input("Enter density of solvent (kg/m^3): "))

Mr = float(input("Enter molar mass of solvent (g/mol): "))

result = calculate_molecules(x, p, Mr)

print(result)