

import string
import random

from paystack.resource import TransactionResource



def main():
    rand = ''.join(
        [random.choice(
            string.ascii_letters + string.digits) for n in range(16)])
    secret_key = 'sk_test_d6f931726274137ee0fb2dc8731fbe3ca8aa18e4'
    random_ref = rand
    test_email = 'beninn57@gmail.com'
    test_amount = '1000'
    plan = 'Basic'
    client = TransactionResource(secret_key, random_ref)
    response = client.initialize(test_amount,
                                 test_email,
                                 plan)
    print(response)
    client.authorize() # Will open a browser window for client to enter card details
    verify = client.verify() # Verify client credentials
    print(verify)
    print(client.charge()) # Charge an already exsiting client
main()