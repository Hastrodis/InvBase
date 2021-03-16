from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer, tokenizer
from django_elasticsearch_dsl.registries import registry
from SaveBase.models import Techn, Type

n_analyzer = analyzer(
    'n_analyzer',
    tokenizer = tokenizer('trigram', 'ngram', min_gram=4, max_gram=9),
    filter = ["lowercase", "snowball"]
)

@registry.register_document
class TechDocument(Document):
    InvNomer = fields.TextField(
        analyzer = n_analyzer,
        fields ={
            'raw': fields.TextField(analyzer='keyword')
        }
    )
    Naimen = fields.TextField(
        analyzer = n_analyzer,
        fields ={
            'raw': fields.TextField(analyzer='keyword')
        }
    )
    IDType = fields.ObjectField(properties={
        'TypeTech': fields.TextField(),
    })

    class Index:
        # Name of the Elasticsearch index
        name = 'tech'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0,
                    'max_ngram_diff' : 50}

    class Django:
        model = Techn # The model associated with this Document
        related_models = [Type]
        # The fields of the model you want to be indexed in Elasticsearch
        #fields = [
        #    'Naimen',
        #]
