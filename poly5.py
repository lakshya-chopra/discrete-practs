def eval_poly(func:str,deg,val):

    coeffs = list(map(float,func.split()))

    sum_ = 0
    for i in coeffs:

        sum_ += i * val**deg
        deg -= 1
    return sum_

if __name__ == "__main__":

    func = input("Enter the polynomial coeffs (sep by a space): ")
    deg = int(input("DEGREE: "))
    val = float(input("Enter the varibale value: "))

    print(f"\nResult: {eval_poly(func,deg,val)}")