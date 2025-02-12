# Virtual Controller

Do you have a radio transmitter and receiver for flying drones and RC planes, and you want to use it to practice flying in a simulator? But the transmitter does not have a USB output, so you can't connect it to your computer?
Probably not. But in case you do, this is the perfect thing for that exact situation. With this, you can use your radio transmitter as a virtual joystick/controller to play any game, including flight simulators.

## Setup:
- First, you need an arduino board (UNO works, I haven't tried anything else but anthing with at least 4 pmw ports should work).
- Take your receiver and connect it's ground to the arduino's ground. Then, connect the arduino's 5v line to one the receiver's power pins (Some receivers might take 3.3v power, please verify to make sure you don't accidentally cook your reciver).
- Then connect pins 3, 5, 6 and 9 of the arduino to the yaw, throttle, pitch and roll channels of your receiver respectively.
- Upload the arduino code in `virtual_controller.ino` to the arduino.
- Now, run `virtual_controller.py` (you might need to install uinput and pyserial python modules)
- As long as it didn't throw any error and the arduino's pin 13 light is flashing, you should be fine.
- You can turn on your transmitter, and you might notice that the arduino's light starts flashing more frequently, indicating it's actually receiving input.
- If you check steam's settings, it should recognise the virtual controller.
- You can now use the transmitter as a controller for your games, so enjoy! If any of the inputs are wrongly assigned, you might have messed up the order of the pins, so you can move them around to fix it. If any input is flipped, like trying to roll left rolls it to the right, you could just add a minus sign in the python code of that corresponding input to fix it.

