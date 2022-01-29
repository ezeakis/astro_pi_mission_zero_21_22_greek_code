from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)

sense.show_message("gia melene aggelo koyLmanda")
sense.show_message("hum is")


hum = sense.get_humidity()
hum = round(hum)
sense.show_message(str(hum))

G = (255, 0, 0)

Green_Matrix = [
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
]
sense.set_pixels(Green_Matrix )
