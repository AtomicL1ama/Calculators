#Small calculator for assisting in the subnet pre-lab for CS4121, Fall2022
#Written by Garrett Moore, Nov 2 2022

import math

def getBitSize(n):
    p = 0
    while (math.pow(2,p)<(n+3)):
        p += 1
    return p

def allocateAddresses(firstAddressSpace, hostRequestList):
    hostRequestList.sort(reverse = True)
    numSubnets = len(hostRequestList)
    print("\nNumber of subnets = " + str(numSubnets))
    nextAddressSpace = firstAddressSpace
    for x in range(numSubnets):
        print("\nLAN " + str(x) + ":")
        numHosts = hostRequestList[x]
        bitSize = getBitSize(numHosts)
        subnetRange = int(math.pow(2,bitSize))
        nextAddressSpace += subnetRange
        printSubnet(numHosts, bitSize, subnetRange, nextAddressSpace)    
    
def printSubnet(numHosts, bitSize, subnetRange, nextAddressSpace):
    network = nextAddressSpace - subnetRange
    gateway = network +1
    broadcast = nextAddressSpace -1 
    msg = "   Hosts =  " + str(numHosts)
    msg += "\n   bitSize =  " + str(bitSize)
    msg += "\n   Subnet Mask       =\t255.255.255." + str(256-subnetRange)
    msg += "\n   Network Address   =\t10.10.172." + str(network) 
    msg += "\n   Gateway Address   =\t10.10.172." + str(gateway) 
    msg += "\n   Broadcast Address =  10.10.172." + str(broadcast)
    msg += "\n   Host Range:       =\t10.10.172." + str(gateway+1) + " - 10.10.172." + str(broadcast-1)
    print(msg)
    
def initialize():
    print("\n################ [subnet_calculator.py] ################\n")
    firstAddressSpace = input("Enter first address space integer (i.e. 10.10.172.X): ")
    addMore = True
    hostRequestList = []
    hostRequestList.append(int(input("Enter requested host size: ")))
    addMore = input("Add additional LAN? (y/n): ")
    while (addMore.capitalize() == 'Y'):
        hostRequestList.append(int(input("Enter another requested host size: ")))
        addMore = input("Add additional LAN? (y/n): ")
    allocateAddresses(int(firstAddressSpace),hostRequestList)
    print("\n################\n")
    
###############################

initialize()

###############################

        
    