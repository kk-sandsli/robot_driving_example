from pybricks.hubs import PrimeHub
from pybricks.parameters import Button

def perform_button_action(hub: PrimeHub, buttons_pressed=None) -> None:
    if buttons_pressed is not None:
        if Button.LEFT in buttons_pressed:
            print("Left")
            hub.display.char('<')
        elif Button.RIGHT in buttons_pressed:
            print("Right")
            hub.display.char('>')
        else:
            hub.display.off()
            pass
    else:
        print("No buttons")



