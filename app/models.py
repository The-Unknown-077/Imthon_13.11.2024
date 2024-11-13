from django.db import models


class Aftor(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='authors_image/', null=True, blank=True)

    def __str__(self):
        return self.full_name



class Kategoriya(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name







class BlogDESC(models.Model):
    description = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Kategoriya, on_delete=models.CASCADE, related_name='blogs')
    author = models.ForeignKey(Aftor, on_delete=models.CASCADE, related_name='blogs')
    image = models.ImageField(upload_to='blog_images/')
    title = models.TextField()

    def __str__(self):
        return self.description



