'''
The purpose of indexing objects is to optimize speed and 
performance in finding relevant documents for a given search query.
With search index haystack determines what data should 
be placed in the index.
'''

from haystack import indexes
from book.models import Book
class BookIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True,
     template_name="search/book_text.txt")
    title = indexes.CharField(model_attr='title')
    authors = indexes.CharField()
    def get_model(self):
        return Book
    def prepare_authors(self, obj):
        return [ author.name for a in obj.authors.all()]
    def index_queryset(self, using=None):
        return self.get_model().objects.all()