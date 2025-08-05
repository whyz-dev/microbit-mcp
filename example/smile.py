def on_data_received():
    global buffer
    buffer = serial.read_until(serial.delimiters(Delimiters.NEW_LINE)).trim()
    if buffer == "smile":
        basic.show_icon(IconNames.HAPPY)
    elif buffer == "frown":
        basic.show_icon(IconNames.SAD)
    elif buffer == "straight":
        basic.show_icon(IconNames.ASLEEP)
    else:
        basic.clear_screen()
serial.on_data_received(serial.delimiters(Delimiters.NEW_LINE), on_data_received)

buffer = ""