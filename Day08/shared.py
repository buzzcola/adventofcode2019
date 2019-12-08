def chunk(list, chunkSize):
    result = []
    for i in range(0, len(list), chunkSize):
        result.append(list[i:i + chunkSize])
    return result