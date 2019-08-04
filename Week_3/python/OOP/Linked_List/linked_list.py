class SLNode:
    def __init__(self,val):
        self.value = val
        self.next = None

class SLList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head	# save the current head in a variable
        new_node.next = current_head
        self.head = new_node
        return self
    def print_values(self):
        runner = self.head
        while runner!= None:
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):	# accepts a value
        if self.head == None:
            self.add_to_front(val)
            return self

        new_node = SLNode(val)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self):
        if self.head != None and self.head.next != None: # check if list is empty or if list has only 1 element
            print(f"Removed: {self.head.value}")
            self.head = self.head.next
        else:
            self.head = None # if list has one element, just set the head to None
        return self

    def remove_from_back(self): # implement edge case checks
        runner = self.head
        while(runner.next.next != None):
            runner = runner.next
        print(f"Removed: {runner.next.value}")
        runner.next = None
        return self
    def remove_val(self,val):
        curr = self.head
        prev = None
        # while runner.value != val:
        #     prev = runner
        #     runner = runner.next
        # prev.next = prev.next.next
        # runner = runner.next
        # runner.next = None
        # return self
        while curr != None:
            if curr.value == val:
                if prev != None: # if it didn't find the value at the first position
                    prev.next = curr.next
                else:
                    self.head = curr.next #first element
            prev = curr
            curr = curr.next
        return self
    def insert_at(self, val, n):
        new_node = SLNode(val)
        count = 0
        curr = self.head
        if not self.head or n == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            while count < n -1 and curr.next != None:
                curr = curr.next
                count += 1
            new_node.next = curr.next
            curr.next = new_node
        return self




my_list = SLList()
#my_list.add_to_front("world").add_to_front("hello").add_to_back("I am supposed to be in the back").remove_from_front().print_values()
#my_list.remove_from_front().print_values()
# my_list.add_to_front("hello").remove_from_front().print_values()
# my_list.add_to_front("world").add_to_front("hello").add_to_front("again").remove_from_front().print_values()
# my_list.add_to_front("hello").add_to_back("world").add_to_back("Eric").remove_from_back().print_values()
#my_list.remove_from_back().print_values() # have to implement this check

#my_list.add_to_front("world").add_to_front("hello").add_to_front("again").remove_val("again").print_values()
#my_list.add_to_front("world").add_to_front("hello").add_to_front("again").remove_val("world").print_values()
#my_list.add_to_front("world").add_to_front("hello").add_to_front("again").remove_val("hello").print_values()

my_list.insert_at("one", 0)
my_list.insert_at("two", 1)
my_list.insert_at("three", 1)
my_list.print_values()
