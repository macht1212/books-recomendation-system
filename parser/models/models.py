from pydantic import BaseModel


class AuthorModel(BaseModel):
    """
    Summary
        The AuthorModel class is a Pydantic model that represents an author with three fields: id, firstname, and
        lastname.

    Main functionalities
        The main functionality of the AuthorModel class is to provide a structured representation of an author with
        three fields: id, firstname, and lastname. It ensures that the values assigned to these fields are of the
        correct type.

    Methods
        The AuthorModel class does not have any additional methods. It inherits the methods from the BaseModel class
        provided by Pydantic.

    Fields
        id: An integer field representing the ID of the author.
        firstname: A string field representing the first name of the author.
        lastname: A string field representing the last name of the author.
    """
    id: int
    firstname: str
    lastname: str


class CategoryModel(BaseModel):
    """
    Summary
        The CategoryModel class is a Pydantic model that represents a category with an id and a title field.

    Main functionalities
        The main functionality of the CategoryModel class is to provide a structured representation of a category with
        two fields: id and title. It ensures that the values assigned to these fields are of the correct type.

    Methods
        The CategoryModel class does not define any additional methods.

    Fields
        id: An integer field that represents the ID of the category.
        title: A string field that represents the title of the category.
    """
    id: int
    title: str


class PublisherModel(BaseModel):
    """
    Summary
        The PublisherModel class is a Pydantic model that represents a publisher. It has two fields: id of type int and
        title of type str.

    Main functionalities
        The main functionality of the PublisherModel class is to provide a structured representation of a publisher. It
        ensures that the id field is of type int and the title field is of type str.

    Methods
        The PublisherModel class does not have any additional methods. It inherits the methods from the BaseModel class
        provided by Pydantic.

    Fields
        id: Represents the unique identifier of the publisher. It is of type int.
        title: Represents the title or name of the publisher. It is of type str.
    """
    id: int
    title: str


class BookModel(BaseModel):
    """
    Summary
        The BookModel class is a Pydantic model that represents a book. It defines the structure and validation rules
        for the book data.

    Main functionalities
        The main functionalities of the BookModel class are:
        Defining the structure of a book object with fields such as id, author, category, publisher, title, description,
        rating, and votes.
        Applying validation rules to ensure that the provided data meets the defined structure and constraints.

    Methods
        The BookModel class does not have any custom methods. However, it inherits methods from the BaseModel class
        provided by Pydantic, which include:
        __init__: Initializes the book object with the provided data.
        __repr__: Returns a string representation of the book object.
        dict: Returns the book object as a dictionary.
        json: Returns the book object as a JSON string.

    Fields
        The main fields of the BookModel class are:
        id: An integer representing the book's unique identifier.
        author: An integer representing the ID of the book's author.
        category: An integer representing the ID of the book's category. Defaults to 0 if not provided.
        publisher: An integer representing the ID of the book's publisher. Defaults to 0 if not provided.
        title: A string representing the title of the book.
        description: A string representing the description of the book.
        rating: A float representing the rating of the book. Defaults to 0.0 if not provided.
        votes: An integer representing the number of votes the book has received. Defaults to 0 if not provided.
    """
    id: int
    author: int
    category: int = 0
    publisher: int = 0
    title: str
    description: str
    rating: float = .0
    votes: int = 0


class UserModel(BaseModel):
    """
    Summary
        The UserModel class is a Pydantic model that represents a user with an id field.

    Main functionalities
        The main functionality of the UserModel class is to define the structure and validation rules for a user object.
        It ensures that the id field is of type int.

    Methods
        The UserModel class does not have any additional methods.

    Fields
        The UserModel class has one field:
        id: Represents the unique identifier of the user. It is of type int.
    """
    id: int


class UserBooksModel(BaseModel):
    """
    Summary
        The UserBooksModel class is a Pydantic model that represents a user's book. It has three fields: id, book_id,
        and user_id.

    Main functionalities
        The main functionality of the UserBooksModel class is to provide a structured representation of a user's book.
        It ensures that the provided data adheres to the defined field types.

    Methods
        The UserBooksModel class does not have any additional methods. It inherits the methods from the BaseModel class
        provided by Pydantic.

    Fields
        id: An integer field representing the ID of the user's book.
        book_id: An integer field representing the ID of the book.
        user_id: An integer field representing the ID of the user.
    """
    id: int
    book_id: int
    user_id: int


class UserPreferencesModel(BaseModel):
    """
    Summary
        The UserPreferencesModel class is a Pydantic model that represents user preferences for a book. It has three
        fields: id, book_id, and user_id.

    Main functionalities
        The main functionality of the UserPreferencesModel class is to provide a structured representation of user
        preferences for a book. It ensures that the values assigned to the fields are of the specified types (int in
        this case) and enforces data validation.

    Methods
        The UserPreferencesModel class does not have any additional methods. It inherits the methods from the BaseModel
        class provided by Pydantic, which include methods for data validation, serialization, and deserialization.

    Fields
        id: An integer field representing the unique identifier of the user preference.
        book_id: An integer field representing the unique identifier of the book associated with the user preference.
        user_id: An integer field representing the unique identifier of the user associated with the preference.
    """
    id: int
    book_id: int
    user_id: int




