def iterateChars(text):
    word_count = 0;
    sentence_count = 0;
    number_count = 0;
    letter_count = 0;
    special_count = 0;

    for t in text:
        # ord(t) behaves like (int)t when converted to C#
        # print(str(ord(t)) + ' '); 
        num = ord(t);
        if num == 32:
            word_count+=1;

        if num == 46 or num == 46 or num == 46:
            sentence_count+=1;

        if num >= 48 and num <= 57:
            number_count+=1;
        elif num >= 65 and num <= 90:
            letter_count+=1;
        elif num >= 97 and num <= 122:
            letter_count+=1;
        else:
            special_count+=1;
    
    word_count+=1;
    print('Word Count is ' + str(word_count));
    print('Sentence Count is ' + str(sentence_count));
    print('Number Count is ' + str(number_count));
    print('Letter Count is ' + str(letter_count));
    print('Special Count is ' + str(special_count));


if __name__ == '__main__':
    text = 'The template for all modern computers is the Von Neumann architecture, detailed in a 1945 paper by Hungarian mathematician John von Neumann. This describes a design architecture for an electronic digital computer with subdivisions of a processing unit consisting of an arithmetic logic unit and processor registers, a control unit containing an instruction register and program counter, a memory to store both data and instructions, external mass storage, and input and output mechanisms. The meaning of the term has evolved to mean a stored-program computer in which an instruction fetch and a data operation cannot occur at the same time because they share a common bus. This is referred to as the Von Neumann bottleneck and often limits the performance of the system.';
    #print(text);
    iterateChars(text);