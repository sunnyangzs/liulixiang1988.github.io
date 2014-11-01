title:使用Android开发一个阅后即焚-03 在tab中使用fragment
date:2014-10-15 23:06
category:Android
tags:Android
author:刘理想
summary:在tab中使用fragment

##1. 为什么使用fragment?

简而言之，fragment可以让我们复用设计和代码。

##2. fragment如何作为tab使用

- 在Activity里创建一个fragment container
- 创建fragment对应的class和layout
- 在Activity中添加初始化的fragment。当Activity加载时，初始化的fragment也应该加载
- 添加tab到Action Bar。Action Bar用来控制和显示tab
- 添加`TabListener`来加载新的fragment

可以在layout中使用fragment元素来显示的包含fragment。

##3. 从模板中修改tab

tab中的fragment到底是在哪里定义的呢？我们打开MainActivity，看到文件最后，定义了静态类：

```java
public static class PlaceholderFragment extends Fragment {
    /**
     * The fragment argument representing the section number for this
     * fragment.
     */
    private static final String ARG_SECTION_NUMBER = "section_number";

    /**
     * Returns a new instance of this fragment for the given section
     * number.
     */
    public static PlaceholderFragment newInstance(int sectionNumber) {
        PlaceholderFragment fragment = new PlaceholderFragment();
        Bundle args = new Bundle();
        args.putInt(ARG_SECTION_NUMBER, sectionNumber);
        fragment.setArguments(args);
        return fragment;
    }

    public PlaceholderFragment() {
    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
            Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.fragment_main, container, false);
        return rootView;
    }
}
```

现在先不对这个类做太多深入了解，我们往上看，会看到一个`SectionsPagerAdapter`类的定义，这个类用可以看作是mvc中的控制器，用来连接视图和模型，其中视图就是屏幕，模型就是Fragment。

我们把它抽出来存放到一个单独的类中：

```java
public class SectionsPagerAdapter extends FragmentPagerAdapter {

    private Context mContext;

    public SectionsPagerAdapter(Context context, FragmentManager fm) {
        super(fm);
        mContext = context;
    }

    @Override
    public Fragment getItem(int position) {
        // getItem is called to instantiate the fragment for the given page.
        // Return a PlaceholderFragment (defined as a static inner class below).
        return MainActivity.PlaceholderFragment.newInstance(position + 1);
    }

    @Override
    public int getCount() {
        // Show 2 total pages.
        return 2;
    }

    @Override
    public CharSequence getPageTitle(int position) {
        Locale l = Locale.getDefault();
        switch (position) {
            case 0:
                return mContext.getString(R.string.title_section1).toUpperCase(l);
            case 1:
                return mContext.getString(R.string.title_section2).toUpperCase(l);
        }
        return null;
    }
}
```

注意，因为`getString`是`Context`类的方法。因此，我们需要传进来`Context`，而`Activity`类是`Context`的子类，所以调用时将`Activity`传给它即可。

```java
// Create the adapter that will return a fragment for each of the three
// primary sections of the activity.
mSectionsPagerAdapter = new SectionsPagerAdapter(this, getFragmentManager());
```

另外，更改数量为2，两个的标题分别为“收件箱”和“好友”。

##4. 从模板中修改fragment

现在我们已经有了所有的一切，除了fragement，目前用来的还是默认的fragment。