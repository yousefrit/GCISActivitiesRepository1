''' This activity is done by Group 7 and is a currency converter that uses the basic concepts of
functions, loops, and mainly conditions to apply skills that we've picked up within the GCIS 123 Course
into real-world problems and to gain practical experience of problem solving skills.

This program allows users to convert currencies from AED to various other currencies, and vice-versa.

In accordance with the provided assignment:

This program uses the concept of incremental development which requires us to define many helper functions
with different useage and use them within one singular main function to make our program work effeciently.


There are various parts of this code mainly being:

Conversion Rates: These rates were globally assigned to a variable and used within our functions
Helper Functions: These functions such as aed_to_eur, helped us formulate the new conversion and returned it
Main Function: This was the main heart of our code, which first started with a custom Graphical User Interface
and then took inputs from the user which were used into if statements that would help convert the currencies
according to the input of the user.

Group 7
    1 - Yousef Al Salman, ysa1392
    2 - Ahmed Nayebkhil, asn7942
    3 - Omar Al Gendi, oae5541

Repository Links:

1- Yousef AlSalman:
2- Ahmed Nayebkhil:
3- Omar Al Gendi

                                                                                       '''
# Our constant conversion rates.
AEDtoEuroConversionRate = 0.25
AEDtobritishPoundConversionRate = 0.22
AEDtoDollarConversionRate = 0.27
DollarToAEDConversionRate = 3.67
britishPoundtoAEDConversionRate = 4.66
EurostoAEDConversionRate = 3.98


def aed_to_eur(money): # Function which uses the conversion rate to operate AED to Euros
    ConvertedAEDtoEuro = money * AEDtoEuroConversionRate
    return ConvertedAEDtoEuro

def aed_to_britishPound(money): # Function which uses the conversion rate to operate AED to GBP
    ConvertedAEDtoBritishPound = money * AEDtobritishPoundConversionRate
    return ConvertedAEDtoBritishPound

def aed_to_dollar(money): # Function which uses the conversion rate to operate AED to Dollars
    ConvertedAEDtoDollars = money * AEDtoDollarConversionRate
    return ConvertedAEDtoDollars

def dollar_to_aed(amount): # Function which uses the conversion rate to operate Dollars to AED
    DollarsConvertedtoAED = amount * DollarToAEDConversionRate
    return DollarsConvertedtoAED

def britishPound_to_aed(amount): # Function which uses the conversion rate to operate GBP to AED
    britishPoundConvertedtoAED = amount * britishPoundtoAEDConversionRate
    return britishPoundConvertedtoAED

def eur_to_aed(amount): # Function which uses the conversion rate to operate Euros to AED
    EurosConvertedtoAED = amount * EurostoAEDConversionRate
    return EurosConvertedtoAED


def main(): # The main function which will be the heart of our code and contain the functions and UI.
    ConditionMet = True # Loop condition incase we want to alter it later to false
    while ConditionMet == True: # our main loop so that the code repeats 
     print('"   Main Menu   "')
     print("Welcome to the Currency Converter") # Our basic text UI to guide the user
     print("-----------------------------------")
     print("Select the Conversion Direction: \n 1. AED to Other Currencies \n 2. Other Currencies to AED \n 3. Exit")
     Amount = int(input("Enter your amount you'd like to convert: ")) # First Input of money  to-be converted
     Money = int(input("Enter your choice (1/2/3): ")) # Decide the category
     if Money == 1: # check if its First category, AED to Other
         print(" 1. AED to Euro (EUR) \n 2. AED to British Pound (GBP) \n 3. AED to US Dollar \n 4. Exit")
         Subchoice = int(input("Enter the sub-choice of Currency: ")) # Take the sub choice if its first.
         if Subchoice == 1:
             ConvertedValues1 = aed_to_eur(Amount)
             print(Amount, "AED is equal to ", ConvertedValues1, "Euros")
         elif Subchoice == 2:
             ConvertedValues2 = aed_to_britishPound(Amount)
             print(Amount, "AED is equal to ", ConvertedValues2, "British Pound")
         elif Subchoice == 3:
             ConvertedValues3 = aed_to_dollar(Amount)
             print(Amount, "AED is equal to ", ConvertedValues3, "Dollars")
         elif Subchoice == 4:
             print("Program has been exited.")
             break
         Continue = input("Would you like to continue? Y/N: ")
         if Continue == "N":
             print("Program has been exited")
             break
     elif Money == 2: # Check If it's the second category
         print(" 1. Euro (EUR) to AED \n 2. British Pound (GBP) to AED \n 3. US Dollars to AED \n 4. Exit")
         Subchoice2 = int(input("Enter the sub-choice of currency: ")) # If it is, let the user choose a sub-category
         if Subchoice2 == 1:
             ConvertedValue = eur_to_aed(Amount)
             print(Amount, "Euros is equal to", ConvertedValue, "AED")
         elif Subchoice2 == 2:
             ConvertedValue2 = britishPound_to_aed(Amount)
             print(Amount, "British Pound is equal to", ConvertedValue2, "AED")
         elif Subchoice2 == 3:
             ConvertedValue3 = dollar_to_aed(Amount)
             print(Amount, "Dollars is equal to", ConvertedValue3, "AED")
         elif Subchoice2 == 4:
             print("Program has been exited.")
             break
         Continue2 = input("Would you like to continue? Y/N: ")
         if Continue2 == "N":
             print("Program has been exited.")
             break
     elif Money == 3: 
         print("Program has been exited.")
         break # Usage of break to end the loop has been seen many times in the code.


main()