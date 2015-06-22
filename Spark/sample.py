#!/usr/bin/env python
# -*- coding: utf-8 -*-

#ライブラリのインポート
import pandas as pd
import time

#計測開始
start = time.time()

#データの読み込み
df = pd.read_csv("/Path/To/Data/data_q1587.tsv", delimiter = '\t')

#c1, c2についてピボットテーブルを作成
mt = df.groupby(['c2', 'c1']).size().unstack()

#各ノードのサイズを取得
nodeSizeDic = {x:mt.ix[x].count() for x in mt.index}

#ノードの組み合わせごとに共通サイズを取得
commonSizeDic={}
for node1,v in mt.iterrows():
  edges=v.dropna()
  for edge in edges.index:
    nodes2=mt[edge].dropna()
    for node2 in nodes2.index:
      if node1 != node2:
        commonSizeDic[(node1,node2)] = commonSizeDic.get((node1,node2), 0) + 1

#各情報を集約
pieces=[]
for k,v in commonSizeDic.iteritems():
  pieces.append([k[0],k[1],nodeSizeDic[k[0]],nodeSizeDic[k[1]],v])
wm=pd.DataFrame(pieces,columns=['node1','node2','size1','size2','common'])

#結果を出力
wm.to_csv('output.tsv', sep='\t', index=False)

#計測終了
spendTime = time.time() - start
print spendTime
