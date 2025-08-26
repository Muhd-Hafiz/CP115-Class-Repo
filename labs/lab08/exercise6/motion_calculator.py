import physics_constants

# Calculate projectile motion of a ball thrown upward from a building
# at t = 2 seconds

# Constants
physics_constants.Standard_gravity = 9.81         
physics_constants.Ball_mass = 0.5              
physics_constants.Building_height = 25     
physics_constants.Initial_velocity = 15  
time = 2                

# Assign variables from physics_constants
initial_height = physics_constants.Building_height
initial_velocity = physics_constants.Initial_velocity
gravity = physics_constants.Standard_gravity
mass = physics_constants.Ball_mass

# Calculations
position = initial_height + (initial_velocity * time) - (0.5 * gravity * time**2)
velocity = initial_velocity - (gravity * time)
kinetic_energy = 0.5 * mass * velocity**2

# Determine motion status
if velocity > 0:
    motion_status = "Moving upward"
elif velocity < 0:
    motion_status = "Moving downward"
else:
    motion_status = "Momentarily at rest"

# Display formatted report
print("Projectile Motion Report")
print("-------------------------")
print(f"Initial height: {initial_height:.2f} m")
print(f"Initial velocity: {initial_velocity:.2f} m/s")
print(f"Mass: {mass:.2f} kg")
print()
print(f"At t = {time} s:")
print(f"  Position: {position:.2f} m")
print(f"  Velocity: {velocity:.2f} m/s")
print(f"  Kinetic Energy: {kinetic_energy:.2f} J")
print(f"  Motion Status: {motion_status}")
