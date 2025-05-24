from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class Light(Switchable):
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")


class Fan(Switchable):
    def turn_on(self):
        print("Fan is spinning")

    def turn_off(self):
        print("Fan is stopped")


class Button:
    def __init__(self, device: Switchable):
        self._device = device

    def press(self):
        self._device.turn_on()


# Usage
light = Light()
fan = Fan()

light_button = Button(light)
fan_button = Button(fan)

light_button.press()  # Light is on
fan_button.press()    # Fan is spinning
