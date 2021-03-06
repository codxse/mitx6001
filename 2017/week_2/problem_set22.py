#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 17:41:11 2017

@author: Nadiar
"""

balance = 4773
annualInterestRate = 0.2

"""
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month =
    (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""

monthlyInterestRate = annualInterestRate / 12.0

def monthlyUnpaidBalance(balance, minimumFixedMonthlyPayment):
    return balance - minimumFixedMonthlyPayment

def updatedBalanceEachMonth(balance, minimumFixedMonthlyPayment):
    return monthlyUnpaidBalance(balance, minimumFixedMonthlyPayment) \
            + monthlyInterestRate * \
            + monthlyUnpaidBalance(balance, minimumFixedMonthlyPayment)
            
def loop(balance, minimumFixedMonthlyPayment, nMonth):
    if (nMonth < 1):
        return balance
    else:
        return loop(updatedBalanceEachMonth(balance, minimumFixedMonthlyPayment),
                    minimumFixedMonthlyPayment,
                    nMonth-1)

def isPaid(balance, minimumFixedMonthlyPayment):
    return loop(balance, minimumFixedMonthlyPayment, 12) <= 0

def main(minimumFixedMonthlyPayment):
    if isPaid(balance, minimumFixedMonthlyPayment):
        return minimumFixedMonthlyPayment
    else:
        return main(minimumFixedMonthlyPayment + 10)
        
print("Lowest Payment:", main(10))
        
