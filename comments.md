## General comments:

- In general, I'm used to working with Python, Flask, Postgres and Pytest, which help me advance a little more quickly.
- However, I have had a busy schedule these last days, so I didn't have a lot of free time to devote to the challenge.
- Integrating the BDD tests was a challenging task, and something I had never done in Python, but I think it was a good exercise.
- Using flask-openapi to generate the documentation was also a challenge, since I had never used it before. But I think some of it requirements (RequestBodys, Responses, Paths, Headers), while sometimes annoying, also help you orgnize your code in some aspects.
- I didn't comment every method of every class, because I believe most of them are self-explanatory.

### Testing

- Creation, update and deletion tests are done at repository level, not at model level.
- Couldn't include tests for ObjectNotFoundException, which had in my opinion a lower priority than the others.
- I decided to use BDD tests for integration, because I find them to be very easy to read and understand.
- However, I could not find a way to use a test database for them, so they run against the real app. I had to add an endpoint to reset the database, which is not a secure option, although it checks against an environment variable before doing anything.
- I wanted to include more scenarios in BDD features, but I still think I tested the most important general cases.
- I also couldn't add a test for the "days since creation" field in Publications, which is a calculated field.

### Design

- The system is a standard layered architecture for a backend web application. It consists of:
    - Blueprints, which handle the requests and return the responses. They are not standard classes, so I don't like giving them other responsabilites. Besides, they are a bit overloaded with validations required by the flask-openapi framework.
    - Controllers, which handle the flow of the requests.
    - Repositories, which handle the persistence of the data.
    - Models, which in this case are basically just tables turned into classes, which some minor logic validations.
    - Other classes:
        - Helper classes, which have varying purposes, but basically are used to help the controllers.
        - Exceptions, which are used to handle the exceptions thrown by the controllers.
        - The ExceptionHandler is a class which I like to use to handle any exception thrown in the process of a request. Controllers/blueprints can delegate the exception handling to this class, wrapping their methods in just one try/except block.
        - Schemas, which I used only to serialize the models data to be returned in the responses.
        - RequestHelpers, which are basically used to organize both the requests and responses formats, and needed by flask-openapi to be able to document the api automatically.
- Even though it was stated that only Publications should have created_at and updated_at fields, I decided those fields to be included in the Base Model, because I believe they could be useful for every model.
- For simplicity, users photos are just a string that represents the path to the photo.