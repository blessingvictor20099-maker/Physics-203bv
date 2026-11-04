print("1. Speed")
print("2. Force")
print("3. Density")
print("4. Work Done")
print("5. Kinetic Energy")

choice = int(input("Choose a formula (1-5): "))

if choice == 1:
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))

    speed = distance / time
    print("Speed =", speed, "m/s")

elif choice == 2:
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s²): "))

    force = mass * acceleration
    print("Force =", force, "N")

elif choice == 3:
    mass = float(input("Enter mass (kg): "))
    volume = float(input("Enter volume (m³): "))

    density = mass / volume
    print("Density =", density, "kg/m³")

elif choice == 4:
    force = float(input("Enter force (N): "))
    distance = float(input("Enter distance (m): "))

    work = force * distance
    print("Work Done =", work, "J")

elif choice == 5:
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))

    kinetic_energy = 0.5 * mass * velocity ** 2
    print("Kinetic Energy =", kinetic_energy, "J")

else:
    print("Invalid choice. Please select 1-5.")
