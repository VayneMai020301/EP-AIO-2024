def reverse_string(data):
    '''
        Return Reversed character in string
    
    '''
    result = ""
    for i in range(1, len(data) +1):
        result += data [-i]
    return result

if __name__ =="__main__":

    assert reverse_string("I can do it") =="ti od nac I"
    print(reverse_string("I am a student"))