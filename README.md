# 4-1 Milestone: Create and Read in Python

## About the Project

This Python module aims to facilitate Create (C) and Read (R) operations for MongoDB, offering functionalities to insert documents into a specified collection and query documents based on specified criteria.

## Motivation

The motivation behind this project is to provide a simplified interface to interact with MongoDB databases for basic CRUD operations. It allows users to seamlessly insert documents into a MongoDB collection and retrieve documents based on specified criteria, simplifying the process of working with MongoDB databases in Python applications.

## Usage

### Create (C) Operation

To create (insert) a document into a specified collection, utilize the `create(data)` method from the `AnimalShelter` class in the `animalShelter` module. Pass a dictionary representing the document to be inserted as the `data` argument.

Example:
```python
from animalShelter import AnimalShelter

# Create an instance of AnimalShelter (CRUD)
crud = AnimalShelter("username", "password")

# Document to be inserted
data = {
    "animal_type": "Dog",
    "name": "Buddy",
    "breed": "Golden Retriever",
    # Additional fields...
}

# Insert the document into the collection
crud.create(data)
```

### Read (R) Operation

To read (query) documents from the collection based on specified criteria, utilize the `read(query)` method from the `AnimalShelter` class. Pass a dictionary representing the query criteria as the `query` argument.

Example:
```python
from animalShelter import AnimalShelter

# Create an instance of AnimalShelter (CRUD)
crud = AnimalShelter("username", "password")

# Query documents based on animal_type: Dog
query = {"animal_type": "Dog"}

# Retrieve documents matching the query criteria
documents = crud.read(query)
for doc in documents:
    print(doc)  # Displaying retrieved documents
```

For further usage examples, refer to the provided Jupyter Notebook `testMongoCRUD.ipynb`.

## Installation

### Tools Used

- **Python**: Programming language for module development.
- **MongoDB**: NoSQL database system for data storage.
- **PyMongo**: Python driver for MongoDB for Python-MongoDB interaction.
- **Spider IDE**: Integrated Development Environment used for Python code development.
- **Jupyter Notebook**: Interactive computational environment for creating and sharing documents containing live code, equations, visualizations, and narrative text.

The rationale for using these tools was their robustness, community support, and ease of integration for interacting with MongoDB databases within Python applications, along with the productivity and interactive features offered by Spider IDE and Jupyter Notebook for code development and documentation.

## Getting Started

To reproduce this project:

1. **Database Setup**: Set up a MongoDB instance with user authentication.
2. **Python Environment**: Install Python and PyMongo.
3. **Module Usage**: Import and instantiate the `AnimalShelter` class from the `mongoCRUD` module, then use the provided methods to perform CRUD operations as demonstrated above.


## Screenshots

![Screenshot 2023-11-20 at 3 17 24 AM](https://github.com/jaclynscarey/SNHU-CS-340-H7918/assets/109121563/68d11565-801f-4ad2-84a3-874e529bc735)

![Screenshot 2023-11-20 at 3 20 42 AM](https://github.com/jaclynscarey/SNHU-CS-340-H7918/assets/109121563/1d917118-7c03-4a64-99dc-a631aa4006fa)

![image](https://github.com/jaclynscarey/SNHU-CS-340-H7918/assets/109121563/a8579e9e-fc95-4408-aba3-72bc02a2c13b)

