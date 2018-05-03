import mymodule1
import mymodule2
def main():
    print( (mymodule2.myage - mymodule1.myage) == (mymodule2.year - mymodule1.year))
    print("My name is", __name__)
if __name__=="__main__":
    print("This won't run if I'm imported.")
    main()