#this program goes from m/s to mph

def main():
    print("i can convert meters per second into miles")
    meters_per_second =eval(input("what is the speed in m/s "))
    if meters_per_second < 0:
        print ("Invalid input!")
    else:
        mph = meters_per_second *2.23694
        print (mph,"mph")

main()
