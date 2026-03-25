from django.db import models



class Car(models.Model):
    title = models.TextField(max_length=250)
    year = models.TextField(max_length=4, null=True)

    def __str__(self):
        return f"{self.title} ({self.year})" if self.year else self.title


class Publisher(models.Model):
    name = models.TextField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.TextField(max_length=200)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    author = models.OneToOneField(
        Author, related_name="author", on_delete=models.CASCADE
    )
    website = models.URLField()
    biography = models.TextField(max_length=500)

    def __str__(self):
        return self.auto_field


class Book(models.Model):
    title = models.TextField(max_length=200)
    publication_date = models.DateField()
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name="authors")

    def __str__(self):
        return self.title
