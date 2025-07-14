from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    github_url = models.URLField(blank=True)
    live_demo = models.URLField(blank=True)
    thumbnail = models.ImageField(blank=True)
    tech_stack = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]
    
    class Meta:
        ordering = ["-created_at"]

        def __str__(self):
            return self.title