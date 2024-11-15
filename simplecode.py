from machine import Pin, I2C
import ssd1306

# Initialize I2C with the default pins
# i2c = I2C(1, scl=Pin(6), sda=Pin(5))  # Change pins if needed
i2c = I2C(1, scl=Pin(6), sda=Pin(5), freq=4000)
# Scan for I2C devices
print("Scanning I2C bus...")
devices = i2c.scan()

if devices:
    print("I2C device found at:", [hex(dev) for dev in devices])
    # Try initializing the display at both possible addresses
    try:
        display = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)  # Default address
        display.fill(0)
        display.text("Hello, ESP32-S3!", 0, 50)
        display.show()
    except Exception as e:
        print(f"Failed to initialize at 0x3C: {e}")
        try:
            display = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x58)  # Try address 0x3D
            display.fill(0)
            display.text("Hello, ESP32-S3!", 10, 10)
            display.show()
        except Exception as e:
            print(f"Failed to initialize at 0x3D: {e}")
else:
    print("No I2C device found")


