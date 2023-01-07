email=input()
phno=input()
if (email.endswith("@gmail.com") or email.endswith("@yahoo.com") or email.endswith("@adc.aditya.ac.in")) and (phno.startswith("9") or phno.startswith("8") or phno.startswith("7") or phno.startswith("6")):
                                            print('registration succesful')
else:
    print('check emial and phone number')
   
