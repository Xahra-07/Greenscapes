
### Python Script to Send Data to Azure IoT Hub

import serial
import time
from azure.iot.device import IoTHubDeviceClient, Message

# Azure IoT Hub connection string
CONNECTION_STRING = "YourAzureIoTHubConnectionString"

# Serial port settings for Aeroqual Series 500
SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

def read_sensor_data():
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=10) as ser:
            # Read data from Aeroqual Series 500
            data = ser.readline().decode().strip()
            return data
    except Exception as e:
        print("Error reading sensor data:", str(e))
        return None

def send_to_azure(data):
    try:
        # Create IoT Hub client
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

        # Create message
        message = Message(data)

        # Send message to Azure IoT Hub
        client.send_message(message)
        print("Message sent to Azure IoT Hub:", data)
    except Exception as e:
        print("Error sending data to Azure IoT Hub:", str(e))

def main():
    while True:
        # Read data from Aeroqual Series 500
        sensor_data = read_sensor_data()

        if sensor_data:
            # Send data to Azure IoT Hub
            send_to_azure(sensor_data)

        # Adjust the time interval based on your requirements
        time.sleep(60)  # Data collection interval (seconds)

if __name__ == "__main__":
    main()
