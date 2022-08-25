# Feature: Transaction processing
#     Scenario: Processing an income transaction
#         Given my account has a balance of 0
#         When an income transaction is created to my account with a value of 100
#         Then the balance of my account should be 100

#     Scenario: Processing an expenditure transaction with enough funds
#         Given my account has a balance of 100
#         When an expenditure transaction is created to my account with a value of 50
#         Then the balance of my account should be 50

#     Scenario: Processing an expenditure transaction without enough funds
#         Given my account has a balance of 50
#         When an expenditure transaction is created to my account with a value of 100
#         Then an error should be raised
#         And the balance of my account should be 50