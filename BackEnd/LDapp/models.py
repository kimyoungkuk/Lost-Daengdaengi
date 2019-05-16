from django.db import models

# Create your models here.

# NN(Not Null) is default setting
# If you use Null attribute, you insert this code "null = True, default = True"

# id        INT(11)
# title     VACHAR(1000)
# lat       DOUBLE
# lng       DOUBLE
#class Post(models.Model):
#    title = models.CharField(max_length = 1000, default = "")
#    lat = models.FloatField(null=True, blank=True, default = True)
#    lng = models.FloatField(null=True, default = True)
#    adfil = models.FloatField(blank = True, default = True)

# id            INT(11)
# title         VACHAR(30)
# created_date  DATETIME
# view_cnt      INT(11)
# contents      LONGTEXT()
# write_id      INT(11)         1 to n (1 : n = post : test)
#class Test(models.Model):
#    write = models.ForeignKey(Post, on_delete=models.CASCADE)
#    title = models.CharField(max_length = 30)
#    created_date = models.DateTimeField()
#    view_cnt = models.IntegerField()
#    contents = models.TextField()

class Users(models.Model):
    pw          =   models.CharField(max_length = 20)
    user_id     =   models.CharField(max_length = 20)
    phone_num   =   models.CharField(max_length = 20)
    e_mail      =   models.CharField(max_length = 20)

class Post(models.Model):
    post_type   =   models.IntegerField(null = True)
    post_time   =   models.DateTimeField(auto_now_add = True, null = True)
    post_period =   models.DateTimeField(null = True)
    user        =   models.ForeignKey(Users, on_delete = models.CASCADE, null = True)

class Owner_post(models.Model):
    # one-to-one
    postOwner         =   models.OneToOneField(Post, on_delete = models.CASCADE, primary_key = True, default = True)
    picture         =   models.CharField(max_length = 100)
    phone_num       =   models.CharField(max_length = 20)
    lost_location   =   models.CharField(max_length = 20)
    dog_name        =   models.CharField(max_length = 20)
    dog_sex         =   models.IntegerField()
    dog_type        =   models.CharField(max_length = 20)
    lost_time       =   models.DateTimeField()
    dog_age         =   models.IntegerField()
    dog_feature     =   models.TextField()
    remark          =   models.TextField()

class Dog_shelter(models.Model):
    shelter_name    =   models.CharField(max_length = 20)
    shelter_loc     =   models.CharField(max_length = 20)
    phone_num       =   models.CharField(max_length = 20)
    description     =   models.TextField()

class Finder_post(models.Model):
    # one-to-one
    postFinder      =   models.OneToOneField(Post, on_delete = models.CASCADE, primary_key = True)
    picture         =   models.CharField(max_length = 100)
    phone_num       =   models.CharField(max_length = 20)
    find_time       =   models.DateTimeField()
    find_loc        =   models.CharField(max_length = 20)
    dog_feature     =   models.TextField()
    dog_type        =   models.CharField(max_length = 20)
    # one-to-one
    shelter         =   models.OneToOneField(
            Dog_shelter,
            on_delete = models.CASCADE
            )

class Report(models.Model):
    reason          =   models.CharField(max_length = 10)
    detail          =   models.TextField()
    report_date     =   models.DateTimeField(auto_now_add = True)
    post            =   models.ForeignKey(Post, on_delete = models.CASCADE, null = True)
    userReport      =   models.ForeignKey(Users, on_delete = models.CASCADE, null = True)

class Matching(models.Model):
    userMatching    =   models.ForeignKey(Users, on_delete = models.CASCADE, null = True)
    postMatching    =   models.ForeignKey(Post, on_delete = models.CASCADE, null = True)
