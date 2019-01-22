#! /usr/bin/env python
# -*- coding: utf-8 -*-

#    File Name：       demo04_异常类型
#    Description :
#    Author :          SanYapeng
#    date：            2019/1/21
#    Change Activity:  2019/1/21:

"""
使用 try except
    1 预先避免风险
        try：
            可能产生异常的代码
        except 异常类型 as e:


    2 运行，产生问题
         先修改代码
         再使用try

    try：

    except: 不写代表匹配所有问题

    except Exception

    except Exception as e:  # e 可以是任意字符，也可以是 result 用来接收错误信息

"""