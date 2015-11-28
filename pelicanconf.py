#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '理想'
SITENAME = 'liulixiang1988的博客'
SITEURL = 'http://liulixiang1988.github.io'
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
SOCIAL = (('微博', 'http://weibo.com/liulixiang1988'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'pelican-elegant-1.3'

DUOSHUO_SITENAME = "liulixiang1988"

GITHUB_USER = "liulixiang1988"
GITHUB_SHOW_USER_LINK = True

SIDEBAR_IMAGE = "images/avatar.jpg"
SIDEBAR_IMAGE_ALT = "刘理想"

SEARCH_BOX = True

LANDING_PAGE_ABOUT = {
    "title": "Liu Lixiang",
    "details": """
My Name is Liu Lixiang. I'm a software engineer in Tongling Nonferrous Metals Group.
    """
}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']
MD_EXTENSIONS = ['toc', 'codehilite(css_class=highlight)', 'extra', 'headerid']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
