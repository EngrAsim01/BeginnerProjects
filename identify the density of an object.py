


mass = float(input('Enter the mass of object(Kg): '))
volume = float(input('Enter the volume of object(m^3): '))
density = mass/volume
print(density)


if density >= 2400 and density <= 2700:
        print(f"The metal is Aluminum.")
elif density >= 8100 and density <= 8300:
        print(f"The metal is Bronze.")
elif density >= 10400 and density <= 10600:
        print(f"The metal is Silver.")
elif density >= 11200 and density <= 11400:
        print(f"The metal is Lead.")
elif density >= 17100 and density <= 17500:
        print(f"The metal is Gold.")
elif density >= 21000 and density <= 21500:
        print(f"The metal is Platinum.")
