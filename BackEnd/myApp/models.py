from django.db import models

# Create your models here.
class User(models.Model):
    is_admin    =   models.IntegerField(default = 0)
    key         =   models.CharField(max_length = 1000, default = "")
    nickname    =   models.CharField(max_length = 1000, default = "")

class Owner_post(models.Model):
    # one-to-one
#    postOwner         =   models.OneToOneField(Post, on_delete = models.CASCADE, primary_key = True, default = True)
    title           =   models.CharField(max_length = 1000)
    phone_num       =   models.CharField(max_length = 1000)
    lat             =   models.FloatField(default = True)
    lng             =   models.FloatField(default = True)
    posted_time     =   models.DateTimeField(auto_now_add = True)
    posted_due      =   models.DateField()

    image           =   models.TextField(default = "", blank=True, null=True)
    imageurl        =   models.CharField(max_length = 2000, default = "http://202.30.31.91:8000/media/default_image.jpg", blank=True, null=True)

    dog_name        =   models.CharField(max_length = 200)
    dog_sex         =   models.IntegerField()
    dog_type        =   models.CharField(max_length = 200)
    lost_time       =   models.DateTimeField()
    dog_age         =   models.IntegerField()
    dog_feature     =   models.TextField()
    remark          =   models.TextField()

    user_nickname   =   models.CharField(max_length = 1000, blank=True, default = "")
    user_key        =   models.CharField(max_length = 1000, blank=True, default = "")
    report_count    =   models.IntegerField(blank=True, default = 0)
    view_count      =   models.IntegerField(blank=True, default = 0)

    def __str__(self):
        return self.title

class Dog_shelter(models.Model):
    shelter_name    =   models.CharField(max_length = 20)
    lat             =   models.FloatField(default = True)
    lng             =   models.FloatField(default = True)
    phone_num       =   models.CharField(max_length = 20)
    description     =   models.TextField()
    def __str__(self):
        return self.shelter_name

class Finder_post(models.Model):
    # one-to-one
#    postFinder      =   models.OneToOneField(Post, on_delete = models.CASCADE, primary_key = True)
    title           =   models.CharField(max_length = 1000)
    phone_num       =   models.CharField(max_length = 1000)
    lat             =   models.FloatField()
    lng             =   models.FloatField()
    posted_time     =   models.DateTimeField(auto_now_add = True)
    posted_due      =   models.DateField()

    image           =   models.TextField(default = "", blank=True, null=True)
    imageurl        =   models.CharField(max_length = 2000, default = "http://202.30.31.91:8000/media/default_image.jpg", blank=True, null=True)

    find_time       =   models.DateTimeField()
    dog_feature     =   models.TextField()
    dog_type        =   models.CharField(max_length = 200)
    shelter_name    =   models.CharField(max_length = 200, default = True)
    # one-to-one
    shelter         =   models.ForeignKey(
            Dog_shelter,
            on_delete = models.CASCADE,
            blank = True,
            null = True
            )
    def __str__(self):
        return self.title
    
    user_nickname   =   models.CharField(max_length = 1000, blank=True, default = "")
    user_key        =   models.CharField(max_length = 1000, blank=True, default = "")
    report_count    =   models.IntegerField(blank=True, default = 0)
    view_count      =   models.IntegerField(blank=True, default = 0)

class Comment(models.Model):
    user_nickname   =   models.CharField(max_length=20,default="")
    user_key        =   models.CharField(max_length = 1000, default = "")
    contents        =   models.TextField('contents')
    commented_time     =   models.DateTimeField('posted_date',auto_now_add=True)
    commented_post_type  =   models.CharField(max_length=20,default="")
    commented_post  =   models.IntegerField(default=0)
    

class report(models.Model):
    user_nickname   =   models.CharField(max_length=20,default="")
    contents        =   models.TextField()
    reported_time   =   models.DateTimeField('posted_date',auto_now_add=True)
    reported_post_type   =   models.CharField(max_length=20,default="")
    reported_post  =   models.IntegerField(default=0)





#class Report(models.Model):
#    reason          =   models.CharField(max_length = 10)
#    detail          =   models.TextField()
#    report_date     =   models.DateTimeField(auto_now_add = True)
#    post            =   models.ForeignKey(Post, on_delete = models.CASCADE, null = True)
#    userReport      =   models.ForeignKey(User, on_delete = models.CASCADE, null = True)

#class Matching(models.Model):
#    userMatching    =   models.ForeignKey(User, on_delete = models.CASCADE, null = True)
#    postMatching    =   models.ForeignKey(Post, on_delete = models.CASCADE, null = True)
