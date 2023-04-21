function on_pin_pressed_p3() {
    
}

function on_pin_pressed_p10() {
    
    if (servo_pin_variable == 0) {
        pins.servoWritePin(AnalogPin.P0, 0)
        servo_pin_variable = 1
    }
    
}

input.onPinPressed(TouchPin.P2, on_pin_pressed_p2)
function on_pin_pressed_p2() {
    if (servo_pin_variable == 0) {
        pins.servoWritePin(AnalogPin.P0, 0)
        basic.pause(5000)
        pins.servoWritePin(AnalogPin.P0, 180)
        basic.pause(1000)
        pins.servoWritePin(AnalogPin.P0, 0)
    } else {
        basic.pause(5000)
        pins.servoWritePin(AnalogPin.P0, 180)
        basic.pause(1000)
        pins.servoWritePin(AnalogPin.P0, 0)
    }
    
}

input.onPinPressed(TouchPin.P2, on_pin_pressed_p2)
function on_pin_pressed_p13() {
    if (servo_pin_variable == 0) {
        pins.servoWritePin(AnalogPin.P0, 0)
        basic.pause(5000)
        pins.servoWritePin(AnalogPin.P0, 180)
        basic.pause(1000)
        pins.servoWritePin(AnalogPin.P0, 0)
    } else {
        basic.pause(5000)
        pins.servoWritePin(AnalogPin.P0, 180)
        basic.pause(1000)
        pins.servoWritePin(AnalogPin.P0, 0)
    }
    
}

input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    
    if (servo_pin_variable == 0) {
        pins.servoWritePin(AnalogPin.P0, 0)
        servo_pin_variable = 1
    } else {
        pins.servoWritePin(AnalogPin.P0, 180)
        servo_pin_variable = 0
    }
    
})
let servo_pin_variable = 0
servo_pin_variable = 1
