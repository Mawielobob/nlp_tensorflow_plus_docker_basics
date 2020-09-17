import re
import tensorflow as tf
import matplotlib.pyplot as plt
from collections import Counter
from tensorflow.keras.preprocessing.sequence import pad_sequences


def clean_single_comment(comment):
    
    # remove '\n' & replace '\\n' with space
    comment = comment.replace('\n', '').replace('\\n', ' ')
    
    # lowercase
    comment = comment.lower()
    
    # remove all user names which are started with @ and ended by space
    matches = re.findall(r'(\@.*?\ )', comment, flags=re.IGNORECASE)
    for match in set(matches):
        comment = comment.replace(match, '')
        
    # place for other preprocess
    
    return comment
    
def plot_from_counter(data_list, plot_title, print_values=False):
    c = Counter(data_list)
    plt.bar(c.keys(), c.values());
    plt.title(plot_title)
    plt.show()
    
    if print_values:
        print(dict(c))
        
def prepare_trainig_data(sentences, max_length, trunc_type, tokenizer):
    # tokenize train data
    sequences = tokenizer.texts_to_sequences(sentences)

    # lengthening of short sentences to max_length
    padded = pad_sequences(sequences, maxlen=max_length, truncating=trunc_type)
    
    return padded
    
def predict_padded(model, test_padded):
    
    y_pred = model.predict(test_padded)
    prediction=tf.argmax(y_pred,1)
    
    return prediction
    

