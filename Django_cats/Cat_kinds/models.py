from django.db import models
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect


class CatKinds(models.Model):
    british = models.CharField(max_length=40, verbose_name='kinds')
    likes = models.IntegerField(blank=False)

    def __str__(self):
        return self.british

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        ordering = ['likes', 'british']
        verbose_name = 'Cat kinds'
        verbose_name_plural = 'Cat kinds'



