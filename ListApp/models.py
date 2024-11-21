from django.db import models
class Todo_entry (models. Model):
    entry=models. CharField(max_length=255)
    created_at = models. DateTimeField (auto_now_add=True)
    updated_at = models. DateTimeField (auto_now=True)
def _str_(self):
    return self.entry