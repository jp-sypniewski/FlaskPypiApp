## PyPI Mock App

### A data-driven web app with Flask and SQLAlchemy

#### Description

This application is a full build of a mock-PyPI site, using the Flask web framework with MongoDB.  Users register and log in to the application, at which point they may interact with the "packages" stored by the application.

#### Purpose

This project was undertaken first to utilize SQLAlchemy, with practice on the Flask framework and in the PyCharm IDE of additional benefit.

For SQLAlchemy, I found the syntax familiar having just used JPA in Java/Spring projects.  The setup and usage of SQLite and Alembic were mostly new, but straightforward with the base class driving connections.  I found the relationships between objects to be more eloquent than that of JPA; specifically, SQLAlchemy was both deeper in ability to define relationships and able to do so in fewer lines.  I look forward to working with SQLAlchemy with both MongoDB and MySQL in future projects!

With the refactor to use MongoDB, I have now used a document-type database!  It seems to be straightforward, and I look forward to using it again after some other projects!

#### Technologies Used

* Flask
* Jinja2
* MongoDB
* pytest
* HTML
* CSS/Bootstrap

#### Next Steps

* Explore nuance of MVC v MVVM
* Explore deployment, SSL
