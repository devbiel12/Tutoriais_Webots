from controller import Robot

robot = Robot()
time_step = int(robot.getBasicTimeStep())

sensors = []
for name in ("ds_right", "ds_left"):
    sensor = robot.getDevice(name)
    sensor.enable(time_step)
    sensors.append(sensor)

wheels = []
for name in ("wheel1", "wheel2", "wheel3", "wheel4"):
    wheel = robot.getDevice(name)
    wheel.setPosition(float("inf"))
    wheel.setVelocity(0.0)
    wheels.append(wheel)

avoid_counter = 0

while robot.step(time_step) != -1:
    left_speed = 1.0
    right_speed = 1.0

    if avoid_counter > 0:
        avoid_counter -= 1
        left_speed = 1.0
        right_speed = -1.0
    else:
        for sensor in sensors:
            if sensor.getValue() < 950.0:
                avoid_counter = 100

    wheels[0].setVelocity(left_speed)
    wheels[1].setVelocity(right_speed)
    wheels[2].setVelocity(left_speed)
    wheels[3].setVelocity(right_speed)
