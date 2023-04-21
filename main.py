def on_pin_pressed_p3():
    pass
#//dev notes//
def on_pin_pressed_p10():
    global servo_pin_variable
    if servo_pin_variable == 0:
        pins.servo_write_pin(AnalogPin.P0, 0)
        servo_pin_variable = 1
input.on_pin_pressed(TouchPin.P11, on_pin_pressed_p11)

def on_pin_pressed_p2():
    if servo_pin_variable == 0:
        pins.servo_write_pin(AnalogPin.P0, 0)
        basic.pause(5000)
        pins.servo_write_pin(AnalogPin.P0, 180)
        basic.pause(1000)
        pins.servo_write_pin(AnalogPin.P0, 0)
    else:
        basic.pause(5000)
        pins.servo_write_pin(AnalogPin.P0, 180)
        basic.pause(1000)
        pins.servo_write_pin(AnalogPin.P0, 0)
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

def on_pin_pressed_p13():
    if servo_pin_variable == 0:
        pins.servo_write_pin(AnalogPin.P0, 0)
        basic.pause(5000)
        pins.servo_write_pin(AnalogPin.P0, 180)
        basic.pause(1000)
        pins.servo_write_pin(AnalogPin.P0, 0)
    else:
        basic.pause(5000)
        pins.servo_write_pin(AnalogPin.P0, 180)
        basic.pause(1000)
        pins.servo_write_pin(AnalogPin.P0, 0)

def on_pin_pressed_p1():
    global servo_pin_variable
    if servo_pin_variable == 0:
        pins.servo_write_pin(AnalogPin.P0, 0)
        servo_pin_variable = 1
    else:
        pins.servo_write_pin(AnalogPin.P0, 180)
        servo_pin_variable = 0
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

servo_pin_variable = 0
servo_pin_variable = 1