def FV_loan(PV: float, PM: float, i: float, n:float, t: float) -> float:
    """
    Calculates the Future value of a loan after `n` x `t` interest cycles, where ...
    `i` / `n` is the interest rate per cycle, and the present value `PM` is defined.
    If fv is < 0, we set fv = 0.


    :param PV: Present value of the loan ($)
    :param PM: Payment Rate of the loan ($/cycle)
    :param i:  interest rate per year `t`
    :param t:  high level cycles
    :param n:  cycles per `t` level cycle
    :return:   Future value of the loan after `n` x `t` cycles
    """
    fv = PV*(1+i/n)**(n*t) - PM/(i/n)*((1+(i/n))**(n*t) - 1)
    if fv < 0:
        fv = 0

    return fv


print(FV_loan(50000,1000,0.05,12,10))


# EOF
