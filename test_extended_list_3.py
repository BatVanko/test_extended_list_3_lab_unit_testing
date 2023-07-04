import unittest


class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest
from unittest import TestCase, main


class TestIntegerList(TestCase):
    def test_initial_integers_by_constructor(self):
        in_list = IntegerList()
        self.assertEqual([], in_list._IntegerList__data)
        in_list.add(1)
        self.assertEqual([1], in_list._IntegerList__data)

    def test_if_get_data_returns_correct_data(self):
        in_list = IntegerList(1, 2, 3, 4)
        data_in = in_list.get_data()
        self.assertEqual([1, 2, 3, 4], data_in)

    def test_if_add_element(self):
        in_list = IntegerList(1, 2, 3, 4)
        self.assertEqual([1, 2, 3, 4], in_list._IntegerList__data)
        in_list.add(4)
        self.assertEqual([1, 2, 3, 4, 4], in_list._IntegerList__data)

    def test_if_raise_exception_when_try_to_add_not_int_element(self):
        in_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(Exception) as ex:
            in_list.add('oooo')
        self.assertEqual("Element is not Integer", str(ex.exception))
        with self.assertRaises(Exception) as ex:
            in_list.add(2.5)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_try_to_delete_negative_index(self):
        in_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError) as ex:
            in_list.remove_index(-1)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_try_to_delete_positive_out_of_range_index(self):
        in_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError) as ex:
            in_list.remove_index(4)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_try_to_delete_not_integer_index(self):
        in_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(Exception) as ex:
            in_list.remove_index('i')
    def test_raise_exception_when_try_to_get_negative_index(self):
        in_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(Exception) as ex:
            in_list.get(-1)
        self.assertEqual("Index is out of range", str(ex.exception))
    def test_raise_exception_when_try_to_get_positive_index_out_of_range(self):
        in_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(Exception) as ex:
            in_list.get(4)
        self.assertEqual("Index is out of range", str(ex.exception))
    def test_try_to_insert_element_on_negative_index(self):
        in_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError) as er:
            in_list.insert(-1,20)
        self.assertEqual("Index is out of range", str(er.exception))
    def test_try_to_insert_element_on_positive_index_out_of_range(self):
        in_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(IndexError) as er:
            in_list.insert(5,20)
        self.assertEqual("Index is out of range", str(er.exception))
    def test_try_to_insert_not_integer_element(self):
        in_list = IntegerList(1, 2, 3, 4)
        with self.assertRaises(ValueError) as er:
            in_list.insert(1, 'a')
        self.assertEqual(("Element is not Integer"), str(er.exception))

    def test_try_to_get_biggest_el(self):
        in_list = IntegerList(1, 2, 3, 4)
        result = in_list.get_biggest()
        self.assertEqual(4,result)

    # def test_str(self):
    #     in_list = IntegerList(1, 2, 3, 4)
    #     self.assertEqual([1, 2, 3, 4], str( in_list))

    def test_try_if_el_on_index(self):
        in_list = IntegerList(1, 2, 3, 4)
        result = in_list.get_index(4)
        self.assertEqual(3,result)



if __name__ == '__main__':
    main()
