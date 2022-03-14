def calculate_storage(filesize):
    """ 1-Use floor division to calculate
    how many blocks are fully occupied
    2-Use the modulo operator to check whether
    there's any remainder
    3-Depending on whether there's a remainder or not, return
    the total number of bytes required to allocate enough blocks
    to store your data."""
    block_size = 4096
    full_blocks = block_size // filesize
    partial_block_remainder = full_blocks % block_size
    if partial_block_remainder > 0:
        return block_size
    return full_blocks


print(calculate_storage(1))  # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192
