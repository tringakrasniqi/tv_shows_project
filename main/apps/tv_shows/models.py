from django.db import models

class TVshowManager(models.Manager):
      def basic_validator(self, postData):
            errors = {}
            if len(postData['title']) < 2:
                  errors['title'] = "Title must be more than 2 characters"
            if not postData['network'] or len(postData['network']) < 2:
                  errors['network'] = "Network name must be more at least 3 characters"
            if postData['description']:
                  if len(postData['description']) < 10: 
                        errors['description'] = "Description must be at least 10 characters"
            return errors

class TVshow(models.Model):
      title = models.CharField(max_length=255)
      network = models.CharField(max_length=45)
      release_date = models.DateTimeField()
      description = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      objects = TVshowManager()
