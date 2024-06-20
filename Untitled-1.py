class node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,value):
        new_node = node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.value)
            current = current.next
        return elements
    
    def sort_ascending(self):
        if self.head is None:
            return
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert_ascending(sorted_list, current)
            current = next_node
        self.head = sorted_list
        
    def sorted_insert_ascending(self,head_ref, new_node):
        if head_ref is None or head_ref.value >= new_node.value:
            new_node.next = head_ref
            return new_node
        else:
            current = head_ref
            while current.next and current.next.value < new_node.value:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return head_ref
    
    def sort_descending(self):
        if self.head is None:
            return
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert_descending(sorted_list, current)
            current = next_node
        self.head = sorted_list
        
    def sorted_insert_descending(self, head_ref, new_node):
        if head_ref is None or head_ref.value <= new_node.value:
            new_node.next = head_ref
            return new_node
        else:
            current = head_ref
            while current.next and current.next.value > new_node.value:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return head_ref
    
    def search(self,value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

        
def main():
    linked_list = LinkedList()
    numbers = input("enter numbers").split()
    for number in numbers:
        linked_list.append(int(number))
        
    print("Original list")
    print(linked_list.traverse())
    
    linked_list.sort_ascending()
    print("sorted list ascending:")
    print(linked_list.traverse())
    
    linked_list.sort_descending()
    print("sorted list descending:")
    print(linked_list.traverse())
    
    search_number = int(input("enter the number you want to search: "))
    if linked_list.search(search_number):
        print(f"The number {search_number} is present in the list")
    else:
        print(f" The number {search_number} is not present in the list:")
        
if __name__ == "__main__":
    main()
