#!/usr/bin/env python
#-*- coding:utf-8 -*-

from utils import Object

def test_object():
    
    foo = Object(
        bar='bar',
        baz=(1, 2, 3),
        foo1=Object(
            bar='BAR',
            baz={
                'one': 1,
                'two': 2
                }
            )
        )
    
    assert foo.bar == 'bar'
    assert foo.baz == (1, 2, 3)
    assert foo.foo1.bar == 'BAR'
    assert foo.foo1.baz['one'] == 1