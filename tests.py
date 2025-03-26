import pytest
from main import MemoryManager

#Test case: Test allocation works
def test_allocation():
    mm = MemoryManager(5)
    pointers = [mm.alloc(1) for _ in range(5)]
    assert pointers == [0, 1, 2, 3, 4]


#Test case: Test allcoation after free
def test_valid_free():
    mm = MemoryManager(5)
    pointers = [mm.alloc(1) for _ in range(5)]
    assert pointers == [0, 1, 2, 3, 4]

    mm.free(pointers[1])
    new_ptr = mm.alloc(1)
    assert new_ptr == 1


#Test case: invalid freeing of a slot that is already free
def test_invalid_free():
    mm = MemoryManager(10)
    ptr = mm.alloc(3)
    mm.free(ptr)
    with pytest.raises(ValueError):
        mm.free(ptr)

#Test case: allocating a block
def test_allocation_with_fragmented_buffer():
    mm = MemoryManager(5)
    pointers = [mm.alloc(1) for _ in range(5)]
    mm.free(pointers[1])
    mm.free(pointers[3])
    assert mm.alloc(2) is None

# Test case: merging adjacent free slots
def test_merge_free_slots():
    mm = MemoryManager(10)
    ptr1 = mm.alloc(3)  
    ptr2 = mm.alloc(2)  
    ptr3 = mm.alloc(3)  

    # Free up first 2 ptr to merge free slots
    mm.free(ptr2)
    mm.free(ptr1)
    # Should start allocating at 0
    new_ptr = mm.alloc(5)
    assert new_ptr == 0


# Edge case: invalid ptr, ptr out of bound or not in the buffer, ptr > size or ptr < 0
def test_out_of_bound_free():
    mm = MemoryManager(10)
    with pytest.raises(ValueError):
        mm.free(12)
    with pytest.raises(ValueError):
        mm.free(-1)

# Edge case: allocating into a full buffer
def test_allocating_into_full_buffer():
    mm = MemoryManager(5)
    for _ in range(5):
        assert mm.alloc(1) is not None
    assert mm.alloc(1) is None
    