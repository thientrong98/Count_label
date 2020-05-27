import numpy as np
import matplotlib.pyplot as plt

N = 32
ind = np.arange(N)  # the x locations for the groups
width = 0.27       # the width of the bars

fig = plt.figure()
ax = fig.add_subplot(111)

yvals = [37, 115, 83, 41, 81, 57, 67, 107, 69, 74, 62, 56, 103, 75, 58, 38, 75, 125, 61, 73, 66, 63, 40, 20, 46, 38, 48, 66, 16, 55, 33, 54]
rects1 = ax.bar(ind, yvals, width, color='r')
zvals = [5, 12, 6, 4, 3, 4, 18, 13, 13, 17, 14, 14, 13, 12, 16, 10, 5, 17, 9, 4, 12, 4, 9, 12, 12, 9, 5, 10, 8, 6, 14, 12]
rects2 = ax.bar(ind+width, zvals, width, color='g')
kvals = [12, 4, 12, 4, 9, 9, 8, 8, 9, 11, 8, 9, 8, 7, 4, 5, 30, 4, 15, 5, 5, 8, 4, 4, 8, 9, 4, 12, 6, 6, 4, 6]
rects3 = ax.bar(ind+width*2, kvals, width, color='b')

ax.set_ylabel('Scores')
ax.set_xticks(ind+ width)
ax.set_xticklabels( ('sentimental', 'afraid', 'proud', 'faithful', 'terrified','joyful','angry','sad','jealous','grateful','prepared','embarrassed','excited','annoyed','lonely','ashamed','guilty','surprised','nostalgic','confident','furious','disappointed','caring','trusting','disgusted','anticipating','anxious','hopeful','content','impressed','apprehensive','devastated') )
ax.legend( (rects1[0], rects2[0], rects3[0]), ('y', 'z', 'k') )

def autolabel(rects):
    for rect in rects:
        h = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*h, '%d'%int(h),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.xticks(rotation=45, ha='right')
plt.show()