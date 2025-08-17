def reversestring(text):
    result = ""
    for char in text:
        result = char + result
    return result 

print(reversestring("hello"))

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(18))

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in text:
        if char in vowels:
         count += 1 
    return count

print(count_vowels('This is Sadhika'))


def loopnumber(n):
    result = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
         result += i
    return result

print(loopnumber(100))

from collections import Counter

def most_frequent_num(numbers):
    if not numbers:
        return None
    frequency = Counter(numbers)
    most_frequent_num = frequency.most_common(1)[0][0]
    return most_frequent_num

print(most_frequent_num([1, 2, 2, 3, 4, 4, 4, 5]))

#without counter
def most_frequent(nums):
    counts = {}
    for x in nums:
        if x in counts:
            counts[x] += 1
        else: 
            counts[x] = 1

    best_value = None
    best_count = -1
    for value, count in counts.items():
        if count > best_count:
            best_value = value
            best_count = count
    return best_value

print(most_frequent([1,2,2,3,4,4,4,5]))

def most_frequest_smallest_on_tie(nums):
    counts = {}
    for x in nums:
        counts[x] = counts.get(x, 0) + 1

    max_count = max(counts.values())
    candidates = [v for v, c in counts.items() if c == max_count]
    return min(candidates) if candidates else None

print(most_frequest_smallest_on_tie([1,2,2,3,4,4,4,5]))

def count_words(text):
    words = text.split()
    return len(words)

print(count_words("This is a test. This test is only a test."))

def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    for i in range(len(cleaned_text) // 2):
        if cleaned_text[i] != cleaned_text[-(i + 1)]:
            return False
    return True

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))

def merge_sorted_lists(a, b):
    merged = []
    i, j = 0, 0 
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1 
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return set(merged)

print(merge_sorted_lists([1,2,5], [2,4,6]))

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

print(fizz_buzz(15))

def index_two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return (num_to_index[complement], i)
        num_to_index[num] = i
    return None

print(index_two_sum([2,7,11,15], 9))

def ordered_remove_duplicates(nums):
    result = []
    for num in nums:
        if num not in result:
            result.append(num)
        else:
            continue

    return sorted(result)

print(ordered_remove_duplicates([4,2,2,3,4,1,5,3]))

def char_frequency(text):
    freq = {}
    for char in text:
        if char.isalnum():
            freq[char] = freq.get(char, 0) + 1
    return freq

print(char_frequency("Hello, World!"))

def capitalize_first_letter(text):
    return text.title()

print(capitalize_first_letter("hello world! this is sadhika."))

def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)

print(are_anagrams("listen", "silent"))
print(are_anagrams("hello", "world"))

from string import punctuation

def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        cleaned_word = word.strip(punctuation)
        if len(cleaned_word) > len(longest):
            longest = cleaned_word
    return longest
    
print(longest_word("Hello, world! This is a test sentence."))

from collections import Counter

def find_duplicates(lst):
    counts = Counter(lst)
    return [item for item, count in counts.items() if count > 1]

print(find_duplicates([1,2,3,4,5,4,4,5,5]))

def group_by_first_letter(words):
    groups = {}
    for word in words:
        first_letter = word[0].lower()
        if first_letter not in groups:
            groups[first_letter] = []
        groups[first_letter].append(word)
    return groups

print(group_by_first_letter(["apple", "banana", "apricot", "blueberry", "cherry"]))

def is_perfect_square(n):
    if n < 0:
        return False
    root = int(n**0.5)
    return root * root == n

print(is_perfect_square(16))
print(is_perfect_square(17))

def is_valid_parentheses(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return not stack

print(is_valid_parentheses("()[]{}"))
print(is_valid_parentheses("(]"))
print(is_valid_parentheses("([)]"))
print(is_valid_parentheses("{[]}"))

text = "The sun is shining and the weather is sweet."

def top_words(text, n):
    words = text.lower().split()
    word_counts = Counter(words)
    frequency = word_counts.most_common(n)
    return dict(frequency)

print(top_words(text, 3))

csv_data = "name,age,city\nJohn,30,New York\nAlice,25,Boston"

def parse_csv(csv_data):
    lines = csv_data.strip().split('\n')
    header = lines[0].split(',')
    data = []
    for line in lines[1:]:
        values = line.split(',')
        entry = {header[i]: values[i] for i in range(len(header))}
        data.append(entry)
    return data

print(parse_csv(csv_data))

def custom_split(text, delimiter):
    result = []
    current_word = ""
    for char in text:
        if char == delimiter:
            if current_word:
                result.append(current_word)
                current_word = ""
        else:
            current_word += char
   
    result.append(current_word)
    return result

print(custom_split("Hello,World,This,Is,A,Test", ","))

def is_pangram(text):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    text_set = set(text.lower())
    return alphabet.issubset(text_set)

print(is_pangram("The quick dog fox jumps over 78 the lazy dog"))

def group_by_length(words):
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    return groups

print(group_by_length(["apple", "banana", "cherry", "date"]))

def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest = ""
    for i in range(len(s)):
        odd_palindrome = expand_around_center(i, i)
        even_palindrome = expand_around_center(i, i + 1)
        

        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        if len(even_palindrome) > len(longest):
            longest = even_palindrome

    return longest

print(longest_palindrome("babad"))
print(longest_palindrome("abba"))

def find_all_palindromes(s):
    palindromes = set()
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.add(s[left:right + 1])
            left -= 1
            right += 1

    for i in range(len(s)):
        odd_palindrome = expand_around_center(i, i)
        even_palindrome = expand_around_center(i, i + 1)
        palindromes.add(odd_palindrome)
        palindromes.add(even_palindrome)
    return palindromes

print(find_all_palindromes("ababa"))

def count_types(s):
    return{
        'letters': sum(c.isalpha() for c in s),
        'digits': sum(c.isdigit() for c in s),
        'spaces': sum(c.isspace() for c in s),
        'punctuation': sum(c in punctuation for c in s)
    }

print(count_types("Hello, world! 123"))

def chunk_list(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]
    return

print(list(chunk_list([1, 2, 3, 4, 5, 6, 7, 8], 3)))
