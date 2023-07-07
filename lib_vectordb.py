import os


## for vector store
from elastic_vector_search import ElasticVectorSearch

def setup_vectordb(hf,index_name):
    # Elasticsearch URL setup
    print(">> Prep. Elasticsearch config setup")
    cloud_id = os.getenv('ES_CLOUD_ID', 'ERROR') 
    username = os.getenv('ES_USERNAME', 'ERROR') 
    password = os.getenv('ES_PASSWORD', 'ERROR')

    return ElasticVectorSearch(embedding=hf, cloud_id=cloud_id, username=username, password=password, index_name=index_name)
