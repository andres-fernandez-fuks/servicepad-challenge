Feature: Publication CRUD management
    Background: 
        Given I am an authenticated user
    Scenario: Publication creation
        When I create a new publication
        Then the publication is created and it's data is correct

    Scenario: Correct publication data obtention
        Given I created a publication
        When I get the publication data
        Then the publication data is correct

    Scenario: Correct publication update
        Given I created a publication
        When I update the publication
        Then the publication is updated

    Scenario: Correct publication deletion
        Given I created a publication
        When I delete the publication
        Then the publication is deleted
       
    Scenario: Cannot edit another user's publication
        Given I created a publication
        And I am logged in as another user
        When I try to update the publication
        Then I get an error message

    Scenario: Cannot delete publication without credentials
        Given I created a publication
        And I am not logged in as a user
        When I try to delete the publication
        Then I get an error message