# 문제 1: 리스트에서 짝수만 반환하는 함수
# 리스트를 입력받아 짝수만 반환하는 함수를 작성하세요.

#def get_even_numbers(lst: list[int]):
def get_even_numbers(lst: list):
    """
    리스트에서 짝수만 반환하는 함수
    """
    #pass  # 여기에 코드를 작성하세요.
    return [x for x in lst if x%2 == 0]

# 테스트
print(get_even_numbers([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]




# 문제 2: 주어진 문자열이 회문인지 확인하는 함수
# 문자열을 입력받아 그 문자열이 회문인지 확인하는 함수를 작성하세요.
def is_palindrome(input: str):
    """
    주어진 문자열이 회문인지 확인하는 함수
    """
    #pass  # 여기에 코드를 작성하세요.
    #return True if list(input) == list(input)[::-1] else False # ok
    return True if input == input[::-1] else False
        

# 테스트
print(is_palindrome("tenet"))  # True
print(is_palindrome("소주만병만주소"))    # True
print(is_palindrome("hello"))    # False


# 문제 3: 리스트를 거꾸로 반환하는 함수
# 리스트를 입력받아 거꾸로 반환하는 함수를 작성하세요.
def reverse_list(lst: list):
    """
    리스트를 거꾸로 반환하는 함수
    """
    #pass  # 여기에 코드를 작성하세요.
    #return lst[::-1]
    lst.reverse() # .revere()는 in-place operation(원본을 직접수정하고 아무것도 반환 X)
    return lst

# 테스트
print(reverse_list([1, 2, 3, 4]))  # [4, 3, 2, 1]


#문제 4: 문자열에서 모음 개수 세는 함수
#주어진 문자열(영문자)에서 모음(a, e, i, o, u)의 개수를 세는 함수를 작성하세요.
def count_vowels(input: str):
    """
    문자열에서 모음의 개수를 세는 함수
    """
    #pass  # 여기에 코드를 작성하세요.
    #return input.count('a') + input.count('e') + input.count('i')+ input.count('o') +input.count('u')

    # count = 0
    # for ch in input:
    #     #if ch in ['a', 'e', 'i', 'o', 'u']
    #     if ch in 'aeiou':
    #         count +=1
    # return count

    #return len([ch for ch in input if ch in 'aeiou'])
    #return len(ch for ch in input if ch in 'aeiou') # TypeError: object of type 'generator' has no len()
    return sum(1 for ch in input if ch in 'aeiou') # ?? generator()가 sum()은 있고, len()이 없나?
    # 조건이 true인 경우 1씩 더한다.

# 테스트
print(count_vowels("hello world"))  # 3



# 문제 5: 리스트 내 최댓값 반환 함수
# 리스트를 입력받아 최댓값을 반환하는 함수를 작성하세요.
def find_max(lst : list ):
    """
    리스트에서 최댓값을 반환하는 함수
    """
    #pass  # 여기에 코드를 작성하세요.
    #return max(lst)

    ### ver2
    max = -1
    for x in lst:
        if x > max:
            max = x
    return max


# 테스트
print(find_max([1, 5, 2, 9, 3]))  # 9


#문제 6: 두 문자열이 애너그램인지 확인하는 함수
#두 개의 문자열을 입력받아 애너그램인지 확인하는 함수를 작성하세요.
#애너그램(Anagram)은 같은 문자를 사용해서 순서가 다른 단어를 만들 수 있는 경우를 말합니다.
def are_anagrams(input1:str, input2: str):
    """
    두 문자열이 애너그램인지 확인하는 함수
    """
    #pass  # 여기에 코드를 작성하세요.
    #return set(input1) == set(input2) # 집합으로 해결
    return sorted(input1) == sorted(input2) # 정렬고 해결

# 테스트
print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False