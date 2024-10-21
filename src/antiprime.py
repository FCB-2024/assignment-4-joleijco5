## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT

def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

def is_antiprime(n):
    max_divisors = count_divisors(n)
    for i in range(1, n):
        if count_divisors(i) >= max_divisors:
            return False
    return True

def main(x=None):
    if x is None:
        try:
            x = int(input("Introdueix un nombre enter positiu: "))
        except ValueError:
            print("Please provide a valid integer.")
            return "not anti-prime"
    if x <= 0:
        print("Si us plau, introdueix un nombre enter positiu.")
        return "not anti-prime"  
    if is_antiprime(x):
        return "anti-prime"
    else:
        return "not anti-prime"

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        try:
            x = int(sys.argv[1])
            if x <= 0:
                print("Si us plau, introdueix un nombre enter positiu.")
                print("not anti-prime")
            else:
                print(main(x))
        except ValueError:
            print("Please provide a valid integer.")
            print("not anti-prime")
    else:
        print(main())

	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"
	

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main())