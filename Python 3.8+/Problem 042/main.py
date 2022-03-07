def increase_triangle_numbers(current_state: list,upper_bound: int) -> list:
    while max(current_state) < upper_bound:
        nextNumber = int(0.5 * (len(current_state)+1) * (len(current_state)+2))
        current_state.append(nextNumber)
    return(current_state)

def word_score(word: str, scores: dict) -> int:
    score = 0
    for char in word.lower():
        score += scores[char]
    return(score)

def main():
    characters = "abcdefghijklmnopqrstuvwxyz"
    scores = {char:characters.index(char)+1 for char in characters}
    triangle_numbers = [1,3,6]
    with open("words.txt","r") as f:
        words = f.readline()
        words = words.split(",")
        words = [i.replace('"','') for i in words]
    count = 0
    for word in words:
        score = word_score(word,scores)
        #print(f"{word}\t\tscored as {score}")
        if score > max(triangle_numbers):
            triangle_numbers = increase_triangle_numbers(triangle_numbers,score)
        if score in triangle_numbers:
            count += 1
            #print("And is a triangle number")
        else:
            pass
            #print("And is NOT a triangle number")
    return(count)

if __name__=="__main__":
    print(main())