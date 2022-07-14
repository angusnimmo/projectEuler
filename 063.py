if __name__ == "__main__":
    count = 0

    for i in range(1, 10):
        index = 1
        
        while (index-len(str(i**index))) == 0:
            count += 1
            index += 1
                
    print(count)
