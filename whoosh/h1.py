import os
from whoosh.index import create_in
from whoosh.fields import *
from jieba.analyse import ChineseAnalyzer
from whoosh.analysis import StandardAnalyzer as ChineseAnalyzer
import json

# 创建schema, stored为True表示能够被检索
schema = Schema(title=TEXT(stored=True),
                dynasty=ID(stored=True),
                poet=ID(stored=True),
                content=TEXT(stored=True)
                )
texts = [
    ['hi im super man 我啊 asdf2','asdfasdfasdfasdf', '123123123123', '1231231231231234'],
    ['123123123asd 我啊 asdf是','asdfasdfasdfasdf', '12312d3123123', '1231231231231234'],
    ['123123123asd 我啊 asdf3','asdfasdfasdfasdf', '123123123123', '12312312312312341'],

         ]

# 存储schema信息至indexdir目录
indexdir = 'indexdir/'
if not os.path.exists(indexdir):
    os.mkdir(indexdir)
ix = create_in(indexdir, schema)

# 按照schema定义信息，增加需要建立索引的文档

# writer = ix.writer()
with ix.writer() as writer:
    for i in range(1, len(texts)):
        title, dynasty, poet, content = texts[i]
        d = dict(title=title, dynasty=dynasty, poet=poet, content=content)
        writer.add_document(**d)
# writer.commit()
searcher = ix.searcher()

# 检索content中出现'明月'的文档
from whoosh.qparser import OrGroup, AndGroup, MultifieldParser
group = OrGroup if 1 else AndGroup
parser = MultifieldParser(['title'], schema, group=group)
results = searcher.search(parser.parse("我啊 是"), )

print('一共发现%d份文档。' % len(results))

for i in range(min(10, len(results))):
    print(results[i])
    # print(json.dumps(results[i].fields(), ensure_ascii=False))