from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Book(BaseModel):
    title = models.CharField(max_length=200, null=False, blank=False)
    book_id = models.FloatField(null=False, blank=False)
    author = models.CharField(max_length=100, null=False, blank=False)
    genre = models.CharField(max_length=100, null=False, blank=False)
    publisher = models.CharField(max_length=100, null=True, blank=True)
    year = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.book_id} - {self.title}"

class User(BaseModel):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    user_id = models.IntegerField(null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10, null=False, blank=False, choices=GENDER)
    email = models.EmailField(max_length=100, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Librarian(BaseModel):
    DAY = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    birthdate = models.DateField()
    gender = models.CharField(max_length=10, null=False, blank=False, choices=GENDER)
    duty_day = models.CharField(max_length=50, null=False, blank=False, choices=DAY)

    def __str__(self):
        return self.name


class BorrowBook(BaseModel):
    librarian = models.ForeignKey(Librarian, blank=True, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    borrow_date = models.DateField()

    def __str__(self):
        return f"{self.borrow_date} {self.user} {self.book}"

class ReturnBook(BaseModel):
    borrowed = models.ForeignKey(BorrowBook, blank=True, on_delete=models.CASCADE)
    return_date = models.DateField()

    def __str__(self):
        return f"{self.borrowed} returned: {self.return_date}"