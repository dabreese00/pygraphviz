from nose.tools import *
import pygraphviz as pgv
from os import linesep


def stringify(agraph):
    result = agraph.string().split()
    if '""' in result:
        result.remove('""')
    return " ".join(result)


def test_subgraph():
    G = pgv.AGraph()
    G.add_edge(1, 2)
    s = G.add_subgraph((1, 2), label='foo')
    ans = """strict graph { { graph [label=foo]; 1 -- 2; } }"""
    assert_equal(stringify(G), ans)


def test_subgraph_cluster():
    G = pgv.AGraph(label='foo')
    s = G.subgraph('cluster_a', label='<Hello<BR/>World>')
    s.add_node('sa')
    G.add_node('a')
    ans = """strict graph { graph [label=foo];
             { graph [label=<Hello<BR/>World>]; sa; }
             a; }"""
    assert_equal(stringify(G), " ".join(ans.split()))


def test_subgraph_cluster_attribute():
    G = pgv.AGraph()
    s = G.subgraph(name='cluster_a')
    s.node_attr['foo'] = 'bar'
    G.add_node('a')
    G.node_attr['foo'] = 'baz'
    ans = """strict graph { node [foo=baz];
             subgraph cluster_a {
               graph [foo=bar];
             }
             a; }"""
    assert_equal(stringify(G), " ".join(ans.split()))
