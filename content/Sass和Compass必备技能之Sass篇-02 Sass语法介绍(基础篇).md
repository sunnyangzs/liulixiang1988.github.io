Title: Sass和Compass必备技能之Sass篇-02 Sass语法介绍(基础篇)
Date: 2015-04-17 22:09
Category: Web
Tags: CSS, SASS
Author: 刘理想

##1. sass和scss形式的相互转换

```
$sass-convert main.sass main.scss
或者
$sass-convert main.scss main.sass
```

##2. 创建应用

```
$compass create learn-sass-syntax
$cd learn-sass-syntax
$compass watch
```

##3. 语法

SASS CSS默认都是UTF-8，所以写不写`@charset "UTF-8"`

###3.1 引用@import

使用下划线命名的文件比如_variables.scss，sass称为局部文件，是用到其它文件中的。如果在其他文件中引用，请使用:

```
@import "variables";
```

这个不是css中的import，css中的import指令有两大弊端，一，必需放在文件行首；
二，只有执行到对应行中才加载。

sass中的import是引入文件到宿主文件。可以使用配置选项配置路径。

`@import "compass/reset";`使用normalize来统一，比较好。

使用CSS原声@import的既定规则：
- @import后跟.css结尾的时候
- @import后跟http://开头的字符串
- @import 跟url()
- @import 后带有media queries

注意sass的@import既定规则：
1. 没有文件后缀名的时候，sass会添加.scss或者.sass的后缀
2. 统一目录下，局部文件和非局部文件不能重名
3. 可以同时import多个文件:`@import "variables", "compass/reset";`

###3.2 变量声明

```
$headline-ff: Braggadocio, Arial, Verdana, Helvetica, sans-serif;
$main-sec-ff: Arial, Verdana, Helvetica, sans-serif;
```

###3.3 注释

```
/*会被引用到编译后的css文件中*/
//不会被引用到对应的css文件中
```

###3.4 嵌套

类似LESS

```
.main-sec{
    font-family: $main-sec-ff;

    .headline{
        font-family: $main-sec-ff;
    }
}
```

###3.5 父类选择器

同LESS的&

###3.6 属性嵌套

LESS中没有这个，注意要用冒号。

```
.headline{
    font:{
        family: $main-sec-ff;
        size: 16px;
    }
}
```

