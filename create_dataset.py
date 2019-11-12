
import os
from os import path
import pandas as pd

def main():
    data_root = 'data/bbc-fulltext/bbc'
    data_set = pd.DataFrame(columns = ['contents', 'category'])
            
    for dir_path, dir_names, file_names in os.walk(data_root):
        if dir_path != data_root:
            for file_name in file_names:
                category = path.split(dir_path)[1]
                file_path = path.join(dir_path,file_name)
                try:
                    with open(file_path, 'r') as file:
                        contents = file.read()
                        data_set = data_set.append({'contents':contents, 'category':category}, ignore_index=True)
                except:
                    pass
    print(data_set)
    dataset_path = 'data/dataset'
    data_set.to_csv(path.join(dataset_path,'dataset.csv'))
    
if __name__ == "__main__":
    main()

#  https://towardsdatascience.com/a-practitioners-guide-to-natural-language-processing-part-i-processing-understanding-text-9f4abfd13e72
#  https://github.com/miguelfzafra/Latest-News-Classifier/blob/master/0.%20Latest%20News%20Classifier/03.%20Feature%20Engineering/03.%20Feature%20Engineering.ipynb
#  https://towardsdatascience.com/text-classification-in-python-dd95d264c802