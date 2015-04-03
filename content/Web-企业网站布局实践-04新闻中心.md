Title: 企业网站布局实践-05 新闻中心制作
Date: 2015-04-03 14:00
Category: Web
Tags: CSS, HTML, LESS
Author: 刘理想

##1、结构分析

![新闻中心](images/qy-web-07.png)

从上到下可以分为新闻标题、图片新闻和图片新闻。

##2、创建结构

新闻中心分为标题、图片新闻和新闻列表3部分。
其中，新闻列表还是使用无序列表。
```
<div class="news">
 <div class="title">
     <h2>新闻中心</h2><a href="news.html">More&gt;&gt;</a>
 </div><!-- title结束 -->
 <div class="pic_news">
     <img src="images/news.jpg" alt=""><h2>520 慕女神喊你来表白！</h2>
     <p>
         活动时间：5月20日—5月25日<br>获奖公布时间：5月26日<br>Learn More>>
     </p>
 </div><!-- pic_news结束 -->
 <div class="news_list">
     <ul>
         <li><a href="news.html">【慕客访谈 用户篇】“有为屌丝”在路上</a><span>2014-06-01</span></li>
         <li><a href="news.html">【有奖活动】给父亲的三行书信</a><span>2014-06-01</span></li>
         <li><a href="news.html">《程序猿，请晒出你的童年》活动获奖公告</a><span>2014-05-30</span></li>
         <li><a href="news.html">【慕课访谈】破茧成蝶——美女程序员的蜕变史</a><span>2014-05-28</span></li>
     </ul>
 </div><!-- news_list结束 -->
</div><!-- news结束 -->
```

##3、创建CSS

新闻标题是title节

```
.news{
    width:340px;
    border: 1px solid #E8E8E8;
    background-color: #FFF;

    .title{
        height: 35px;
        border-bottom: 2px solid #E8E8E8;

        &_left{
            width: 70%;
            line-height: 35px; //居中
            font-family: "微软雅黑";
            font-size: 14px;
            font-weight: bold;
            color: #786F66;
            float: left; 
            padding-left: 20px;
        }

        &_right{
            width:20%;
            line-height: 35px;
            float:right;
            text-align: right;

            a{
                text-decoration: none;
                color: #999999;
                font-family: "宋体";
                font-size: 10px;
                font-weight: normal;
                padding-right: 10px;
            }
        }
    }
}
```