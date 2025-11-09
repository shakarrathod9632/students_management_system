from django.db import models

# Course Model
class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']  # default sort A→Z

    def __str__(self):
        return self.name


# Student Model
class Student(models.Model):

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        default='Male'
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="students"
    )

    profile_pic = models.ImageField(
        upload_to='student_photos/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']  # default sort A→Z

    def __str__(self):
        return self.name
