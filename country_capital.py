import csv

def main():
    country = raw_input("Enter a Country name: \n").lower()
    search(country)

def try_again():
    play = raw_input("Do you want to play again: Y/N \n")
    if play=="Y":
        main()
    elif play=="N":
        print "Thankyou for playing"
    else:
        print "Please insert correct letter"
        try_again()
        
    

def search(country):
    wikiOpen=open('capital_cities.csv')
    wikiRead = csv.reader(wikiOpen)
    wikiData = list(wikiRead)
    wikiLen = len(wikiData)
    flag=0
    for i in range(1,wikiLen):  
        if country == wikiData[i][0].lower():
            flag+=1
            print wikiData[i][1]
    if flag !=1:
        print "Country is not in the index"
    else:
        try_again()

main()
