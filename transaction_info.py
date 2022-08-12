import random


def main():
    count = 0
    while count < 10000:
        payment_type = [ "Credit Card", "Venmo", "Google pay", "Apple pay", "Cash app", "Gift card" "Paypal"]
        payment_success = ["Y" , "N" ]
        fail_reason_card1 = ["Failed to Authenticate buyer","Card reported stolen", "Insuffecient Funds", "Incorrect CCV", "Card Type Not Supported"]
        fail_reason_card2 = ["Insuffecient Funds", "Incorrect CCV", "Gift Card Type Not Supported"]
        fail_reason_app = ["Failed to Authenticate buyer", "Payment site timed out", "Insuffecient Funds"]
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
            else:
                payment_info.append(random.choice(fail_reason_app))        
        count += 1
        print(payment_info)
main()