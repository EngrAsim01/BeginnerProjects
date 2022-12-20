

def volumeOfSphere(radius):
    volume = (4/3)*3.14*radius**3
    volume = volume*1000000
    return volume

def volumeOfCuboid(length,width,height):
    cubeVolume = length*width*height
    return cubeVolume

radius = float(input('Enter the radius of Sphere:'))
volumeOfEarth= volumeOfSphere(radius)
print(f'Volume of sphere is : {volumeOfEarth}' )

legth = float(input('Length of cube in mm: '))
width = float(input('Width of cube in mm: '))
height = float(input('Height of cube in mm: '))
volumeOfLego = volumeOfCuboid(legth,width,height)
print(f'Volume of Cuboid is: {volumeOfLego}')

print(f'Number of lego required for earth: {volumeOfEarth/volumeOfLego}')