Title: Java Web之JSP-03 JSP内置对象
Date: 2015-04-09 16:47
Category: Java
Tags: Java, Web, JSP
Author: 刘理想

##1. jsp内置对象简介

1、JSP内置对象是Web容器创建的一组对象，【不使用new关键字】就可以使用的内置对象。
2、九大内置对象:
out,request,response,session,application（五大常用对象）
Page,pageContext,exception.config（四个不太常用对象）

##2. out对象

缓冲区Buffer：就是内存的一块区域涌来保存临时数据。

out是JspWriter 的实例,是向客户端输出内容的常用对象.
常用方法:

1. void println() 向客户端打印字符串.
2. void clear() 清除缓冲区,在flush之后调用会抛出异常.
3. void clearBuffer() 清除缓冲区,在flush之后调用不会抛出异常.
4. void flush() 将缓冲区内容输出到客户端.
5. int getBufferSize() 
6. int getRemaining()
7. boolean isAutoFlush() 返回缓冲区满时，是自动清空还是抛出异常
8. void close() 关闭输出流

##3. Get和Post提交方式的区别

表单有两种提交方式：get与post。定义在`<form action="dologin.jsp" name="loginForm" method="提交方式***"></form>` 动作／名称等顺序无所谓。
1.get：以【明文】方式，通过URL提交数据，数据在URL中【可以看到】。提交数据最多不超过【2KB】。安全性较低，但效率比post方式高。适合提交数据量不大，且安全要求不高的数据：比如：搜索、查询等功能。
2.post：将用户提交的信息封装在HTML HEADER内。适合提交数据量大，安全性高的用户信息。如：注册、修改、上传等功能。

##4. request对象

客户端的请求信息被封装在request对象中，它是HttpServletRequest类的实例。request对象具有请求域，即完成客户端的请求之前，该对象一直有效。常用方法如下：

1. String getParameter(String name) 返回name制定的参数值
2. String[] getParameterValues(String name) 返回包含参数name的所有值的数组（如复选框的值）。
3. void setAttribute(String, Object) 存储此请求中的属性
4. object getAttribute(String name) 返回制定属性的属性值
5. String getContentType() 得到请求体的mime类型
6. String getProtocol() 返回请求用的协议类型及版本号
7. String getServerName() 返回接受请求的服务器主机名
8. int getServerPort();//返回服务器接受此请求所用的端口号
9. String getCharacterEncoding();//返回字符编码方式
10. void setCharacterEncodinng();//设置请求的字符编码方式
11. int getContentLength();//返回请求体的长途(以字节数)
12. String getRemoteAddr();//返回发送此请求的客户端IP地址,IP地址为IPv6本地环回地址。
13. String getRealPath(String path);//返回虚拟路径的真实路径
14. String request.getContextPath();//返回上下文路径

使用关键：
1. 单个参数的获取使用getParameter(String name), 多个参数的获取getParameterValues(String name)。在使用这两个方法是，需传递对应的参数name，这个name应是在表格中声明的对象。
2. 不存在参数值的方法，直接使用表达式即可获取，例如：`<%=request.getContentType()%>`
3. 传递中文参数时，可能会出现乱码情况，需声明：`request.setCharacterEncoding("utf-8");`但此方法不能解决使用url传递中文时出现的乱码，若想解决这个，需要在server.xml的connector的末尾加上:`URIEncoding="utf-8"`

##5. response对象

response对象包含了响应客户请求的有关信息，但在JSP中很少直接用到它，它是HttpServletResponse类的实例，response对象具有页面作用域，即访问一个页面时，该页面内的response对象只能对这次访问有效，其它页面的response对象对当前页面无效。
常用方法：

1. String getCharacterEncoding();//返回响应的是何种字符编码
2. void setContentType(String type);//设置响应MIME类型
3. PrintWriter getWriter();//返回可以想客户端输出字符的一个对象PrintWriter
4. sendRedirect(java.lang.String location);//重新定向客户端请求

PrintWriter比out对象先打印。调用out.flush()可以解决

###5.1 JSP内置对象——请求转发与请求重定向的区别

1. 请求重定向：服务端responce.sendRedirect("xx.jsp")重定向。【客户端行为】：即客户端会访问两次，第一次访问后会立即跳转到第二个重定向页面上，【从本质上讲等于两次请求】，而前一次的请求封装的request对象不会保存，地址栏的URL地址会改变。
2. 请求转发：服务端request.getRequestDispatcher("xx.jsp").forward(request,response)请求转发。forward(request,response)用于保存内置对象request和response。【服务器行为】：服务器会代替客户端去访问转发页面，【从本质是一次请求】，转发后请求对象会保存，地址栏的URL地址不会改变。

##6. session对象

一、什么是session

1. session表示客户端与服务器的一次会话
2. Web中的session指：用户在浏览某个网站时，从进入网站到浏览器关闭所经过的这段时间，也就是用户浏览网站所花费的时间。
3. 从上述定义中可以看到，session实际是一个【特定的时间概念】
4. 服务器的内存中，保存着不同用户的不同的session。

二、session对象常用方法

1. long getCreationTime() 返回session创建时间
2. public String getId() 返回创建时jsp引擎为它设的唯一id号
3. public Ojbect setAttribute(String name, Object value) 使用指定名称将对象绑定到此对话
4. public Object getAttribute(String name) 返回此会话中的指定名称绑定在一起的对象，如果没有对象绑定在该名称下，则返回null
5. String[] getValueNames() 返回一个包含此session中所有可用属性的数组
6. int getMaxInactiveInterval() 返回两次请求间隔多长时间此session被取消（单位秒）
7. setMaxInactiveInterval(int)可以设置session存活的最长时间，在时间过了之后，服务器会创建全新的一个session。前一个session的内容无法被传递到新的session。
