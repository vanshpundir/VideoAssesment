
import random
import spacy


nlp = spacy.blank('en')
def train_model(train_data):
    if 'ner' not in nlp.pipe_names:  # Checking if NER is present in pipeline
        nlp.add_pipe("ner", last=True)  # adding NER pipe in the end

    for _, annotation in train_data:  # Getting 1 resume at a time from our training data of 200 resumes
        for ent in annotation[
            'entities']:  # Getting each tuple at a time from 'entities' key in dictionary at index[1] i.e.,(0, 15, 'Name') and so on
            nlp.add_label(ent[
                              2])  # here we are adding only labels of each tuple from entities key dict, eg:- 'Name' label of (0, 15, 'Name')

    # In above for loop we finally added all custom NER from training data.

    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']  # getting all other pipes except NER.
    with nlp.disable_pipes(*other_pipes):  # Disabling other pipe's as we want to train only NER.
        optimizer = nlp.begin_training()

        for itn in range(10):  # trainig model for 10 iteraion
            print('Starting iteration ' + str(itn))
            random.shuffle(train_data)  # shuffling data in every iteration
            losses = {}
            for text, annotations in train_data:
                try:
                    nlp.update(
                        [text],  # batch of texts
                        [annotations],  # batch of annotations
                        drop=0.2,  # dropout rate -makes it harder to memorise
                        sgd=optimizer,  # callable to update weights
                        losses=losses)  # Dictionary to update with the loss, keyed by pipeline component.
                except Exception as e:
                    pass
train_model(r"C:\Users\jogin\Downloads\annotations1.json")