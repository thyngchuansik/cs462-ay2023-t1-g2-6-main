def on_gesture_shake():
    basic.show_icon(IconNames.HEART)
    basic.pause(100)
    serial.write_line("1")
    basic.clear_screen()

input.on_gesture(Gesture.SHAKE, on_gesture_shake)