'''Starter code by Michael Geurzhoy'''
import math

def norm(vec):
    '''Return the norm of a vector stored as a dictionary'''

    sum_of_squares = 0.0
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    dot = []
    B = []
    dotproduct = 0
    lenvec1 = 0
    lenvec2 = 0

    for i in vec1:
        if i in vec2:
            A = [vec1[i], vec2[i]]
            dot.append(A)
    for j in range(0, len(dot)):
        multdot = dot[j][0]*dot[j][1]
        B.append(multdot)

    for k in B:
        dotproduct += k

    denom = norm(vec1) * norm(vec2)
    cos = dotproduct / denom
    return cos


def build_semantic_descriptors(sentences):
    sent2 = []
    for i in sentences:
        sent2.extend(i)
    S = set(sent2)
    S = list(S)
    dict = {}
    for m in S:
        dict[m] = {}
    for k in range(0, len(sentences)):
        Sk = list(set(sentences[k]))
        for i in range(0, len(Sk)):
            So =[]
            So.extend(Sk[0:i])
            So.extend(Sk[i+1:])
            for o in So:
                if o in dict[Sk[i]]:
                    dict[Sk[i]][o] += 1
                else:
                    dict[Sk[i]][o] = 1
    return dict

def build_semantic_descriptors_from_files(filenames):
    text = ""
    text2 = []
    for i in range(0, len(filenames)):
        f = open(filenames[i], "r", encoding="latin1")
        text += ".\n" + f.read()
    text = text.lower()
    text = text.replace(",", "")
    text = text.replace("-", " ")
    text = text.replace("--", " ")
    text = text.replace(":", "")
    text = text.replace(";", "")
    text = text.replace("?", ".")
    text = text.replace("!", ".")
    text = text.split(".")
    for i in range(0, len(text)):
        text2.append(text[i].split())
    while [] in text2:
        text2.remove([])
    return build_semantic_descriptors(text2)



def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    L =[]
    if word not in semantic_descriptors:
        return choices[0]
    vec1 = semantic_descriptors[word]
    for i in range(0, len(choices)):
        if choices[i] in semantic_descriptors:
            vec2 = semantic_descriptors[choices[i]]
            sim = [similarity_fn(vec1, vec2)]
        else:
            sim = [-1]
        L.extend(sim)
    ind = L.index(max(L))
    answer = choices[ind]
    return answer


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    f  = open(filename)
    text = f.read()
    t = text.splitlines()
    correct = 0
    for i in range(0, len(t)):
        ti = t[i]
        ti = ti.split()
        if ti[1] == most_similar_word(ti[0], ti[2:], semantic_descriptors, similarity_fn):
            correct += 1
    return (correct / len(t))*100

