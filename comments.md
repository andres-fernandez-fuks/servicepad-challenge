## General comments:

### Testing

- Creation, update and deletion tests are done at repository level, not at model level.

### Design

- Even though it was stated that only Publications should have created_at and updated_at fields, I decided those fields to be included in the Base Model, because I believe they could be useful for every model.