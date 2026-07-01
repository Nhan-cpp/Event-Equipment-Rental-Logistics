from models.Equipment import equipment
def main():
    test = equipment("12124124",0.2,-1,True)
    test.ID = "1_"
    print(test.ID)
if __name__ == "__main__":
    main()