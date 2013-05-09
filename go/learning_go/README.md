learning_go
=====

exercises code of book Learning Go  https://github.com/miekg/gobook

Learning Go中文版 https://github.com/mikespook/Learning-Go-zh-cn

Thanks @miekg & @mikespook , great book

顺便吐槽一下go里面的range

同样的语法, 却输出不同结果  
你说你是动态语言也就罢了, 偏偏还是强类型的编译语言

比如 range 用在 array 或 slice 上

    slice := make([]int, 10)
    for i, val := range slice {
        // 这里i输出的是序号, val才是值
        fmt.Println(i, val)
    }

    //这还好, 但是...
    //下面这样他也不会报错, 等你傻傻的运行了才发现被玩了

    for val2 := range slice {  //忘记了是两个返回值, 编译也通过了
        // val2 只是序号了
        fmt.Println(val2)
        // wtf, 打印了 0 到 9
    }

这时候你开始想念Python的 `for in` 和 `range`, `xrange` 了

再看看 range 作用于 map

    dict := make(map[string]string)
    dict["key1"] = "value1"
    dict["key2"] = "value2"

    for key, val := range dict { //输出key, val
        fmt.Println(key, val)
    }
    for key := range dict {  //只输出key
        fmt.Println(key)  
    }

还好有了前面的经验, 可以理解

然后....  
再看看 range 作用于 channel  
基于前面的经验, 你写下了下面的代码

    ch := make(chan string)
    for i, val := range ch {
        fmt.Println(i, val)
    }

纳尼, 编译不过, 他说 too many variables in range, 尼玛 range 不是单双通吃的吗? 
且channel明明可以输出两个值的啊  
像这样

    val, ok := <-ch //完全ok
    fmt.Println(val, ok)
    //这样也不会错
    val = <-ch

