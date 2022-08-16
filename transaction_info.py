import random

def main():

    
    trans = transactionTest() 
    paymentType = trans[0]
    trans.remove(trans[0])
    print(paymentType, ":",trans)

def transactionTest():
        
    

    payment_type = [ "Credit Card", "Venmo", "Google pay", "Apple pay", "Cash app", "Gift card", "Paypal"]
    fail_reason_card1 = ["Failed to Authenticate buyer","Card reported stolen", "Insuffecient Funds", "Incorrect CCV", "Card Type Not Supported"]
    fail_reason_card2 = ["Insuffecient Funds", "Incorrect CCV", "Gift Card Type Not Supported"]
    fail_reason_app = ["Failed to Authenticate buyer", "Payment site timed out", "Insuffecient Funds"]

    payment_type = [ "Credit Card", "Venmo", "Google pay", "Apple pay", "Cash app", "Gift card", "Paypal", "Souls of my Enemys"]
    fail_reason_card1 = ["Failed to Authenticate buyer","Card reported stolen", "Insuffecient Funds", "Incorrect CCV", "Card Type Not Supported"]
    fail_reason_card2 = ["Insuffecient Funds", "Incorrect CCV", "Gift Card Type Not Supported"]
    fail_reason_app = ["Failed to Authenticate buyer", "Payment site timed out", "Insuffecient Funds"]
    fail_reason_soul = ["Insuffecient Souls", "Soul type not excepted", "What is this, Why is it screaming"]

    payment_info = []
    payment_info.append(random.choice(payment_type))

    if random.randint(1,100) > 50:
        payment_info.append("Y")
    else:
        payment_info.append("N")
        if payment_info[0] == "Credit Card":
            payment_info.append(random.choice(fail_reason_card1))
        elif payment_info[0] == "Gift Card":
            payment_info.append(random.choice(fail_reason_card2))
        elif payment_info[0] == "Souls of my Enemys":
            payment_info.append(random.choice(fail_reason_soul))
        else:
            payment_info.append(random.choice(fail_reason_app))        
    
    return payment_info
main()