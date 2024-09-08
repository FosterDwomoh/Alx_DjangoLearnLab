from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.PositiveIntegerField()
    #Foreign key to the author model
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

        def __str__(self):
            return self.title

class BookFilter(filters.FilterSet):
    title = filters.CharField(lookup_expr='icontains')
    author = filters.CharField(field_name='author_name', lookup_expr = 'icontains')
    publication_year = filters.NumberField()

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']