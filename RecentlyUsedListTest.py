#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'mokkeee'

from RecentlyUsedList import RecentlyUsedList

from unittest import TestCase
import hamcrest as hc
import unittest


class EmptyListTest(TestCase):
    def setUp(self):
        self.sut = RecentlyUsedList()

    def test_リストの長さが0であること(self):
        hc.assert_that(self.sut, hc.has_length(0))


class OneElementListTest(TestCase):
    def setUp(self):
        self.sut = RecentlyUsedList()
        self.sut.append("a")

    def test_リストの長さが1であること(self):
        hc.assert_that(self.sut, hc.has_length(1))

    def test_リストは追加要素のみのリストであること(self):
        hc.assert_that(list(self.sut), ["a"])


class ThreeElementsListTest(TestCase):
    def setUp(self):
        self.sut = RecentlyUsedList()
        self.sut.append("first").append("second").append("last")

    def test_リストの長さが３であること(self):
        hc.assert_that(self.sut, hc.has_length(3))

    def test_リストの先頭要素が最後に追加したデータであること(self):
        hc.assert_that(self.sut[0], hc.equal_to("last"))

    def test_リストの最終要素が最初に追加したデータであること(self):
        hc.assert_that(self.sut[2], hc.equal_to("first"))


class DuplicateElementsAddListTest(TestCase):
    def setUp(self):
        self.sut = RecentlyUsedList()
        self.sut.append("first").append("second").append("third").append("second")

    def test_リストの長さが３であること(self):
        hc.assert_that(self.sut, hc.has_length(3))

    def test_リストの先頭要素が最後に追加したデータであること(self):
        hc.assert_that(self.sut[0], hc.equal_to("second"))

    def test_リスト内のデータが先頭に移動されていること(self):
        hc.assert_that(list(self.sut), hc.equal_to(["second", "third", "first"]))


class HaveCapacityList(TestCase):
    def setUp(self):
        self.sut = RecentlyUsedList(capacity=3)
        self.sut.append("first").append("second").append("third").append("last")

    def test_リストの長さが３であること(self):
        hc.assert_that(self.sut, hc.has_length(3))

    def test_リストの先頭要素が最後に追加したデータであること(self):
        hc.assert_that(self.sut[0], hc.equal_to("last"))

    def test_リストの最終要素が最初に追加したデータであること(self):
        hc.assert_that(self.sut[2], hc.equal_to("second"))

    def test_最初に追加したデータがリストから消去されていること(self):
        self.assertNotIn("first", self.sut)


class ErrorTest(TestCase):
    def setUp(self):
        self.sut = RecentlyUsedList()
        self.sut.append("1").append("2")

    def test_配列要素指定のデータ追加はエラーとなること(self):
        try:
            self.sut[1] = "aaaa"
            self.fail()
        except TypeError:
            pass
        except:
            raise

    def test_データ数以上の要素アクセスでエラーとなること(self):
        hc.assert_that(hc.calling(self.sut.__getitem__).with_args(2), hc.raises(IndexError))


if __name__ == '__main__':
    unittest.main()
