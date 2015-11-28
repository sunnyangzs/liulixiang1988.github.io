Title: React使用笔记(3)-React Event Listener
Date: 2015-11-28 12:18
Category: Web
Tags: JavaScript
Author: 刘理想

[TOC]

##1. 构造基本结构

首先，我们先创建一个按钮，一个输入框。我们准备点击按钮时，后面有一个`<span>`显示和隐藏。代码如下：

```jsx
<div id="container"></div>
<script type="text/jsx">
    var TestClickComponent = React.createClass({
        render: function(){
            return (
                <div>
                    <button>显示|隐藏</button>
                    <span>测试点击</span>
                </div>
                );
        }
    });

    var TestInputComponent = React.createClass({
        getInitialState: function(){
            return {
                inputContent: ''
            }
        },
        render: function(){
            return (
                <div>
                    <input type="text" /><span>{this.state.inputContent}</span>
                </div>
                );
        }
    });

    React.render(
        <div>
            <TestClickComponent />
            <TestInputComponent />
        </div>,
        document.getElementById('container'));
</script>
```

这里有几点需要注意，在`render`里返回的时候，需要用个`<div>`包裹起来，因为每个里面有好几html标签。

##2. 给`<button>`添加事件绑定

用驼峰式命名的方式来绑定事件，比如`onClick`。注意这里的`onClick`事件和原生HTML属性中的`onclick`不是一回事儿。这里，它并不是一个真事的DOM节点，它只是一个React Element，而且写法也不一样，HTML标签的属性对于大小写是不敏感的，而React Element对于大小写是敏感的。

`onClick`的处理函数一般通过对象属性封装在React组件的对象实例上。

```jsx
var TestClickComponent = React.createClass({
    handleClick: function(event){
        
    },

    render: function(){
        return (
            <div>
                <button onClick={this.handleClick}>显示|隐藏</button>
                <span>测试点击</span>
            </div>
            );
    }
});
```

`handleClick`函数的参数是React封装的`event`对象。这个`event`对象是在原生的js的`event`对象的基础上封装的，因此，我们可以调用一些在原生js的`event`对象上的方法：

```js
handleClick: function(event){
    event.stopPropagation();
    event.preventDefault();
}
```

我们如何在`event`事件处理函数内处理`<span>`呢，我们通过给`<span>`添加一个`ref`属性，然后就能在`this.refs`中获取这个对象了。

```jsx
<span ref="tip">测试点击</span>
```

注意，我们使用`this.refs.tip`引用的并不是真实的DOM节点，而是React组件。我们要操作DOM节点该怎么办呢？使用React给我们封装的方法`React.findDOMNode`，参数就是我们的React组件。

```jsx
handleClick: function(event){
    var tipE = React.findDOMNode(this.refs.tip)

    if (tipE.style.display === 'none'){
        tipE.style.display = 'inline';
    } else {
        tipE.style.display = 'none';
    }
    event.stopPropagation();
    event.preventDefault();
}
```

##3. 给`<input>`添加事件绑定

我们给`<input>`添加`onChange`事件，这里我们使用`event.target.value`来获取`<input>`的值，然后设置`state`，对应的`<span>`的内容就会跟着改变。

```jsx
changeHandler: function(event){
    this.setState({
        inputContent: event.target.value
    });
    event.preventDefault();
    event.stopPropagation();
},
render: function(){
    return (
        <div>
            <input type="text" onChange={this.changeHandler}/><span>{this.state.inputContent}</span>
        </div>
        );
}
```

作者：liulixiang1988#gmail.com (#换成@)
参考链接：http://www.imooc.com/learn/504