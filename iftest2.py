# various ipchk scripts

# script 1
ipchk = "192.168.0.1"
if ipchk:
    print("Looks like the IP address was set: " + ipchk)

# script 2
ipchk = input("Apply an IP address: ")
if ipchk:
    print("Looks like the IP address was set: " + ipchk)

#script 3
ipchk = input("Apply an IP address: ")
if ipchk:
    print("Looks like the IP address was set: " + ipchk)
else:
    print("You did not provide input.")

# script 4
ipchk = input("Apply an IP address: ")

# if user set IP of gateway
if ipchk == "192.168.70.1":
   print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
elif ipchk:
   print("Looks like the IP address was set: " + ipchk)
else: # if data is NOT provided
   print("You did not provide input.")





