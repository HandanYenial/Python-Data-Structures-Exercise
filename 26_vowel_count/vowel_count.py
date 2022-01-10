
vowels=set("aeiou")
def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase=phrase.lower()
    num_vowels={}
    
    for letter in phrase:
        if letter in vowels:
            num_vowels[letter]=num_vowels.get(letter,0)+1
            
    return num_vowels
    
    