import pandas
import os
import seaborn

colours = {
    'Economics' : 'orange',
    'Stack Overflow' : 'blue',
    'Psychology & Neuroscience' : 'green',
}


def main():
    for file in list(os.scandir('data_bk')):
        if file.name.startswith('.'):
            continue
        df = pandas.read_csv(file.path, index_col=0).sort_values('count', ascending = False)
        numWords = len(df)
        df['cName'] = df['class'].apply(lambda x: x if x != 'Stack Overflow' else 'Computer Science')
        df['colour_class'] =df['class'].apply(lambda x : colours[x])
        df['rank'] = range(numWords)
        df['size_objs'] = df['rank'].apply(lambda x : (numWords - x) / numWords) + 1
        df['alpha_val'] = df['rank'].apply(lambda x : .8 * (numWords - x) / numWords + .2)
        df.to_csv('data/{}'.format(file.name))

if __name__ == '__main__':
    main()
