import random

score = 0
ran = 500
primelist = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311,
313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401,
409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487,
491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593,
599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677,
683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773,
787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881,
883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997)

def isprime(number):
    if number in primelist:
        return True
    else:
        return False

def finddivisors(number):
    if isprime(number)==True:
        return([number])
    divisors=[]
    for i in range(2,number):
        if number%i==0:
            if isprime(i) == True:
                divisors.append(i)
            else:
                divs = finddivisors(i)
                for j in range(0,len(divs)):
                    divisors.append(divs[j])

    return divisors



#print set(finddivisors(812))
def test(integer,factors,saidfactors,attempts):
    if attempts>9:
        print "Sorry, to many attempts. The factors were:"
        print str(factors)
        main()
    factor = input("What are the prime factors of "+str(integer)+"? ")
    if factor not in factors:# and factor not in saidfactors:
        print "Nope, that is not a prime factor sorry!"
        print ""
        attempts+=1
        test(integer,factors,saidfactors,attempts)
    if factor in saidfactors:
        print "Sorry, you said that already"
        print ""
        test(integer,factors,saidfactors,attempts)
    else:
        saidfactors.append(factor)
        print "Yeap, that is a factor!"
        print ""
        if set(factors) == set(saidfactors):
            print "You got all the factors. Congratulations! The factors are " + str(factors)
            print ""
            main()
        else:
            test(integer,factors,saidfactors,attempts)

def list_primes():
    k=0
    wrong = False
    while wrong == False:
        guess = input("What prime comes next? ")
        if(guess == primelist[k]):
            guesses = primelist[0:(k+1)]
            k += 1
            print "That is correct, the first "+str(k)+" primes are "
            print str(guesses)+"."
            print ""

        else:
            wrong = True
    print "Ooops, that is not the next prime, the next prime was " + str(primelist[k])
    list_primes()

def main():
    integer = random.randrange(0,ran)
    factors = set(finddivisors(integer))
    test(integer,factors,[],0)

def game_play():
    game = input("What game do you want? Factors (1) or Primelist (2) ")
    if game == 1:
        ran = input("Up to what number? ")
        main()
    if game == 2:
        list_primes()
    else:
        print "Must enter valid game."
        game_play()

game_play()
