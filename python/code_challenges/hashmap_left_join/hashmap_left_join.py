def left_join(hash_left, hash_right):
    
    return_hash = []
    
    for key, in hash_left:
        return_hash.append(key)
        return_hash.append(hash_left[key])
        
        if key in hash_right:
            return_hash.append(hash_right[key])
        else:
            return_hash.append(None)
            
    return return_hash