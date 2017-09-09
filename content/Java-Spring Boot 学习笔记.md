Title: Spring Boot 学习笔记
Date: 2017-09-09 21:53
Category: Java
Tags: Spring
Author: 刘理想

[TOC]

示例代码地址：[这里](https://github.com/liulixiang1988/javademo/tree/master/spring/%E6%B7%B1%E5%85%A5%E5%AE%9E%E8%B7%B5spring-boot)



## 1. 配置

### 1.1 基本配置

#### 1.1.1 POM

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>

	<groupId>lx</groupId>
	<artifactId>deep-into-spring-boot</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<packaging>jar</packaging>

	<name>deep-into-spring-boot</name>
	<description>深入实践spring boot</description>

	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>1.5.6.RELEASE</version>
		<relativePath/> <!-- 从仓库中查找parent -->
	</parent>

	<properties>
		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
		<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
		<java.version>1.8</java.version>
	</properties>

	<dependencies>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-web</artifactId>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
		</dependency>
	</dependencies>

	<build>
		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
			</plugin>
		</plugins>
	</build>

</project>
```



#### 1.1.2 application.yml

将端口设置为8080（默认就是的，并且设置tomcat的字符集为UTF-8

```yaml
server:
  port: 8080
  tomcat:
    uri-encoding: UTF-8
```

spring boot更多预置参数请参考：

https://docs.spring.io/spring-boot/docs/current/reference/html/common-application-properties.html



### 1.2 应用配置 