def sumlist_sliceHalf(vals):
    if len(vals)==0:
        return 0
    
    new_list= vals[len(vals)//2:]
    old_list= vals[:len(vals//2)]
    return new_list[0]+ old_list[0]+sumlist_sliceHalf(new_list[1:]) + sumlist_sliceHalf(old_list[1:])

def _sumlist_pretend_sliceHalf(vals,start,end):
    if len(vals)==0:
        return 0
    return vals[start]+ _sumlist_pretend_sliceHalf(vals,start+1,end)