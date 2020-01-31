from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If self.capacity is equal to the length of self.storage.
        if self.capacity == len(self.storage):
            
            # If self.current is None.
            if self.current is None:
                
                # Then self.current is equal to self.storage.tail, which we need when we move it to the end.
                self.current = self.storage.tail
                
            # Then the self.current.value is set to an item.
            self.current.value = item
            
            # If self.current.prev.
            if self.current.prev:
                
                # Then set the self.current to equal to self.current.prev
                self.current = self.current.prev
                
            # Otherwise set self.current to equal to self.storage.tail
            else:
                self.current = self.storage.tail
                
        # Otherwise the length of the self.storage is less(<) than the self.capacity.
        elif len(self.storage) < self.capacity:
            
            # Then we want to add to the head
            self.storage.add_to_head(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # We set the storage_node to the end of the storage.
        storage_node = self.storage.tail
        
        # While the storage_node.
        while storage_node:
            
            # If the storage_node.value is not None.
            if storage_node.value is not None:
                
                # Then list_buffer_contents appends the sotrage_node.value.
                list_buffer_contents.append(storage_node.value)
                
            # And the storage_node is set to equal to storage_node.prev.
            storage_node = storage_node.prev
            
        # Now return the list_buffer_contents
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
