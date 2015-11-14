# -*- coding: utf-8 -*-

__author__ = 'mokkeee'


class RecentlyUsedList(object):
    def __init__(self, capacity=None):
        self.list = []
        self.capacity = capacity

    def __len__(self):
        return len(self.list)

    def __getitem__(self, index):
        return self.list[index]

    def __iter__(self):
        return iter(self.list)

    def append(self, data):
        if data in self.list:
            self._move_first(data)
        else:
            self._append_first(data)

        if self._capacity_over():
            self._remove_last()

        return self

    def _append_first(self, data):
        self.list.insert(0, data)

    def _capacity_over(self):
        if self.capacity is None:
            return False
        if self.capacity >= len(self.list):
            return False
        return True

    def _remove_last(self):
        self.list.pop()

    def _move_first(self, data):
        self.list.remove(data)
        self._append_first(data)

