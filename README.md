# BM25
Reimplement BM25 with python3

### BM25公式：

<img src="http://chart.googleapis.com/chart?cht=tx&chl= Score(Q, d)=\sum_{i}^{n} W_{i} R\left(q_{i}, d\right)" style="border:none;">

其中，Q为用户问题，d为“文档”库中的一个文档，n为用户问题中词的个数,q_i为用户问题中第i个词，W_i为该词的权重，R(q_i,d)为该词与标准问题的相关性分数。W_i相当于TF-IDF算法中的IDF，R(q_i,d)相当于是TF-IDF算法中的TF；只不过BM25对这两个指标进行了优化，具体如下：

<img src="http://chart.googleapis.com/chart?cht=tx&chl= W_{i}=\log \left(\frac{N - df_{i} \+ 0.5}{d f_{i} \+ 0.5}\right)" style="border:none;">

其中，N表示为“文档”库中的总文档数， df_i 表示包含词汇 q_i 的标准问题的个数。

<img src="http://chart.googleapis.com/chart?cht=tx&chl= R\left(q_{i}, d\right)=\frac{f_{i}\left(k_{1}\+1\right)}{f_{i}\+K} * \frac{q f_{i}\left(k_{2}+1\right)}{q f_{i}+k_{2}}" style="border:none;">

<img src="http://chart.googleapis.com/chart?cht=tx&chl= K=k_{1} *\left(1-b+b * \frac{d l}{a v g_{-} d l}\right)" style="border:none;">

其中，k_1,k_2和b是调协因子，一般分别设为2，1，0.75； f_i 表示词汇 q_i在文档中出现的次数； qf_i 表示词汇在用户问题中出现的次数；dl 为文档的长度； avg_dl 为“文档”库中所有文档的平均长度。

### 运行
```
python main.py
```

outputs:
Query_id | Document_id |  rank_id | BM25_value 
-|-|-|-
0	|3127	|0	|17.168630281724607
0	|2246	|1	|13.074544882177358
0	|1930	|2	|10.894128792490445
1	|2748	|0	|13.796923352177505
1	|2897	|1	|13.25847752540956
1	|2491	|2	|12.964882702322535

