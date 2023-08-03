#!/usr/bin/env python
# coding: utf-8

# In[24]:


#1.Write a Pandas program to create a dataframe from a dictionary and display it.
#Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
#Solution:-
import pandas as pd
data = {'X': [78, 85, 96, 80, 86], 'Y': [84, 94, 89, 83, 86], 'Z': [86, 97, 96, 72, 83]}
df=pd.DataFrame(data)
print(df)


# In[25]:


#Sample Python dictionary data and list labels:
#exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
#labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#Solution:-
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
      }

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
student_a_data = {
    'name': exam_data['name'][labels.index('a')],
    'attempts': exam_data['attempts'][labels.index('a')],
    'qualify': exam_data['qualify'][labels.index('a')],
      }
print(student_a_data)


# In[26]:


#3: Write a Pandas program to display a summary of the basic information about a specified DataFrame and its data.
#Sample Python dictionary data and list labels:
#exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
#labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#Solution:-
import pandas as pd
import numpy as np
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
print(df.info())


# In[27]:


#4:Write a Pandas program to get the first 3 rows of a given DataFrame.
#Sample Python dictionary data and list labels:
#exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
#labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#Solution:-
import pandas as pd
import numpy as np
exam_data = {
    'name':['Anastasia','Dima','Ketherine','James','Emily','Michael','Matthew','Laura','Kevin','Jonas'],
    'score':[12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19],
    'attempts':[1,3,2,3,2,3,1,1,2,1],
    'qualify':['yes','no','yes','no','no','yes','yes','no','no','yes']
}
labels = ['a','b','c','d','e','f','g','h','i','j']
df = pd.DataFrame(exam_data,index=labels)
first_3_row = df.head(3)
print(first_3_row)


# In[28]:


#5.Write a Pandas program to select the rows where the number of attempts in the examination is greater than 2.
#Sample Python dictionary data and list labels:
#exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
#labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#Solution:-
import pandas as pd
import numpy as np
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
first_3_rows = df.head(3)
print(first_3_rows)


# In[29]:


#6. Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).
#Sample Python dictionary data and list labels:
#exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
#'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
#'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
#'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
#labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#Expected Output:
#Solution:-
import pandas as pd
import numpy as np
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
            }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
selected_rows = df.loc[(df['score'] >= 15) & (df['score'] <= 20)]
print(selected_rows)


# In[30]:


#1. Write a Pandas program to convert all the string values to upper, lower cases in a given pandas series. Also find the length of the string values.
#Solution:-
import pandas as pd
data = pd.Series(['Hello', 'WORLD', 'Pandas', 'Python', 'Data Science'])
upper_case_series = data.str.upper()
lower_case_series = data.str.lower()
string_lengths = data.str.len()
result_df = pd.DataFrame({
    'Original': data,
    'Upper Case': upper_case_series,
    'Lower Case': lower_case_series,
    'String Length': string_lengths
})
print(result_df)


# In[31]:


#2. Write a Pandas program to remove whitespaces, left sided whitespaces and right sided whitespaces of the string values of a given pandas series.\
#Solution:-
import pandas as pd
data = pd.Series(['   apple', 'orange   ', '   banana   ', '  pineapple  '])
data_stripped = data.str.strip()
data_lstripped = data.str.lstrip()
data_rstripped = data.str.rstrip()
print("Original Series:")
print(data)
print("\nAfter removing whitespaces from both sides:")
print(data_stripped)
print("\nAfter removing left-sided whitespaces:")
print(data_lstripped)
print("\nAfter removing right-sided whitespaces:")
print(data_rstripped)


# In[32]:


#3. Write a Pandas program to add leading zeros to the integer column in a pandas series and makes the length of the field to 8 digit.
#Solution:-
import pandas as pd
data = {'IntegerColumn': [1, 22, 333, 4444, 55555]}
df = pd.DataFrame(data)
df['PaddedColumn'] = df['IntegerColumn'].astype(str).str.zfill(8)
print(df)


# In[33]:


#4. Write a Pandas program to add leading zeros to the character column in a pandas series and makes the length of the field to 8 digit.
#Solution:-
import pandas as pd
data = [10, 203, 4567, 89012, 345678]
my_series = pd.Series(data)
my_series_str = my_series.astype(str).str.zfill(8)
print(my_series_str)


# In[34]:


#5. Write a Pandas program to capitalize all the string values of specified columns of a given DataFrame.
#Solution:-
import pandas as pd
def capitalize_strings(df, columns):
    df_copy = df.copy()
    for column in columns:
        if column in df_copy:
            df_copy[column] = df_copy[column].apply(lambda x: x.capitalize() if isinstance(x, str) else x)
    return df_copy
data = {
    'Name': ['john', 'michael', 'susan'],
    'Age': [25, 30, 22],
    'City': ['Uttar Pradesh', 'los angeles', 'chicago']
}
df = pd.DataFrame(data)
columns_to_capitalize = ['Name', 'City']
result_df = capitalize_strings(df, columns_to_capitalize)
print(result_df)


# In[35]:


#6. Write a Pandas program to count of occurrence of a specified substring in a DataFrame column.
#Solution:-
import pandas as pd
data = {
    'Text_Column': ['apple is a fruit', 'banana is a fruit', 'orange is a fruit', 'grapes are fruits']
}
df = pd.DataFrame(data)
substring_to_count = 'fruit'
count_occurrences = df['Text_Column'].str.count(substring_to_count).sum()
print(f"The substring '{substring_to_count}' appears {count_occurrences} times in the DataFrame column.")


# In[ ]:




