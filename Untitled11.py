#!/usr/bin/env python
# coding: utf-8

# In[14]:


1.	Given a 2D list (matrix), write Python code that prints its transpose and upload the code to GIT repository.  
Example:
Input:
[[1, 2], [3, 4], [5, 6]]
Output:
[[1, 3, 5], [2, 4, 6]]




def transpose_matrix(matrix):
    # Using zip to transpose the matrix
    transposed = [list(row) for row in zip(*matrix)]
    return transposed

matrix = [[1, 2], [3, 4], [5, 6]]
result = transpose_matrix(matrix)

print("Original Matrix:", matrix)
print("Transposed Matrix:", result)


# In[2]:


text = "Hello world python"
words = text.split()

reversed_words = []
for w in words:
    reversed_words.insert(0,w)
    
result = " ".join(reversed_words)
print(result)
    





# In[ ]:




