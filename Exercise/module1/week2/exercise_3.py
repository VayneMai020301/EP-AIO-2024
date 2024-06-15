
def count_token(path_file):

    token_dict = {}

    with open(path_file, "r") as file :
        data  = file.readlines()
        for line in data:
            line = line.strip("\n")
            for token in line.split(" "):
                if token not in token_dict.keys():
                    token_dict[token] = 1
                else:
                    token_dict[token] += 1

    return token_dict

if __name__ == "__main__":
    assert count_token("test.txt") == {
        "mai": 2,
        "trung":2,
        "kien":2
    }
    assert count_token("P1_data.txt")["who"] ==3 
    print (count_token("P1_data.txt")["man"])
