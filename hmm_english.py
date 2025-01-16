def calculate_emission_probs(data_set):
    emission_counts = {}

    for sentence in data_set:
        for word, tag in sentence:
            if tag not in emission_counts:
                emission_counts[tag] = {}
            if word not in emission_counts[tag]:
                emission_counts[tag][word] = 0
            emission_counts[tag][word] += 1

    emission_probs = {k: {k1: v1 / sum(v.values()) for k1, v1 in v.items()} for k, v in emission_counts.items()}
    return emission_probs

def calculate_transition_probs(data_set):
    transition_counts = {'<S>': {}, '<E>': {}}

    for sentence in data_set:
        if len(sentence) > 0:
            first_tag = sentence[0][1]
            if first_tag not in transition_counts['<S>']:
                transition_counts['<S>'][first_tag] = 0
            transition_counts['<S>'][first_tag] += 1
            
            last_tag = sentence[-1][1]
            if last_tag not in transition_counts:
                transition_counts[last_tag] = {}
            if '<E>' not in transition_counts[last_tag]:
                transition_counts[last_tag]['<E>'] = 0
            transition_counts[last_tag]['<E>'] += 1
            
            for i in range(len(sentence) - 1):
                current_tag = sentence[i][1]
                next_tag = sentence[i + 1][1]
                if current_tag != '<S>':  # Exclude <S> from regular tag transitions
                    if current_tag not in transition_counts:
                        transition_counts[current_tag] = {}
                    if next_tag not in transition_counts[current_tag]:
                        transition_counts[current_tag][next_tag] = 0
                    transition_counts[current_tag][next_tag] += 1

    transition_probs = {k: {k1: v1 / sum(v.values()) for k1, v1 in v.items()} for k, v in transition_counts.items()}
    return transition_probs

           
def viterbi(words, transition_probs, emission_probs):
    state_sequence = []
    T = [tag for tag in transition_probs.keys() if tag not in ['<S>', '<E>']]

    for key, word in enumerate(words):
        probabilities = []
        for tag in T:
            if key == 0:
                transition_prob = transition_probs['<S>'].get(tag, 0)
            else:
                transition_prob = transition_probs[state_sequence[-1]].get(tag, 0)

            emission_prob = emission_probs.get(tag, {}).get(word, 0)

            state_probability = emission_prob * transition_prob
            probabilities.append(state_probability)

        max_probability = max(probabilities)
        max_state = T[probabilities.index(max_probability)]
        state_sequence.append(max_state)

    return list(zip(words, state_sequence))


with open('English_data.txt', 'r') as input_file:
    data = input_file.read()
    data = data.split('\n')

data_set = []
sentence = []

for lines in data:
    if lines == "":
        data_set.append(sentence)
        sentence = []
    else:
        word_tag = lines.split("\t") 
        sentence.append(word_tag)

# print(data_set)

emission_probs = calculate_emission_probs(data_set)
# print ("Emission :",emission_probs)
transition_probs = calculate_transition_probs(data_set)
# print ("Transition:",transition_probs)

with open('English_Annotations.txt', 'r') as file:
    data = file.read()
    data = data.split('\n')

test_data = []
actual_tags = []
test_sentences = []
test_tags = []
for lines in data:
    if lines == "":
        test_data.append(test_sentences)
        actual_tags.append(test_tags)
        test_tags = []
        test_sentences = []
    else:
        # print(lines)
        word, tag = lines.split("\t")
        test_sentences.append(word)
        test_tags.append(tag)

# print(actual_tags)

with open('English_output_hmm.txt', 'w') as output_file:
    sentence = 0
    for test_sentence in test_data:
        predicted_tags = viterbi(test_sentence, transition_probs, emission_probs)
        for idx, (word, predicted_tag) in enumerate(predicted_tags):
            # output_file.write(f"{idx}\t{word}\t{predicted_tag}\n")
            actual_tag = actual_tags[sentence][idx]
            output_file.write(f"{word}\t{actual_tag}\t{predicted_tag}\n")
        output_file.write("\n")
        sentence = sentence + 1

