import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

raw_data = {'first_name': ['sentimental', 'afraid', 'proud', 'faithful', 'terrified','joyful','angry','sad','jealous','grateful','prepared','embarrassed','excited','annoyed','lonely','ashamed','guilty','surprised','nostalgic','confident','furious','disappointed','caring','trusting','disgusted','anticipating','anxious','hopeful','content','impressed','apprehensive','devastated'],
        'pre_score': [37, 115, 83, 41, 81, 57, 67, 107, 69, 74, 62, 56, 103, 75, 58, 38, 75, 125, 61, 73, 66, 63, 40, 20, 46, 38, 48, 66, 16, 55, 33, 54],
        'mid_score': [5, 12, 6, 4, 3, 4, 18, 13, 13, 17, 14, 14, 13, 12, 16, 10, 5, 17, 9, 4, 12, 4, 9, 12, 12, 9, 5, 10, 8, 6, 14, 12],
        'post_score': [12, 4, 12, 4, 9, 9, 8, 8, 9, 11, 8, 9, 8, 7, 4, 5, 30, 4, 15, 5, 5, 8, 4, 4, 8, 9, 4, 12, 6, 6, 4, 6]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'pre_score', 'mid_score', 'post_score'])
# Setting the positions and width for the bars
pos = list(range(len(df['pre_score']))) 
width = 0.25 
    
# Plotting the bars
fig, ax = plt.subplots(figsize=(10,5))

# Create a bar with pre_score data,
# in position pos,
plt.bar(pos, 
        #using df['pre_score'] data,
        df['pre_score'], 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#EE3224', 
        # with label the first value in first_name
        label=df['first_name'][0]) 

# Create a bar with mid_score data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos], 
        #using df['mid_score'] data,
        df['mid_score'],
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#F78F1E', 
        # with label the second value in first_name
        label=df['first_name'][1]) 

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*2 for p in pos], 
        #using df['post_score'] data,
        df['post_score'], 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#01FF00', 
        # with label the third value in first_name
        label=df['first_name'][2]) 

# Set the y axis label
ax.set_ylabel('Số nhãn')

# Set the chart's title
ax.set_title('Thống kê')

# Set the position of the x ticks
ax.set_xticks([p + 3 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df['first_name'])

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(df['pre_score'] + df['mid_score'] + df['post_score'])] )

# Adding the legend and showing the plot
plt.legend(['Train', 'Test', 'Valid'], loc='upper left')
plt.grid()
plt.show()