class MemoryManager:
    def __init__(self, num_bytes: int):
        #free_slots and allocated_slots both contain pointers
        self.size = num_bytes
        self.free_slots = [(0, num_bytes)]
        self.allocated_slots = {}


    def alloc(self, size: int):
        # Check for valid free slots
        for i in range(len(self.free_slots)):
            start = self.free_slots[i][0]
            free_slot_size = self.free_slots[i][1]
         
            if free_slot_size >= size:
                if free_slot_size == size:
                    self.free_slots.pop(i)
                else:
                    leftover_slot_size = free_slot_size - size
                    leftover_slot = (start + size, leftover_slot_size)
                    self.free_slots[i] = leftover_slot
                self.allocated_slots[start] = size
                return start
        return None



    def free(self, ptr: int):
        if ptr < 0 or ptr > self.size:
            raise ValueError("Invalid pointer")
        if ptr not in self.allocated_slots:
            raise ValueError("Invalid pointer")
        else:
            allocated_size = self.allocated_slots.get(ptr)
            del self.allocated_slots[ptr]
            self.free_slots.append((ptr, allocated_size))
            # Sort the free slots by starting index to simplify merging
            # Find free adjacent slots to merge
            self.free_slots.sort()
            merged_free_slots = []
            for slots in self.free_slots:
                if merged_free_slots and (merged_free_slots[-1][0] + merged_free_slots[-1][1] == slots[0]):
                    prev_start, prev_size = merged_free_slots[-1]
                    merged_free_slots[-1] = (prev_start, prev_size + slots[1])
                else:
                    merged_free_slots.append(slots)
            self.free_slots = merged_free_slots


            




