import serial
import serial.tools.list_ports
import os
import sys
import logging
import argparse
import random
import pprint
import glob
import subprocess
import time
import webcam
import gdrive
import email_noti
import location
import DAO
from datetime import datetime

# Configure logging
logging.basicConfig(
    format="%(asctime)s %(levelname)s %(filename)s:%(funcName)s():%(lineno)i: %(message)s", 
    datefmt="%Y-%m-%d %H:%M:%S", 
    level=logging.DEBUG)
logger = logging.getLogger(__name__)

def print_serial_ports() -> None:
    # Device filter. micro:bit = "0D28:0204", Arduino Nano 33 BLE Sense = "2341:805A"
    vidpid_filter = [ "0D28:0204", "2341:805A" ] 

    # get list of serial ports
    ports = list(serial.tools.list_ports.comports())
    
    # print ports
    print("Ports found:")
    for port in ports:
        if any(x.upper() in port[2].upper() for x in vidpid_filter):
            identifier = port.hwid.split(' ')[2].split('=')[1]
            print(f"{port.device}")
            print(f"    desc: {port.description}")
            print(f"    hwid: {port.hwid}")
            files = glob.glob(f"/dev/serial/by-id/*{identifier}*")
            for file in files:
                print(f"    device alias: {file}")
        print()


def loop(serial_port: str) -> None:
    # open the serial port
    with serial.Serial(serial_port, 115200, timeout=1) as s:
        print("Press Ctrl-C to stop")
        print("--------------------")

        try:
            # loop forever
            while True:

                # read a line from the serial port, as bytes
                line = s.readline()

                # # read a line from the serial port, decode bytes to string
                line = line.decode('utf-8')

                # message should end with \n, this removes the \n and all other whitespace before and after the message
                line = line.strip()

                # if the read was successful, do something with it
                if line:
                    print(f"{line}")

                    # If collision detected
                    if line == '1':
                        video_file = webcam.start_recording() # open camera, return timestamp.mp4
                        print("Recording video...")

                        file_id = gdrive.upload_video_googledrive(video_file) # send to gdrive
                        print("Successfully uploaded to google drive!")

                        file_link = f"https://drive.google.com/file/d/{file_id}/view?usp=drive_link"
                        address, lat, long  = location.get_address()
                        email_noti.send_email(file_link, address) # send email
                        print("Successfully emailed user!")

                        date_time = video_file[:-4].replace("_", " ").replace("-", ":") + " GMT+0800 (Singapore Standard Time)" # get datetime -> remove .mp4 from filename
                        bus = random.randint(1, 999)
                        country = 'Singapore'
                        date =  datetime.strptime(video_file[:-4], "%a_%b_%d_%Y_%H-%M-%S").strftime("%d/%m/%Y")
                        timestamp =  datetime.strptime(video_file[:-4], "%a_%b_%d_%Y_%H-%M-%S").timestamp()
                        postalCode = ''
                        print(bus, file_link, date_time, address, date, lat, long, postalCode, country, timestamp)
                        request_status = DAO.send_data(bus, file_link, date_time, address, date, lat, long, postalCode, country, timestamp) # send to database
                        print(request_status) # "Successfully sent to database!" / error message

        except KeyboardInterrupt:
            print()
            print("kthxbye")

def main() -> None:
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("port", nargs="?")
    args = parser.parse_args()
    args_port = args.port

    if args_port:
        print_serial_ports()
        print(f"Using serial port: {args_port}")
    else:
        print(f"Error: must specify the serial port 💤")
        print(f"Example:")
        print()
        print(f"    python {os.path.basename(__file__)} INSERT_YOUR_SERIAL_PORT_HERE")
        print()
        print(f"Huh, simi serial port? See below for possible serial ports:")
        print_serial_ports()
        exit()

    loop(args_port)

if __name__ == "__main__":
    main()