class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def print_list(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values


def reverse_linked_list(linked_list):
    previous_node = None
    current_node = linked_list.head

    while current_node is not None:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    linked_list.head = previous_node


def insertion_sort_linked_list(linked_list):
    sorted_list = SinglyLinkedList()
    current = linked_list.head

    while current:
        next_node = current.next

        if sorted_list.head is None or sorted_list.head.value >= current.value:
            current.next = sorted_list.head
            sorted_list.head = current
        else:
            search = sorted_list.head
            while search.next and search.next.value < current.value:
                search = search.next
            current.next = search.next
            search.next = current

        current = next_node

    return sorted_list


def merge_and_sort_linked_lists(list1, list2):
    merged_list = SinglyLinkedList()
    current_list1 = list1.head
    current_list2 = list2.head

    while current_list1 is not None:
        merged_list.append(current_list1.value)
        current_list1 = current_list1.next

    while current_list2 is not None:
        merged_list.append(current_list2.value)
        current_list2 = current_list2.next

    return insertion_sort_linked_list(merged_list)


# Creating Test List
example_list = SinglyLinkedList()
for value in [7, 2, 4, 3, 5]:
    example_list.append(value)

# Reverse
reverse_linked_list(example_list)
reversed_list_values = example_list.print_list()

# Order
sorted_list = insertion_sort_linked_list(example_list)
sorted_list_values = sorted_list.print_list()

# Merge
list1_random = SinglyLinkedList()
list2_random = SinglyLinkedList()
for value in [10, 5, 15]:
    list1_random.append(value)
for value in [2, 8, 7]:
    list2_random.append(value)

merged_and_sorted_list = merge_and_sort_linked_lists(
    list1_random, list2_random)
merged_and_sorted_list_values = merged_and_sorted_list.print_list()


print(reversed_list_values, sorted_list_values, merged_and_sorted_list_values)
