# POS Tagger

## HMM

### hmm_english.py

The training data for English has been saved into English_data.txt after converting the tags from UD to BIS. The code trains the model on the basis of English_data.txt and then takes the test data from English_Annotations.txt and then predicts the tags and then saves them into the file English_output_hmm.txt in the format {word}\t{actual_tag}\t{predicted_tag}.

### hmm_hindi.py

The code trains the model on the basis of Hindi_data.txt and then takes the test data from Hindi_Annotations.txt and then predicts the tags and then saves them into the file Hindi_output_hmm.txt in the format {word}\t{actual_tag}\t{predicted_tag}.

## CRF

### model_english

The training data for English has been saved into English_data.txt after converting the tags from UD to BIS. The model is trained on the basis of English_data.txt  with respect to template.txt (which considers two words before and after the current word) and then it takes the test data from English_Annotations.txt and then predicts the tags and then saves them into the file English_output_crf.txt in the format {word}\t{actual_tag}\t{predicted_tag}.

### model_hindi

The model is trained on the basis of Hindi_data.txt  with respect to template.txt (which considers two words before and after the current word) and then it takes the test data from Hindi_Annotations.txt and then predicts the tags and then saves them into the file Hindi_output_crf.txt in the format {word}\t{actual_tag}\t{predicted_tag}.

## analysis.py

The code in this file calculates the Recall, Precision and F1 score and then generates the confused matrix for all of the four models and saves everything in analysis.txt .
