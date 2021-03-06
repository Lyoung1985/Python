# IPython log file

import matplotlib as plt
import pandas as pd
from pandas import Series, DataFrame
get_ipython().run_line_magic('pinfo', 'Series.plot')
DataFrame.plot
get_ipython().run_line_magic('pinfo', 'DataFrame.plot')
s = Series()
get_ipython().run_line_magic('pinfo', 's.plot')
get_ipython().run_line_magic('ll', '')
s = Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))
s.plot()
plt.save('Figure_14.png')
df
df = DataFrame(np.random.randn(10,4).cumsum(0),
               columns=['A','B','C','D'],
               index=np.arange(0,100,10))
               
df.plot
df = DataFrame(np.random.randn(10,4).cumsum(0),
               columns=['A','B','C','D'],
               index=np.arange(0,100,10))
               
df.plot()
plt.axes
plt.axes()
import matplotlib.pyplot as plt
fig, axes = plt.subplots(2,1)
data = Series(np.random.randn(16),index=list('abcdefghijklmnop'))
data.plot(kind='bar', ax=axes[0],color='k', alpha=0.7)
data = Series(np.random.rand(16),index=list('abcdefghijklmnop'))
data.plot(kind='bar', ax=axes[0],color='k', alpha=0.7)
fig, axes = plt.subplots(2,1)
data = Series(np.random.rand(16),index=list('abcdefghijklmnop'))
data.plot(kind='bar', ax=axes[0],color='k', alpha=0.7)
data.plot(kind='barh', ax=axes[1],color='k', alpha=0.7)
fig.savefig('Figure_16.png')
df = DataFrame(np.random.rand(6,4),)
df = DataFrame(np.random.rand(6,4),
               index=['r1','r2','r4','r5','r6'],
               columns=pd.Index(['A','B','C','D'],name='Genus'))
               
df = DataFrame(np.random.rand(6,4),
               index=['r1','r2','r3','r4','r5','r6'],
               columns=pd.Index(['A','B','C','D'],name='Genus'))
               
df = DataFrame(np.random.rand(6,4),
               index=['r1','r2','r3','r4','r5','r6'],
               columns=pd.Index(['A','B','C','D'],name='Genus'))
               
