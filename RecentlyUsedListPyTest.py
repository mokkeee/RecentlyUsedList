#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from RecentlyUsedList import RecentlyUsedList

__author__ = 'mokkeee'


class TestEmptyList:
    sut = RecentlyUsedList()

    def test_リストの長さが0であること(self):
        assert len(self.sut) == 0

    def test_リストに要素がないこと(self):
        assert list(self.sut) == []


class TestOneElementList:
    sut = RecentlyUsedList().append("one")

    def test_リストの長さが１であること(self):
        assert len(self.sut) == 1


class TestError:
    sut = RecentlyUsedList().append("one")

    def test_リストの長さ以上のデータアクセスはエラーとなること(self):
        with pytest.raises(IndexError):
            print(self.sut[1])

    def test_リスト要素を直接指定したデータ追加はエラーとなること(self):
        with pytest.raises(TypeError):
            self.sut[1] = "two"


@pytest.mark.parametrize(('datalist', 'capacity', 'expect_list'), [
    ([], None, []),
    ([], 1, []),
    (['one'], None, ['one']),
    (['one', 'one'], None, ['one']),
    (['one', 'two'], 1, ['two']),
    (['one', 'two', 'three'], None, ['three', 'two', 'one']),
    (['one', 'two', 'one'], None, ['one', 'two']),
    (['one', 'two', 'three'], 2, ['three', 'two'])
])
def test_追加したデータとキャパシティに応じたリストが作成されること(datalist, capacity, expect_list):
    sut = RecentlyUsedList(capacity=capacity)
    for data in datalist:
        sut.append(data)

    assert list(sut) == expect_list

