from random import randint
from typing import Tuple


class ListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None


def create_num_list(num) -> ListNode:
    res = None
    last_node = None
    for digit in reversed(str(num)):
        new_node = ListNode(int(digit))
        if last_node is not None:
            last_node.next = new_node
        else:
            res = new_node
        last_node = new_node
    return res


def list2num(node: ListNode) -> int:
    res = 0
    mult = 1
    while node is not None:
        res += mult * node.value
        mult *= 10
        node = node.next
    return res


def add_two_numbers(num1: ListNode, num2: ListNode) -> ListNode:
    """
    Add two non-negative numbers represented as a linked lists.
    :param num1: first number linked list
    :param num2: second number linked list
    :return: linked list representing the sum of two numbers
    """
    assert (num1 is not None) and (num2 is not None)
    res = None
    trans_value = 0
    last_node = res

    def add_digits(val1: int, val2: int = 0, val3: int = 0) -> Tuple[ListNode, int]:
        sum_digit = val1 + val2 + val3
        new_digit, val3 = sum_digit % 10, sum_digit // 10
        new_node = ListNode(value=new_digit)
        return new_node, val3

    while num1 is not None and num2 is not None:
        new_node, trans_value = add_digits(num1.value, num2.value, trans_value)
        if last_node is not None:
            last_node.next = new_node
        else:
            res = new_node
        last_node = new_node
        num1 = num1.next
        num2 = num2.next

    while num1 is not None:
        new_node, trans_value = add_digits(num1.value, trans_value)
        last_node.next = new_node
        last_node = new_node
        num1 = num1.next

    while num2 is not None:
        new_node, trans_value = add_digits(num2.value, trans_value)
        last_node.next = new_node
        last_node = new_node
        num2 = num2.next

    if trans_value != 0:
        new_node = ListNode(value=trans_value)
        last_node.next = new_node

    return res


if __name__ == '__main__':
    num1 = 342
    num2 = 465
    num1_l = create_num_list(num1)
    num2_l = create_num_list(num2)
    assert list2num(add_two_numbers(num1_l, num2_l)) == num1 + num2

    for _ in range(100000):
        num_1, num_2 = randint(0, 99999), randint(0, 999999)
        num_1_l, num_2_l = create_num_list(num_1), create_num_list(num_2)
        true_add = num_1 + num_2
        res_node = add_two_numbers(num_1_l, num_2_l)
        assert list2num(res_node) == true_add
