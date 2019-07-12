#!/usr/bin/python3
import time
import psutil

totalvalue = 0
old_value = 0   
def main():
    global totalvalue 
    global old_value
    try:
        while True:
            # Grabs the total number of data used at this time
            new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

            # skips the first one, since it's 0
            # then, we should get the difference since the last check and convert it to GB
            if old_value:
                send_stat(new_value - old_value)

            old_value = new_value

            time.sleep(.1)
    except KeyboardInterrupt:
        print ("\n\n"+ "%0.6f" % convert_to_gbyte(totalvalue) + "GB\n")
        main()

def convert_to_gbyte(value):
    #return value/1024./1024./1024
    return value/1000./1000./1000

def send_stat(value):
    #print ("%0.3f" % convert_to_gbit(value) + "GB")
    global totalvalue
    totalvalue += value

main()
print ("\n\n"+ "%0.6f" % convert_to_gbyte(totalvalue) + "GB\n")
