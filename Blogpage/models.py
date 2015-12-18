from __future__ import unicode_literals

from django.db import models
from tinymce import models as tinymce_models

class posts(models.Model):

	author = models.CharField(max_length = 40)
	title = models.CharField(max_length = 200)
	bodytext = tinymce_models.HTMLField()
	timestamp = models.DateTimeField()
	
	def __unicode__(self): #Python 3 is __str__
		return self.title
