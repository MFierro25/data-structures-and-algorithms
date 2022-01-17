def left_join(hash_left, hash_right):
    
    return_hash = {}
    
    for key, in hash_left:
        return_hash.update(key)
        return_hash.update(hash_left[key])
        
        if key in hash_right:
            return_hash.update(hash_right[key])
        else:
            return_hash.update(None)
            
    return return_hash.keys()