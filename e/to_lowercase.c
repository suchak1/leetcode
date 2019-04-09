char* toLowerCase(char* str) {

    for(int i = 0; str[i] != '\0'; i++)
    {
        if(str[i] >= 'A' && str[i] <= 'Z')
            str[i] = 'a' + str[i] - 'A';
    }
    
    return str;
    
    
}


//0ms, 100.00%
