#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '理想'
SITENAME = 'Liu Lixiang的博客'
# SITEURL = 'http://liulixiang1988.github.io'
SITESUBTITLE = '机器学习/Python/Android/Web'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('GitHub', 'https://github.com/liulixiang1988/'),)

# Social widget
SOCIAL = (('知乎', 'https://www.zhihu.com/people/liulixiang1988'),
          ('微博', 'http://weibo.com/liulixiang1988'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

THEME = 'gum'

DUOSHUO_SITENAME = "liulixiang1988"
DUOSHUO_SITEURL = 'http://liulixiang1988.github.io'

GITHUB_USER = "liulixiang1988"
GITHUB_SHOW_USER_LINK = True

SIDEBAR_IMAGE = "images/avatar.jpg"
SIDEBAR_IMAGE_ALT = "刘理想"

SEARCH_BOX = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search', 'render_math']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
MENUITEMS = [('分类', '/categories.html'),
             ('标签', '/tags.html'),
             ('归档', '/archives.html')]
