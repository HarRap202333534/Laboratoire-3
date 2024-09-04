import bme280
import smbus2
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.output(27, GPIO.LOW)
GPIO.output(17,GPIO.LOW)

port = 1
address = 0x77 # Adafruit BME280 address. Other BME280s may be different
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

def verifAmbient(temp_min, temp_max, hum_min, hum_max) :
    if ambient_temperature < temp_min or ambient_temperature > temp_max :
        GPIO.output(27, GPIO.HIGH)
    else :
        GPIO.output(27, GPIO.LOW)
    if humidity < hum_min or humidity > hum_max :
        GPIO.output(17, GPIO.HIGH)
    else :
        GPIO.output(17, GPIO.LOW)

verif = False
while verif == False :
    choix = input('Quelle plantation souhaitez-vous optimiser ?')
    if(choix == 'TOMATE' or choix == 'CAROTTE' or choix == 'CONCOMBRE') :
        verif = True

while True:
    bme280_data = bme280.sample(bus,address)
    humidity  = bme280_data.humidity
    pressure  = bme280_data.pressure
    ambient_temperature = bme280_data.temperature
    if choix == 'TOMATE' :
       verifAmbient(20, 25, 50, 70)
    elif choix == 'CAROTTE':
        verifAmbient(16, 23, 45, 65)
    elif choix == 'CONCOMBRE' :
        verifAmbient(18, 26, 60, 70)
    print(humidity, pressure, ambient_temperature)
    sleep(1)