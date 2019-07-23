# -*- coding: utf-8 -*-
import pymysql
pymysql.install_as_MySQLdb()
 #字段数据匹配
    #ranking.objects.filter(ranking__contains) 含有
    #print(f"xxx")  # f 就是 flask 里面的 format
# """不等于 （exclude）
#     __gt  大于
#     __gte 大于等于
#     __lt 小于
#     __lte 小于等于
#     __in 在一个范围内 [60,120] 即为60 到120
#     __isnull 是否为空
# """
    #  print(str(xxx.query))  可以显示出sql的原生语句
    # exclude(),reverse(),distinct()
    # ranking.objects.all().exclude(条件) 在all的结果中除去exclude 内部设定的值
    # ranking.objects.all().exclude(条件).reverse()
    # """反向排序reverse() 需要在Meta元类里设置ordering """
    # distinct() 去重
    # extra() 实现字段别名      s =ranking.objects.all().extra(select={"A":"name"})   print(s.A) 即为打印name
    # defer() 排除某些字段
    # only() 选择一些字段        ranking.objects.all()。only('xx','xx')
    # union   # 并集 	  a =  ranking.objects.filter(xx=xx)  b =  ranking.objects.filter(xx) print(a.union(b))
    # select_related() 一对一、一对多查询优化     prefetch_related   一对多、多对多查询优化，
    # """ 	news = RecruitmentNews.object.all().select_related()
    # 		for a in news:                                              子表查询父表
    # 			print(f"{a.username}---{a.Slogan.slogan})
    # """
    # 反向查询
    #            --------不返回queryset的API---------------------
    # get()、get_or_create() 、first()、last()、
    #   Slogan.objects.get_or_creeate(solgan='xxx',defaults={xx:xx}
    # first() 获取第一条数据，last()获取最后一条数据
    # create()、bulk_creeaate()、create_or_update()
    # bulk_create(), 批量创建对象。
    #create_or_update()  创建或更新
    # updaate 、updaate_or_create
    # Slogan.objects.folter(更新的目标).update(更新的 内容)
    # exists()、
    # 对象是否存在， Slogan.objects.filter(对象).exxists()
    #
    # __icontains  不区分大小写
    #
    #
    #  -------------F \ Q ----------
    #  F对象 ：操作字段的数据
    # 例如，让所有数据都加11元（一个price的models例子）
    # xxx.objects.update(price=F('price') + 11)
    #
    # Q 对象： and 、or 、 not      & ，|，~  非
    # xxx.objects.filter(Q(title__icontains = 'java') & Q(xxx__gte=5000))







