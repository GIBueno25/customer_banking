# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    print("\nSavings Account:")

    balance = float(input("Enter the savings account balance: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    months = int(input("Enter the number of months: "))
    
    # Ensure all values are of the correct data type and non-negative
    if balance < 0 or interest_rate < 0 or months < 0:
        print("All values must be non-negative.")
        return

    # Call the create_savings_account function and pass the variables from the user.
    updated_balance, interest_earned = create_savings_account(balance, interest_rate, months)
  
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"\nFor a period of {months} month(s):")
    print(f"Interest Earned: ${interest_earned:,.2f}")
    print(f"Updated Savings Account Balance: ${updated_balance:,.2f}\n")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    print("\nCD Account:")

    cd_balance = float(input("Enter the CD account balance: "))
    cd_interest_rate = float(input("Enter the interest rate (as a percentage): "))
    cd_months = int(input("Enter the number of months: "))

    # Ensure all values are of the correct data type and non-negative
    if cd_balance < 0 or cd_interest_rate < 0 or cd_months < 0:
        print("All values must be non-negative.")
        return

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"\nFor a period of {cd_months} month(s):")
    print(f"Interest Earned (CD): ${cd_interest_earned:,.2f}")
    print(f"Updated CD Account Balance: ${updated_cd_balance:,.2f}\n")

if __name__ == "__main__":
    # Call the main function.
    main()
