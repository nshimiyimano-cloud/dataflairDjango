from django.db import models

# Create your models here.


from django.db import models
# Create your models here. #DataFlair 
class Post(models.Model): 
    post_heading = models.CharField(max_length = 200)
    post_text = models.TextField()
def deletepost():
    print('post deleted')       
class Like(models.Model):
    post = models.ForeignKey(Post,on_delete=deletepost)
        #post = models.ForeignKey(Post, on_delete = "CASCADE")

