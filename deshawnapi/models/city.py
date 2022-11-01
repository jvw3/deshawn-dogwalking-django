from django.db import models # Import base class from Django stdlib


class City(models.Model): # Must inherit from this base class
    name = models.CharField(max_length=155) # Define all non-id fields
# You'll notice that only the name property is defined in the class. This is because when you generate a table from a database model, Django will automatically create the id column, make it the primary key, and set it to autoincrement whenever a new row is inserted.

# It's pretty handy... as long as you remember that it does it for you. Many a beginner defined the id field in their model class and ended up with 2 in the table.