import threading

def Display():          # Callback Function :- no call but somebody runs you(thread)
    print("Inside Display Function : ",threading.get_ident())

def main():
    print("Inside main : ",threading.get_ident())

    t = threading.Thread(target=Display)
    t.start()

    print("End of main")
    
if __name__ == "__main__" :
    main()