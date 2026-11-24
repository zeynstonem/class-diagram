# Book Class Diagram to Python Implementation

This repository contains a simple Python implementation of a **Book** UML class diagram.

## UML Class Diagram

```mermaid
classDiagram
    class Book {
        +str title
        +str author
        +bool is_available
        +borrow()
        +return_book()
        +show_info()
    }

"""
Class Overview
Attributes:
title: Title of the book.
author: Author of the book.
is_available: Shows whether the book is available to borrow (True or False).
Methods:
borrow(): Marks the book as borrowed if it is available.
return_book(): Marks the book as available again.
show_info(): Prints the book's title, author, and availability status.

"""


