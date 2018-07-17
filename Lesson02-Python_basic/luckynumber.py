def guess_luckynumber():
    import random
    lucky_number=random.randint(1,100)
    number=int(input("清輸入終極密碼:"))
   
    while number!= lucky_number:  
        if number<lucky_number:
            print ("再大一點")
            number=int(input("Please enter an luncky number:"))
        else:
            print ("再小一點")
            number=int(input("Please enter an luncky number:"))
    print ("猜對了！")   
    
guess_luckynumber()