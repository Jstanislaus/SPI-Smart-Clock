import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# Set up I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Set up OLED with 128x32 resolution
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display
oled.fill(0)
oled.show()

# Create image buffer
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Draw text
font = ImageFont.load_default()
draw.text((0, 0), "Hello Pi!", font=font, fill=255)

# Display image
oled.image(image)
oled.show()
