from django.db import models
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments import highlight

# Create your models here.
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default='python')
    style = models.CharField(max_length=100, choices=STYLE_CHOICES, default='friendly')
    author = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created']


class Member(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    class_type = models.CharField(max_length=15)
    donation = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date']


class Book(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type

    class Meta:
        ordering = ['publish']
