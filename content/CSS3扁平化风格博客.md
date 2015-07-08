Title: CSS3扁平化风格博客
Date: 2015-07-08 19:39
Category: Web
Tags: CSS3
Author: 刘理想

[TOC]
##1. 页面整体分析

做一个网页或者网站，第一步就是先定义网页与网站的结构，这是所有任务的前提。

---

##2 准备工作

在这个案例中，我们将使用Gulp, SASS和Compass来创建。

###2.1 安装Gulp
Gulp是为了后期进行自动化工作而做的。

- 如果电脑没有安装node，那么第一步就是下载node，并且安装。
- 安装http-server来查看网页: `npm install -g http-server`
- 全局安装gulp:`sudo npm install -g gulp`
- 初始化项目：`npm init`
- 安装gulp及常用库
```
npm install gulp --save-dev
npm install gulp-concat --save-dev
npm install gulp-uglify --save-dev
npm install gulp-rename --save-dev
npm install gulp-minify-css --save-dev
npm install gulp-sass --save-dev
npm install gulp-compass --save-dev
npm install gulp-sourcemaps
npm install del --save-dev
```

###2.2 安装SASS与Compass

- 如果没有安装ruby，请先安装ruby
- 配置ruby gem的source:
```
$ gem sources --remove https://rubygems.org/
$ gem sources -a https://ruby.taobao.org/
$ gem sources -l
*** CURRENT SOURCES ***
https://ruby.taobao.org

# 请确保只有 ruby.taobao.org
$ gem install rails #安装
$ gem update #更新
$ gem install sass --version=3.3
$gem uninstall sass
```
- 安装SASS
```
$gem install sass
$gem install sass --version=3.3
$sass -v
```
- 安装Compass
```
gem isntall compass
```

接下来我们来配置项目

###2.3 使用Compass配置SASS
```
compass create
```

一般来说，我们使用`compass create [项目名]`来创建项目，但是我们在之前已经使用`node init`初始化过了，所以此处我们略去项目名。

###2.4 配置bower
创建`.bowerrc`文件，然后添加：
```
{
  "directory": "lib"
}
```
这里是指定bower安装的第三方库都在lib目录下。

###2.4 创建gulp任务

在根目录下创建gulpfile.js
```
'use strict';

var gulp = require('gulp'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    rename = require('gulp-rename'),
    compass = require('gulp-compass'),
    minifyCss = require('gulp-minify-css'),
    maps = require('gulp-sourcemaps'),
    del = require('del');

//编译JavaScript
gulp.task('concatScripts', function() {
    return gulp.src([
            'js/jquery.js',
            'js/main.js'
        ])
        .pipe(maps.init())
        .pipe(concat("app.js"))
        .pipe(maps.write('./'))
        .pipe(gulp.dest('js'));
});

//压缩JavaScript
gulp.task('minifyScripts', ['concatScripts'], function() {
    return gulp.src("js/app.js")
        .pipe(uglify())
        .pipe(rename('app.min.js'))
        .pipe(gulp.dest('js'));
});

//编译SASS
gulp.task('compileSass', function() {
    return gulp.src('./scss/*.scss')
        .pipe(compass({
            config_file: './config.rb',
            css: 'css',
            sass: 'scss',
            sourcemap: true
        }))
        .pipe(gulp.dest('css'));
});

//压缩CSS
gulp.task('minifyCss', ['compileSass'], function(){
    return gulp.src("css/application.css")
        .pipe(minifyCss({compatibility: 'ie8'}))
        .pipe(rename('application.min.css'))
        .pipe(gulp.dest('css'));
});

//监视
gulp.task('watchFiles', function() {
    gulp.watch(['scss/**/*.scss', 'scss/*.scss'], ['compileSass']);
    gulp.watch('js/main.js', ['concatScripts']);
});

//清理
gulp.task('clean', function() {
    del(['dist', 'css/application*.css*', 'js/app*.js*']);
});

//构建
gulp.task('build', ["minifyScripts", "minifyCss"], function() {
    gulp.src(["css/application.min.css",
            "js/app.min.js",
            "index.html",
            "img/**",
            "fonts/**"
        ], {
            base: './'
        })
        .pipe(gulp.dest('dist'))
});

//服务
gulp.task('serve', ['watchFiles']);

//默认任务
gulp.task('default', ['clean'], function() {
    gulp.start('build');
});
```

目前为止我们的目录如下：
```
├── config.rb
├── css
├── fonts
├── gulpfile.js
├── img
│   ├── banner.jpg
│   ├── pic01.jpg
│   ├── pic02.jpg
│   └── pic03.jpg
├── index.html
├── js
│   ├── jquery.js
│   └── main.js
├── lib
├── node_modules
│   ├── del
│   ├── gulp
│   ├── gulp-compass
│   ├── gulp-concat
│   ├── gulp-rename
│   ├── gulp-sass
│   ├── gulp-sourcemaps
│   └── gulp-uglify
├── package.json
└── scss
    ├── application.scss
    └── base
        └── _normalize.scss
```

经过一番配置，后面我们只需要运行:
```
gulp serve
```
就可以监视文件的变化，并且自动进行编译了。

---
##3. 模块分析与细节实现

###3.1 重置样式与文件结构

我们使用normalize来对样式进行重置，normailze的SCSS版本在这里：https://github.com/JohnAlbin/normalize-scss 下载到`scss/base/_normalize.scss`。

然后打开`application.scss`，引入:
```
@import "base/normalize";
```
就完成对页面的重置了。
如果此时定义一个页面如下：
```
<!DOCTYPE html>
<html>
    <head>
      <link href="css/application.css" media="screen, projection" rel="stylesheet" type="text/css" />
    </head>
    <body>
        <div id="div1">
            <h1>标题1</h1>
            <h2>标题2</h2>
            <ul>
                <li>item 01</li>
                <li>item 02</li>
                <li>item 03</li>
                <li>item 04</li>
                <li>item 05</li>
            </ul>
        </div>
    </body>
</html>
```

此时运行`http-server`可以再浏览器的`localhost:8080`中进行查看。

###3.2 页头、Banner、正文、页脚的宏观布局

布局一直都是从大到小，因此刚开始不必对细节过分关注。
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>理想的博客</title>
    <link href="css/application.css" media="screen, projection" rel="stylesheet" type="text/css" />
</head>
<body>
    <!-- 页头 -->
    <header id="header" class="">
        <nav>
        </nav>
        <div id="banner"></div>
    </header>
    <!-- /页头 -->
    <!-- /内容 -->
    <div class="content">
    </div>
    <!-- /内容 -->
    <!-- 页脚 -->
    <footer>
    </footer>
    <!-- /页脚 -->
</body>
</html>
```

###3.3 页头结构分析及布局






