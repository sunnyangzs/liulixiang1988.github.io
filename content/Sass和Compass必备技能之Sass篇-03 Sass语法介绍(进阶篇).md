Title: Sass和Compass必备技能之Sass篇-03 Sass语法介绍(进阶篇)
Date: 2015-04-17 22:46
Category: Web
Tags: CSS, SASS
Author: 刘理想

##1. 变量操作

变量操作有两种方式，第一种是直接操作，第二种是通过函数。

通过函数：
- 跟代码块无关的函数，多是自己内置函数，称functions
- 可重用的代码块，称mixin: @include和 @extand的方式来应用，

运算符： `>= <= > < == != ()`

CSS3增加了HSL的颜色，SASS会自动转换HSL为RGB,完美解决兼容。

sass支持@function来声明函数。

##2. mixin和include

```
//声明
@mixin col-6{
    width: 50%;
    float: left;
}

//调用
.webdemo-sec {
    @include col-6();

    &:hover{
        background-color: #F5F5F5;
    }
}
```

CSS中class最好使用语义化的命名。IE6不支持多个class。

带参数以及默认参数：
```
@mixin col($width:50%){
    width: $width;
    float: left;
}

.webdemo-sec {
    @include col(30%);

    &:hover{
        background-color: #F5F5F5;
    }
}
```

#3. @extend
```
.error{
    color: #f00;
}

.serious-error{
    @extend .error;
    border: 1px solid #f00;
}
```

extend两个知识点：
1. extend不可以继承选择器序列
2. %仅用来被继承，如`%error`，则不会输出到css中。


