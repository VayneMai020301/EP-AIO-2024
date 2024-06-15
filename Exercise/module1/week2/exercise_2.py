__doc__ ='''


'''

def character_count(string:str)->dict :
    '''
    
    '''
    result = {}

    for character in string:
        if character not in result.keys():
            result[character] = 1
        else:
            result[character] += 1
    return result

if __name__ == "__main__" :


    assert (character_count("maitrung")) == {
        "m": 1,
        "a":1 ,
        "i": 1,
        "t":1 ,
        "r":1 ,
        "u":1 ,
        "n":1 ,
        "g":1 ,
    }
    print(character_count("smiles"))