df
fig, axes = plt.subplots(2,1)
df.plot(kind='bar',ax=axes[0])
df.plot(kind='barh',ax=axes[1],stacked=True, alpha=0.5)
fig.savefig('Figure_17.png')
tips = pd.read_csv(' /Users/dengxiaojun/Documents/pydata-book-2nd-edition/examples/tips.csv‘)
tips = pd.read_csv('/Users/dengxiaojun/Documents/pydata-book-2nd-edition/examples/tips.csv‘)
tips = pd.read_csv('/Users/dengxiaojun/Documents/pydata-book-2nd-edition/examples/tips.csv')
party_counts = pd.crosstab(tips.day,tips.size)
party_counts
tips
party_counts = pd.crosstab(tips.day,tips.size)
party_counts
party_counts = pd.crosstab(index=tips.day,colnames=tips.size)
party_counts = pd.crosstab(index=tips.day,columns=tips.size)
party_counts
tips
party_counts = party_counts.loc[:,2:5]
party_counts
party_counts = pd.crosstab(tips.size,tips.day)
party_counts
get_ipython().run_line_magic('pinfo', 'pd.crosstab')
tips.size
tips['size']
tips = pd.read_csv('/Users/dengxiaojun/Documents/pydata-book-2nd-edition/examples/tips.csv‘)
tips = pd.read_csv('/Users/dengxiaojun/Documents/pydata-book-2nd-edition/examples/tips.csv')
party_counts = pd.crosstab(tips.day,tips['size'])
party_counts
party_counts = party_counts.loc[:,2:5]
party_pcts = party_counts.div(party_counts.sum(1).astype(float), axis=0)
party_pcts
party_pcts.plot(kind='bar',stacked=True)
tips
tips = pd.read_csv('/Users/dengxiaojun/Documents/pydata-book-2nd-edition/examples/tips.csv')
tips
tips = pd.read_csv('/Users/dengxiaojun/Documents/pydata-book-2nd-edition/examples/tips.csv')
tips['tip_pct'] = tips['tips']/tips['total_bill']
tips = pd.read_csv('/Users/dengxiaojun/Documents/pydata-book-2nd-edition/examples/tips.csv')
tips['tip_pct'] = tips['tip']/tips['total_bill']
tips['tip_pct'].hist(bins=509)
tips = pd.read_csv('/Users/dengxiaojun/Documents/pydata-book-2nd-edition/examples/tips.csv')
tips['tip_pct'] = tips['tip']/tips['total_bill']
tips['tip_pct'].hist(bins=50)
tips['tip_pct'].plot('kind=kde')
tips['tip_pct'].plot(kind='kde')
tips['tip_pct'].plot(kind='kde')
tips['tip_pct'].plot(kind='kde')
get_ipython().system('pip3 install scipy')
get_ipython().system('pip3 install scipy')
get_ipython().system('pip3 install scipy -i http://mirrors.aliyun.com/pypi/simple/ ')
get_ipython().system('pip3 install scipy -i http://pypi.douban.com/simple/ ')
get_ipython().system('pip3 install --ipgrade pip')
get_ipython().system('pip3 install --upgrade pip')
get_ipython().system('pip3 install scipy -i http://pypi.douban.com/simple/ ')
get_ipython().system('pip3 install scipy -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com')
tips['tip_pct'].plot(kind='kde')
tips['tip_pct'].plot(kind='kde')
comp1  = np.random.normal(0,1,size=200)
comp2 = np.random.normal(10,2,size=200)
values = Series(np.concatenate([comp1,comp2]))
values.hist(bins=100, alpha=0.3, color='k', normed=True)
values.hist(bins=100, alpha=0.3, color='k', density=True)
values.plot(kind='kde', style='k--')
comp1  = np.random.normal(0,1,size=200)
comp2 = np.random.normal(10,2,size=200)
values = Series(np.concatenate([comp1,comp2]))
values.hist(bins=100, alpha=0.3, color='k', density=True)
values.plot(kind='kde', style='k--')
macro = pd.read_csv('/Users/dengxiaojun/Documents/pydata-book-2nd-edition/examples/macrodata.csv')
data = macro[['cpi','m1','tbilrate','unemp']]
trans_data = np.log(data).diff().dropna()
trans_data[-5:]
plt.scatter(trans_data['m1'],trans_data['unemp'])
plt.title('Changes in log %s vs .log %s' % ('m1', 'unemp'))
macro = pd.read_csv('/Users/dengxiaojun/Documents/pydata-book-2nd-edition/examples/macrodata.csv')
data = macro[['cpi','m1','tbilrate','unemp']]
trans_data = np.log(data).diff().dropna()
trans_data[-5:]
plt.scatter(trans_data['m1'],trans_data['unemp'])
macro = pd.read_csv('/Users/dengxiaojun/Documents/pydata-book-2nd-edition/examples/macrodata.csv')
data = macro[['cpi','m1','tbilrate','unemp']]
trans_data = np.log(data).diff().dropna()
trans_data[-5:]
plt.scatter(trans_data['m1'],trans_data['unemp'])
plt.title('Changes in log %s vs .log %s' % ('m1', 'unemp'))
pd.scatter_matrix(trans_data,diagonal='kde',color='k',alpha=0.4)
pd.plotting.scatter_matrix(trans_data,diagonal='kde',color='k',alpha=0.4)
get_ipython().run_line_magic('pwd', '')
get_ipython().run_line_magic('cd', '/Users/dengxiaojun/Documents/GitHub/')
get_ipython().run_line_magic('cd', 'Python/')
get_ipython().run_line_magic('cd', 'ipython/')
get_ipython().run_line_magic('logstart', '')
#从csv文件中加载数据到DataFrame中
tips = pd.read_csv('/Users/dengxiaojun/Documents/pydata-book-2nd-edition/datasets/haiti/haiti.csv')
data = tips
data
# 每一行表示从某人手机上发送的紧急或其他问题的报告，每条报告都有一个时间戳和位置(经度和纬度)
data['INCIDENT DATE','LATITUDE','LONGITUDE'][:10]
data[['INCIDENT DATE','LATITUDE','LONGITUDE']][:10]
# GATEGORY字段含有一组一逗号分隔的代码，这些代码表示消息的类型
# CATEGORY字段含有一组一逗号分隔的代码，这些代码表示消息的类型
data['CATEGORY'][:6]
# 经观察上面的数据摘要有些分类信息缺失，因此需要丢弃这些数据点，然后调用describe发现一些异常的地理位置
data.describe()
#清除错误位置信息并一处缺失分类信息
data = data[(data.LATITUDE > 18)&(data.LATITUDE<20)&(data.LONGITUDE>-75)&(data.LONGITUDE<-70)&data.CATEGORY.notnull()]
#根据分类对数据做一些分析和图形化工作，但各个分类字段可能含有多个分类。
# 此外分类信息不仅有一个编码，还有一个英文名称。因此需要对数据做一些规整化处理
def to_cat_list(catstr):
    # 用户获取分类的列表
    stripped = （x.strip() for x in catstr.split(',')）
def to_cat_list(catstr):
    # 用户获取分类的列表
    stripped = (x.strip() for x in catstr.split(',')）
def to_cat_list(catstr):
    # 用户获取分类的列表
    stripped = (x.strip() for x in catstr.split(','))
def get_all_categories(cat_series):
    # 获取所有分类信息
    cat_sets = (set(to_cat_list(x)) for x in cat_series)
    return sorted(set.union(*cat_sets))
def to_cat_list(catstr):
    # 用户获取分类的列表
    stripped = (x.strip() for x in catstr.split(','))
    return [x for x in stripped if x]
def get_all_categories(cat_series):
    # 获取所有分类信息
    cat_sets = (set(to_cat_list(x)) for x in cat_series)
    return sorted(set.union(*cat_sets))
def get_english(cat):
    # 获取英文名称
    code, names = cat.split('.')
    if '|' in names:
        names = names.split('|')[1]
    return code, names.strip()
# 将编码跟名称映射到字典
all_cats = get_all_categories(data.CATEGORY)
# 生成器表达式
english_mapping = dict(get_english(x) for x in all_cats)
english_mapping('2a')
english_mapping['2a']
# 根据分类选取记录的方式很多，其中之一是添加指标列(或哑变量)，每个分类一列
# 现抽取出唯一的分类编码，并构造一个全零DataFrame(列为分类编码，索引跟data的索引一样)
def get_code(seq):
    return[x.split('.')[0] for x in seq if x]
all_codes = get_code(all_cats)
code_index = pd.Index(np.unique(all_codes))
dummy_frame = DataFrame(np.zeros((len(data),len(code_index))),
                        index = data.index,
                        columns = code_index)
                        
dummy_frame.loc[:,:6]
dummy_frame.loc[:, :6]
dummy_frame.ix[:,:6]
for row,cat in zip(data.index, data.CATEGORY):
    codes = get_code(to_cat_list(cat))
    dummy_frame.ix[row,codes]=1
    
data = data.join(dummy_frame.add_prefix('category_'))
data.ix[:,10:15]
get_ipython().system('pip3 install basemap')
get_ipython().system('pip3 install mpl_toolkits')
from mpl_toolkits.basemap import Basemap
get_ipython().system('pip3 install mpl_toolkits')
get_ipython().system('pip3 install basemap')
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null
get_ipython().system('ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null')
get_ipython().system('ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null')
brew install geos
get_ipython().system('brew install geos')
export GEOS_DIR=/usr/local/Cellar/geos/3.6.2
get_ipython().system('export GEOS_DIR=/usr/local/Cellar/geos/3.6.2')
get_ipython().system('python3 setup.py install')
get_ipython().system('python setup.py install')
get_ipython().system('python3.6 setup.py install')
get_ipython().system('python3')
get_ipython().system('python3.6 setup.py install')
get_ipython().system('pip3 install pyproj')
from mpl_toolkits.basemap import Basemap
get_ipython().system('brew install geos')
get_ipython().system('python3 setup.py install')
get_ipython().system('python3 setup.py install')
from mpl_toolkits.basemap import Basemap
reload(sys)
import sys
get_ipython().run_line_magic('reload_ext', '')
get_ipython().run_line_magic('reload_ext', 'sys')
from mpl_toolkits.basemap import Basemap
