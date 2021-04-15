import json
import pytest
import rdflib
import requests

def test_test():
    assert 1 == 1

def test_maps_to_property():
    # open a graph
    graph = rdflib.Graph()
    # load some data
    graph.parse('mato.ttl', format="ttl")
    assert graph, 'Error: mato.ttl graph failed to parse'

    qres = graph.query("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX dc: <http://purl.org/dc/elements/1.1/>

        SELECT DISTINCT *    
        WHERE {
                ?onto dc:title ?title.
               }
        """)
    assert len(qres) > 0  , 'Error: No triples returned.'
