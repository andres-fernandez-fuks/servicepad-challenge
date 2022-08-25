Feature: User CRUD management
    Scenario: User creation
        Given I am not currently an user
        When I create a new user
        Then I am an user with the correct data
        And I can login with my credentials

    Scenario: Correct user data obtention with the right credentials
        Given I am an user with certain data
        And I am logged in
        When I get my data
        Then I get the correct data


    Scenario: Correct user data edition with the right credentials
        Given I am an user with certain data
        And I am logged in
        When I edit my data
        Then my data is updated

    Scenario: Correct user data deletion with the right credentials
        Given I am an user with certain data
        And I am logged in
        When I delete my account
        Then I am not an user anymore

    Scenario: Cannot get user data with the wrong credentials
        Given I am an user with certain data
        And I am logged in as another user
        When I edit my data
        Then I get an Ownership error

    Scenario: Cannot get user data without credentials
        Given I am not logged in
        When I edit my data
        Then I get an Authentication error
    
