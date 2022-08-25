Feature: Login management
    Background:
        Given I am a registered user
    Scenario: Login with valid credentials
        When I login with valid credentials
        Then I receive an authentication token
    Scenario: Login with invalid credentials
        When I login with invalid credentials
        Then I get an Authentication error
    Scenario: Logout
        Given I am logged in
        When I logout of the application
        Then I receive a successful response

