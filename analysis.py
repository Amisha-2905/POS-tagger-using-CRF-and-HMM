from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix

def generate_confusion_matrix(true_tags, predicted_tags, title):
    cm = confusion_matrix(true_tags, predicted_tags)
    matrix_str = f"{title}\n\n"
    matrix_str += "       Predicted\n"
    matrix_str += "     |  0   |  1   |\n"
    matrix_str += "True |------|------|\n"
    matrix_str += f"  0  |  {cm[0][0]:<3} |  {cm[0][1]:<3} |\n"
    matrix_str += f"  1  |  {cm[1][0]:<3} |  {cm[1][1]:<3} |\n"
    matrix_str += "\n"
    return matrix_str

first_tags = []
second_tags = []

with open("English_output_hmm.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line: 
            continue
        parts = line.split()
        if len(parts) == 3:  
            first_tags.append(parts[1])
            second_tags.append(parts[2])

precision = precision_score(first_tags, second_tags, average="weighted", zero_division=0)

print("Precision:", precision)

recall = recall_score(first_tags, second_tags, average="weighted", zero_division=0)

print("Recall:", recall)

f1 = f1_score(first_tags, second_tags, average="weighted", zero_division=0)

print("F1 Score:", f1)

confusion_matrix_text = generate_confusion_matrix(first_tags, second_tags, "Confusion Matrix - English HMM")

with open("analysis.txt", 'w') as output:
    output.write("""Analysis of Hidden Markov Model (HMM) for English POS Tagging\n\n""")
    output.write(f"Precision: {precision:.2f}\n")
    output.write(f"Recall: {recall:.2f}\n")
    output.write(f"F1 Score: {f1:.2f}\n\n")
    output.write(confusion_matrix_text)


first_tags = []
second_tags = []

with open("English_output_crf.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line: 
            continue
        parts = line.split()
        if len(parts) == 3:  
            first_tags.append(parts[1])
            second_tags.append(parts[2])

precision = precision_score(first_tags, second_tags, average="weighted", zero_division=0)

print("Precision:", precision)

recall = recall_score(first_tags, second_tags, average="weighted", zero_division=0)

print("Recall:", recall)

f1 = f1_score(first_tags, second_tags, average="weighted", zero_division=0)

print("F1 Score:", f1)

confusion_matrix_text = generate_confusion_matrix(first_tags, second_tags, "Confusion Matrix - English CRF")

with open("analysis.txt", 'a') as output:
    output.write("""Analysis of Conditional Random Field (CRF) for English POS Tagging\n\n""")
    output.write(f"Precision: {precision:.2f}\n")
    output.write(f"Recall: {recall:.2f}\n")
    output.write(f"F1 Score: {f1:.2f}\n\n")
    output.write(confusion_matrix_text)

first_tags = []
second_tags = []

with open("Hindi_output_hmm.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line: 
            continue
        parts = line.split()
        if len(parts) == 3:  
            first_tags.append(parts[1])
            second_tags.append(parts[2])

precision = precision_score(first_tags, second_tags, average="weighted", zero_division=0)

print("Precision:", precision)

recall = recall_score(first_tags, second_tags, average="weighted", zero_division=0)

print("Recall:", recall)

f1 = f1_score(first_tags, second_tags, average="weighted", zero_division=0)

print("F1 Score:", f1)

confusion_matrix_text = generate_confusion_matrix(first_tags, second_tags, "Confusion Matrix - Hindi HMM")

with open("analysis.txt", 'a') as output:
    output.write("""Analysis of Hidden Markov Model (HMM) for Hindi POS Tagging\n\n""")
    output.write(f"Precision: {precision:.2f}\n")
    output.write(f"Recall: {recall:.2f}\n")
    output.write(f"F1 Score: {f1:.2f}\n\n")
    output.write(confusion_matrix_text)

first_tags = []
second_tags = []

with open("Hindi_output_crf.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line: 
            continue
        parts = line.split()
        if len(parts) == 3:  
            first_tags.append(parts[1])
            second_tags.append(parts[2])

precision = precision_score(first_tags, second_tags, average="weighted", zero_division=0)

print("Precision:", precision)

recall = recall_score(first_tags, second_tags, average="weighted", zero_division=0)

print("Recall:", recall)

f1 = f1_score(first_tags, second_tags, average="weighted", zero_division=0)

print("F1 Score:", f1)

confusion_matrix_text = generate_confusion_matrix(first_tags, second_tags, "Confusion Matrix - Hindi CRF")

with open("analysis.txt", 'a') as output:
    output.write("""Analysis of Conditional Random Field (CRF) for Hindi POS Tagging\n\n""")
    output.write(f"Precision: {precision:.2f}\n")
    output.write(f"Recall: {recall:.2f}\n")
    output.write(f"F1 Score: {f1:.2f}\n\n")
    output.write(confusion_matrix_text)