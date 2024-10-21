## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT

x=int(input("Escribe un numero entero positivo "))

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

def main(x):
    if x <= 0:
        return "not anti-prime"
    if is_antiprime(x):
        return "antiprime"
    else:
        return "not anti-prime"

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <positive_integer>")
    else:
        try:
            x = int(sys.argv[1])
            print(main(x))
        except ValueError:
            print("Please provide a valid integer.")
            print("not anti-prime")



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
    print(main(x))