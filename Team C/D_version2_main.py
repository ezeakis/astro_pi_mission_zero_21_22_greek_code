from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
sense.show_message("Hello!")

sense.show_message("How are you?", scroll_speed = 0.10)
humidity = sense.get_humidity()
humidity = round(humidity)
sense.show_message(str(humidity))
G = (0, 255, 0)
R = (150, 56, 50)
B = (46, 192, 50)
Green_Matrix = [ G, G, G, G, G, G, G, B, R, R, R, G, R, R, R, B, R, G, G, R, G, G, R, B, R, G, G, G, G, G, R, B, G, R, G, G, G, R, G, B, G, G, R, G, R, G, G, B, G, G, G, R, G, G, G, B, G, G, G, G, G, G, G, B, ] 

#sense.set_pixels(Green_Matrix)

Blue_Matrix = [ B, B, B, B, B, B, B, G, R, R, R, G, R, R, R, G, R, R, R, R, R, R, R, G, R, R, R, R, R, R, R, G, B, R, R, R, R, R, B, G, B, B, R, R, R, B, B, G, B, B, B, R, B, B, B, G G, G, G, G, G, G, G, B, ] 

sense.set_pixels(Blue_Matrix)
