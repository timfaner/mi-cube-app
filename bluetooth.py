# Search for BLE UART devices and list all that are found.
# Author: Tony DiCola
import atexit
import time,random
from cube_parser import parseCube
from cube_event import Cube

import Adafruit_BluefruitLE
from Adafruit_BluefruitLE.services import DeviceInformation
import uuid 

import gui
import threading


DEVICE_UUID=uuid.UUID('f9c2bf43-8bab-4faf-92d9-3a34e0ce9f32')
UART_SERVICE_UUID = uuid.UUID("0000aadb-0000-1000-8000-00805f9b34fb")
TX_CHAR_UUID = uuid.UUID("0000aadb-0000-1000-8000-00805f9b34fb")


def getRandomMove():
    l = ('F','R','D','B','L','U')
    rnd = random.randint(0,5)
    rnd1 = random.randint(0,1)
    suffix = "'" if rnd1==0 else ""
    return l[rnd]+suffix




f = ""

flags=""

cube = Cube() 


def received(data):
    global f,flags

    

    d = parseCube(data)
    try:
        olddata = cube.data_face

        ret = cube.update(d)
        if "'" in ret:
            ret = ret[0].lower()
        flags = flags+ret
        gui.updatetext(flags)
        if f == "":
            pass
        elif f == ret:
            print("Move passed : {}".format(f))
        else:
            print("Move failed :")
            print(olddata)
            print(d)
        #print('Received: {0}'.format(d))
    except Exception as e:
        print(e)
        print(olddata)
        print(d)
    print("===========================")

    f = getRandomMove()
    print("Next move ===>  {}".format(f))


# Get the BLE provider for the current platform.
ble = Adafruit_BluefruitLE.get_provider()

# Main function implements the program logic so it can run in a background
# thread.  Most platforms require the main thread to handle GUI events and other
# asyncronous events like BLE actions.  All of the threading logic is taken care
# of automatically though and you just need to provide a main function that uses
# the BLE provider.




def main():
    global flags
    # Clear any cached data because both bluez and CoreBluetooth have issues with
    # caching data and it going stale.
    ble.clear_cached_data()

    # Get the first available BLE network adapter and make sure it's powered on.
    adapter = ble.get_default_adapter()
    adapter.power_on()
    print('Using adapter: {0}'.format(adapter.name))

    # Start scanning with the bluetooth adapter.
    adapter.start_scan()
    # Use atexit.register to call the adapter stop_scan function before quiting.
    # This is good practice for calling cleanup code in this main function as
    # a try/finally block might not be called since this is a background thread.
    #atexit.register(adapter.stop_scan)
    print('Searching for UART devices...')
    print('Press Ctrl-C to quit (will take ~30 seconds on OSX).')
    # Enter a loop and print out whenever a new UART device is found.
    known_uarts = set()
    d = []
    k = 0
    while k == 0:
        # Call UART.find_devices to get a list of any UART devices that
        # have been found.  This call will quickly return results and does
        # not wait for devices to appear.
        found = set(ble.find_devices())
        
        # Check for new devices that haven't been seen yet and print out
        # their name and ID (MAC address on Linux, GUID on OSX).
        new = found - known_uarts
        for device in new:
            print('Found UART: {0} [{1}]'.format(device.name, device.id,))
            if device.id == DEVICE_UUID:
                print("wa")
                d.append(device)
                k = 1
                break
        known_uarts.update(new)
        # Sleep for a second and see if new devices have appeared.
        time.sleep(1.0)

    device = d[0]
    device.connect()
    time.sleep(1)
    try:
        print('Discovering services...')
        #device.discover([UART_SERVICE_UUID], [TX_CHAR_UUID])

        #DeviceInformation.discover(device)

        #dis = DeviceInformation(device)
        #print(dis)
        # Find the UART service and its characteristics.
        uart = device.list_services()


        #rx = uart.find_characteristic(TX_CHAR_UUID)
        #time.sleep(2)
        
        c = uart[0].list_characteristics()
        rx = c[0]
        #print(uart.list_characteristics())
        #print(uart)
        # Function to receive RX characteristic changes.  Note that this will
        # be called on a different thread so be careful to make sure state that
        # the function changes is thread safe.  Use queue or other thread-safe
        # primitives to send data to other threads.
        # Turn on notification of RX characteristics using the callback above.
        print('Subscribing to RX characteristic changes...')
        rx.start_notify(received)
        # Now just wait for 30 seconds to receive data.
        print('Waiting Siganl to stop.')
        
        while flags != "UUUU":
            pass
        # Wait for service discovery to complete for at least the specified
        # service and characteristic UUID lists.  Will time out after 60 seconds
        # (specify timeout_sec parameter to override).
        pass
    finally:
        pass
    




def startble():
    ble.initialize()
    ble.run_mainloop_with(main)



t = threading.Thread(target=startble)



t.start()

gui = gui.Gui()
gui.start()

