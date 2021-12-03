class Min_Heap:
    def __init__(self):
        self.heap_list = [None]  # Node(weight=1), Node(weight=2), Node(weight=3)......etc.
        self.size = 0

    # Helper methods
    def left_child_idx(self, parent_idx):
        return parent_idx * 2

    def right_child_idx(self, parent_idx):
        return parent_idx * 2 + 1

    def parent_idx(self, child_idx):
        return child_idx // 2

    def add_node(self, weight):
        node_to_add = Node(weight)

        if self.size == 0:
            self.heap_list.append(node_to_add)
        else:
            pass



    # Returns the min value
    def pop(self):
        if self.size > 0:

            # Switches the min value with the last item in the heap, pops it, then restores the heap
            self.heap_list[1], self.heap_list[self.size] = self.heap_list[self.size], self.heap_list[1]
            min_value = self.heap_list.pop()
            self.heapify_down

        else:
            print('The heap is empty')

    # This probably isn't correct yet
    def heapify_down(self):
        # Take the first item in the heap as the current
        current_node_idx = 1

        # Heapify until the current node has no children
        while self.heap_list[current_node_idx].left_child:
            node_idx_to_swap = None

            # Check if it has a right child
            if self.right_child_idx(current_node_idx) <= self.size:

                # If it does, compare right child to left child, note which child is smaller
                right_child_idx = self.right_child_idx(current_node_idx)
                left_child_idx = self.left_child_idx(current_node_idx)
                right_child = self.heap_list[right_child_idx]
                left_child = self.heap_list[left_child_idx]

                if right_child.weight < left_child.weight:  # What if they are the same????, heap list should be a set of weights?
                    node_idx_to_swap = right_child_idx
                else:
                    node_idx_to_swap = left_child_idx

            # If no right child exists, it'll be swapped with the left child, since left children get added first
            else:
                node_idx_to_swap = self.left_child_idx(current_node_idx)

            # Swap the smaller child with the parent, set the current node to be that child
            self.heap_list[current_node_idx], self.heap_list[node_idx_to_swap] = self.heap_list[node_idx_to_swap], self.heap_list[current_node_idx]

            # Set the current node to be the node at the swapped index
            current_node_idx = node_idx_to_swap



