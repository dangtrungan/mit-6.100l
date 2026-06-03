## 6.100A PSet 1: Part C
## Name: Dang Trung An
## Time Spent: 1:00
## Collaborators: None

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_of_dream_home = 800000
portion_down_payment = 0.25
cost_of_down_payment = cost_of_dream_home * portion_down_payment

months = 36
epsilon = 100
steps = 0

low = 0
high = 1
r = (high + low) / 2
amount_saved = initial_deposit * (1 + high / 12) ** months  # maximum savings in 36 months

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
if initial_deposit >= cost_of_down_payment:
    r = 0.0

elif amount_saved < cost_of_down_payment:
    r = None

else:
    while abs(amount_saved - cost_of_down_payment) > epsilon:
        amount_saved = initial_deposit * (1 + r / 12) ** months
        if amount_saved < cost_of_down_payment:
            low = r
        else:
            high = r
        r = (high + low) / 2
        steps += 1

print(f"Best savings rate: {r}")
print(f"Steps in bisection search: {steps}")
