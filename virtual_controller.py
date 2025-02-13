#! /usr/bin/python3
import uinput
import time
import serial

ARDUINO_PORT = "/dev/ttyACM0"

events = (
    uinput.ABS_X + (-32768, 32767, 0, 16),
    uinput.ABS_Y + (-32768, 32767, 0, 16),
    uinput.ABS_Z + (-32768, 32767, 0, 16),
    uinput.ABS_RZ + (-32768, 32767, 0, 16),
    uinput.BTN_A,
    uinput.BTN_B,
    uinput.BTN_X,
    uinput.BTN_Y,
)

controller = uinput.Device(events)

arduino_connection = None
try:
    arduino_connection = serial.Serial(ARDUINO_PORT)
    arduino_connection.baudrate = 115200
    arduino_connection.bytesize = 8
    arduino_connection.parity = 'N'
    arduino_connection.stopbits = 1
except serial.SerialException:
    print("Could not connect to arduino.\nMake sure it is plugged in and the value of ARDUINO_PORT in this script is set correctly.")
    exit()

try:
    vals = [0, 0, 0, 0, 0, 0, 0, 0]
    controller.emit(uinput.ABS_X, vals[0])
    controller.emit(uinput.ABS_Y, vals[1])
    controller.emit(uinput.ABS_Z, vals[2])
    controller.emit(uinput.ABS_RZ, vals[3])
    # controller.emit(uinput.BTN_A, 1)
    # time.sleep(0.1)
    controller.emit(uinput.BTN_A, 0)
    # controller.emit(uinput.BTN_B, 1)
    # time.sleep(0.1)
    controller.emit(uinput.BTN_B, 0)
    # controller.emit(uinput.BTN_X, 1)
    # time.sleep(0.1)
    controller.emit(uinput.BTN_X, 0)
    # controller.emit(uinput.BTN_Y, 1)
    # time.sleep(0.1)
    controller.emit(uinput.BTN_Y, 0)
    print("Connected to arduino")
    while True:
        arduino_outputs = arduino_connection.readline().split()
        if len(arduino_outputs) != 4:
            print(f"received wrong number of values from arduino: {len(arduino_outputs)}\nExpected 4 values")
            continue
        arduino_outputs = [int(x) for x in arduino_outputs]

        vals[3] = int(32768.0*(arduino_outputs[1] - 1500)/(500))
        vals[2] = int(32768.0*(arduino_outputs[0] - 1500)/(500))
        vals[1] = int(32768.0*(arduino_outputs[2] - 1000)/(1000))
        vals[0] = int(32768.0*(arduino_outputs[3] - 1500)/(500))


        controller.emit(uinput.ABS_X, vals[0])
        controller.emit(uinput.ABS_Y, vals[1])
        controller.emit(uinput.ABS_Z, vals[2])
        controller.emit(uinput.ABS_RZ, vals[3])
        time.sleep(0.001)
except KeyboardInterrupt:
    if arduino_connection:
        arduino_connection.close()
except serial.SerialException:
    print("Arduino disconnected!")
print("\nStopping")
