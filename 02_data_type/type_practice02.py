# 1.



def test1():
    numbers = [5, 2, 9, 1, 7]
    numbers.append(3) # 3 추가
    numbers.sort() # 정렬
    numbers.pop(-1) # remove(값 at index=-1)도 됨
    #numbers.remove(max(numbers)) # pop대신
    print(numbers[:-2]) # 슬라이싱 후 출력
    #print(numbers[:3]) # 슬라이싱 앞에서 부터
    #### one-liner
    # sorted((numbers + [3])).remove(sorted((numbers + [3]))[-1])
    # numbers = [5, 2, 9, 1, 7]
    # print([:-2])
    
test1() 


def test2():
    info = ("Alice", 25, "Engineer")
    print(f"이름은 {info[0]}이고, 나이는 {info[1]}살이다.")
    
#test2() 




def test3():
    scores = {"Tom": 87, "Jane": 92, "Mike": 78}

    scores["Mike"] = 82 # Mike 점수수정
    #scores.update({"Mike" : 82}) # 있으면 업데이트
    
    scores.update({"Lucy": 95}) # 없으면 추가
    #scores.update(Lucy = 95) # 이것도 ok
    print(scores)
    
    avg = 0
    N_students = 0
    for k,v in scores.items():
        print(k, v)
        avg += v
        N_students +=1
        
    print(f"평균점수: {avg/N_students}")
    
    #### only
    avg2 = sum(scores.values()) / len(scores.values())
    #avg = sum(scores.values()) / len(scores) # 같다
    print(f"평균점수: {avg2}")
    
    
    #### one-liner by using reduce()
    from functools import reduce
    print(f"평균점수: {reduce(lambda x, y: x+y, scores.values())/len(scores)}")
    
#test3()


def test4():
    student1 = {"Python", "Math", "English"}
    student2 = {"Python", "Biology", "English"}
    print(set(student1).intersection(set(student2)))
    print(set(student1).symmetric_difference(set(student2)))
    print(set(student1).union(set(student2)))
    
#test4() 