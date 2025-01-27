import ipaddress


def decimal(ip):
    try:
        numberconverted = int(ipaddress.ip_address(ip))
        return numberconverted
    except ValueError as error:
        return "invalid input: ", error ,"."
    
def binary(ip):
    try:
        binaryconverted = bin(int(ipaddress.IPv4Address(ip)))
        return binaryconverted
    except ValueError as errore:
        return "invalid input: ", errore ,"."

if __name__ == "__main__":
    userinput = input("Enter IP adress").strip()
    result = decimal(userinput)
    bresult = binary(userinput)
    print("Number conversion", result)
    print("Binary Conversion" )