# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import sys
from whoosh.index import open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser, MultifieldParser
from jieba.analyse import ChineseAnalyzer
from whoosh import scoring
from whoosh.query import *

sys.path.append("../")

analyzer = ChineseAnalyzer()
ix = open_dir("html_index")  # for read only

inputstring = "中国and(国际or物流)and开幕"
# inputstring = "12 string english"
# inputstring = "中国国际物流节开幕"
keywords = []
for t in analyzer(inputstring):
    keywords.append(t.text)
# keywords = inputstring.split(" ")
# keywordstr = " ".join(keywords)

# searcher = ix.searcher(weighting=scoring.TF_IDF())
# parser = QueryParser("body", schema=ix.schema)

# for keyword in keywords:
#     print("result of %s" % keyword)
#     print(keyword)
#     q = parser.parse(keyword)
#     results = searcher.search(q, terms=True)
#     for hit in results:
#         print(hit['title'])
#     print("="*10)

# qp = QueryParser("title", schema=ix.schema)
qp = MultifieldParser(["title", "body"], schema=ix.schema)

with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
    # q = qp.parse(keywordstr)
    # terms_list = [terms for terms in q.terms()]
    # print(terms_list)
    # querystring = Or(terms_list)
    # querystring = And([Term("title", "中国"), Term("title", "国际"), Term("title", "物流"), Term("title", "国际物流节"), Term("title", "开幕")])
    # print(q)
    # querystring = Or([Term("body", word) for word in keywords])
    querystring = qp.parse(inputstring)
    results = searcher.search(querystring, terms=True, limit=100, collapse_limit=1)
    for hit in results:
        print(hit['title'].encode('gbk'))
