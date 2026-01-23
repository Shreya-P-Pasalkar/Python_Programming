def ChkPrime(No) :
    iSum = 0

    for i in range(1,No) :
        if(No%i == 0) :
            iSum = iSum + 1

    if (iSum == 1) :
        return True
    else :
        return False

