import math
import time
from max30105 import MAX30105, HeartRate
import smbus
from bme280 import BME280
import socket
#from matplotlib import pyplot as plt


class DataPoint():
    def __init__(self,value,time):
        self.time_stamp = time
        self.value = value

        



class Device():
    def __init__(self):
        self.humidity = []
        self.temperature = []
        self.smoke_level = []
        self.mean_size = 100
        self.identifier = "0,0"

    def setup_network(self):
        self.network = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connected = False
        while not connected:
            try:
                self.network.connect(("192.168.88.167",25565))
                connected = True
            except:
                a = 1
    
    def upload_data(self):
        network_string = (#str(round(self.calculate_humidity_trend(),5)) + "," +
                          str(round(self.humidity[-1].value,5)) + "," +
                          #str(round(self.calculate_temperature_trend(),5)) + "," +
                          str(round(self.temperature[-1].value,5)) + "," +
                          #str(round(self.calculate_smoke_level_trend(),5)) + "," +
                          str(round(self.smoke_level[-1].value,5)) + "," +
                          str(round(self.pressure.value,5)) + "," +
                          str(self.identifier))
        
        network_string = network_string.encode()
        self.network.sendall(network_string)
        
    
    def update(self):
        dev.get_smoke_data()
        dev.get_humi_temp_data()

    def setup_particle_sensor(self):
        self.MAX30105 = MAX30105()
        self.MAX30105.setup(leds_enable=3)
        self.MAX30105.set_led_pulse_amplitude(1,0.0)
        self.MAX30105.set_led_pulse_amplitude(2,0.0)
        self.MAX30105.set_led_pulse_amplitude(3,12.5)

        self.MAX30105.set_slot_mode(1,"red")
        self.MAX30105.set_slot_mode(2,"ir")
        self.MAX30105.set_slot_mode(3,"green")
        self.MAX30105.set_slot_mode(4,"off")
        self.hr = HeartRate(self.MAX30105)

    def setup_temp_humi_sensor(self):
        bus = smbus.SMBus(1)
        self.bme280 = BME280(i2c_dev=bus)

    def setup_sensors(self):
        self.setup_particle_sensor()
        self.setup_temp_humi_sensor()

    def get_smoke_data(self):
        data = []
        for i in range(self.mean_size*3+1):
            samples = self.MAX30105.get_samples()
            if samples is not None:
                for sample in samples:
                    r = samples[2] & 0xff
                    d = self.hr.low_pass_fir(r)
                    data.append(d)
        
        mean = sum(data)/(self.mean_size*3)
                
        self.smoke_level.append(DataPoint(mean,time.time))

    def get_humi_temp_data(self):
        temp_data = []
        humi_data = []
        pres_data = []
        for i in range(self.mean_size):
            temp_data.append(self.bme280.get_temperature())
            humi_data.append(self.bme280.get_humidity())
            pres_data.append(self.bme280.get_pressure())

        mean_temp = sum(temp_data)/self.mean_size
        mean_humi = sum(humi_data)/self.mean_size
        mean_pres = sum(pres_data)/self.mean_size

        
        self.humidity.append(DataPoint(mean_humi,time.time()))
        self.temperature.append(DataPoint(mean_temp,time.time()))
        self.pressure = DataPoint(mean_pres,time.time())
    

    """def calculate_humidity_trend(self):
        return self.lin_reg(self.humidity)

    def calculate_temperature_trend(self):
        return self.lin_reg(self.temperature)

    def calculate_smoke_level_trend(self):
        return self.lin_reg(self.smoke_level)

    def lin_reg(self,data_set):
        x = 0
        Sxy = 0
        Sx = 0
        Sx2 = 0
        Sy = 0
        Sy2 = 0
        sample_size = len(data_set)
        for y in data_set:
            y=y.value
            x += 1
            Sxy += x * y
            Sx += x
            Sx2 += x**2
            Sy += y
            Sy2 += y**2
            
        
        lin_reg = ((sample_size*Sxy)-(Sx*Sy))/((sample_size*Sx2)-(Sx)**2)
        return lin_reg"""


dev = Device()
dev.setup_sensors()
dev.setup_network()
for i in range(2):
    dev.update()
while True:
    try:
        dev.update()
        dev.upload_data()
        print("sending_data")
    except:
        dev.setup_network()
    



