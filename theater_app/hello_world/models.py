from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse  # To generate URLS by reversing URL patterns


class Type(models.Model):
    """Model representing a play type (e.g. Comedy, Love, Drama, History)."""
    name = models.CharField(
        max_length=200,
        help_text="Enter a play type (e.g. Comedy, Love, History etc.)"
        )

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    place_of_birth = models.CharField(max_length=50)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('actor-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0} {1}'.format(self.first_name, self.last_name)


class Play(models.Model):
    """Model representing a play"""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    type = models.ManyToManyField(Type, help_text="Select a type for this play")
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the play")
    actors = models.ManyToManyField(Actor, help_text="Select the actors for this play")

    def display_type(self):
        return ', '.join([type.name for type in self.type.all()[:3]])

    def display_actor(self):
        return ', '.join([actor.first_name for actor in self.actors.all()[:3]])

    display_actor.short_description = 'Actor'
    display_type.short_description = 'Type'

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('play_page', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.title, self.author)


class Review(models.Model):
    """Model representing a review for one or more plays"""
    title = models.CharField(max_length=200)
    play = models.ForeignKey('Play', on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=1000, help_text="Enter a brief review")
    reviewer_name = models.CharField(max_length=20)

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('review-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.title, self.reviewer_name)


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    place_of_birth = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '{0}, {1}'.format(self.last_name, self.first_name)


class PlayInfo(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4,
    #                       help_text="Unique ID for this particular play")
    play = models.ForeignKey('Play', on_delete=models.SET_NULL, null=True)
    duration = models.CharField(max_length=50)
    PLACES = [
        {'MS', 'Main Stage'},
        {'ES', 'Euphorion Stage'},
        {'HS', 'Hamlet Stage'}
    ]
    place = models.CharField(max_length=15, choices=PLACES, default='MS')

    MAIN_CATEGORIES = [
        {'12+', 'Forbidden under 12'},
        {'14+', 'Forbidden under 14'},
        {'18+', 'Forbidden under 18'}
    ]
    age_category = models.CharField(max_length=18, choices=MAIN_CATEGORIES, default='U12')

    def get_absolute_url(self):
        return reverse('play-info-detail', args=[str(self.id)])


class Ticket(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4,
    #                       help_text="Unique ID for this particular ticket")
    play = models.ForeignKey('Play', on_delete=models.SET_NULL, null=True)
    date_of_play = models.DateField(null=True, blank=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    buyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    buyer_name = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('ticket-detail', args=[str(self.id)])



