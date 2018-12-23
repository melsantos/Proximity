from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    age = models.PositiveIntegerField()
    hobbies = models.TextField(default='')
    photo = models.ImageField(upload_to="profile_photos/", null=True, default="profile_photos/default.jpg")
    location = models.CharField(max_length=150, blank=True, default='') #of the form: Riverside, CA
    latitude = models.FloatField(max_length=150, default=0.0)
    longitude = models.FloatField(max_length=150, default=0.0)

    def __str__(self):
        return '%s\'s Profile' % self.user.get_username()

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True) #apparently cascade delete happens automatically?
    postContent = models.TextField()
    datePosted = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to="post_photos/",null=True)

    def __str__(self):
        return '%s\'s post - %s' % (self.profile.user.get_full_name(), self.datePosted.strftime("%x %X"))

    def get_comments(self):
        return Comment.objects.filter(post=self.id)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    commentContent = models.TextField()
    datePosted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s\'s comment on %s\'s Post' % (self.profile.user.get_full_name(), self.post.profile.user.get_full_name() )

class Follow(models.Model):
    userFollowing = models.ForeignKey(User, on_delete=models.PROTECT, related_name="userFollowing")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="userFollowed")
    isRequest = models.BooleanField(default=False)

    def __str__(self):
        return '%s follows %s' % (self.user.get_username(), self.userFollowing.get_username())

class Block(models.Model):
    userBlocking = models.ForeignKey(User, on_delete=models.PROTECT, related_name="userBlocking")
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="userBlocked")

    def __str__(self):
        return '%s blocked %s' % (self.user.get_username(), self.userBlocking.get_username())   

class Thread(models.Model):
    userOne = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userOne")
    userTwo = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userTwo")

    def __str__(self):
        return '%s - %s' % (self.userOne.get_username(), self.userTwo.get_username())

class Message(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    messageContent = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    datePosted = models.DateTimeField(auto_now_add=True)
    isRequest = models.BooleanField(default=False)

    def __str__(self):
        return '%s message %s' % (self.author.get_username(), self.datePosted.strftime("%x %X"))

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    name = models.CharField(max_length=100, blank=False)
    date = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=150, blank=False, default='') #like Riverside, CA
    latitude = models.FloatField(max_length=150, default=0.0)
    longitude = models.FloatField(max_length=150, default=0.0)
    description = models.CharField(max_length=500, blank=False)
    category = models.CharField(max_length=100)
    poster = models.ForeignKey(Profile, blank=True, on_delete=models.PROTECT, related_name='poster', default=1)
    rsvp_list = models.ManyToManyField(Profile, blank=True)

    def __str__(self):
        return '%s - %s' % (self.name, self.location)