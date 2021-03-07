import sys
import math
import random
import argparse
class Circle:
    def create_next_circle(self, x, y, r, counter):
        self.x = x
        self.y = y
        self.r = r
        self.counter = counter
        self.prev = counter + 1
        self.next = counter - 1
        self.status = True
    def find_next(head_next,head_status,head_num,c1,counter):
        for i in range(0, len(head_num)):
            check = 0
            if head_status[i] == True:
                for j in range(head_num[i] - 1,-1, -1):
                    if head_status[j] == True:
                        head_next[i] = j
                        check = 1
                        break
                if check != 1:
                    for j in range(len(head_num) - 1, i, -1):
                        if head_status[j] == True:
                            head_next[i] = j
                            check = 1
                            break
        return head_next

    def find_prev(head_prev, head_status, head_num,counter):
        for i in range(0, len(head_num)):
            check = 0
            if head_status[i] == True:
                for j in range(i + 1, len(head_num)):
                    if head_status[j] == True:
                        head_prev[i] = j
                        check = 1
                        break
                if check != 1:
                    for j in range(0 ,i - 1, 1):
                        if head_status[j] == True:
                            head_prev[i] = j
                            check = 1
                            break
        head_prev[c2] = counter
        return head_prev
    def find_c1(head_num,head_x,head_y,head_status):
        min_dist = sys.maxsize
        for i in head_num:
            dist = round(math.sqrt((head_x[i] - 0) ** 2 + (head_y[i] - 0) ** 2),2)
            if (dist < min_dist and head_status[i]):
                min_dist = dist
                min_pos = i
        if min_dist == sys.maxsize:
            return -1
        return min_pos
    def find_c2(head_next,c1):
        return head_next[c1]
    def find_tangent_circle(head_x , head_y, head_r, c1, c2, r):
        dx = head_x[c2] - head_x[c1]
        dy = head_y[c2] - head_y[c1]
        dist = round(math.sqrt(dx ** 2 + dy ** 2),2)
        r1 = head_r[c1] + r
        r2 = head_r[c2] + r
        l = ((r1) ** 2 - (r2) ** 2 + dist ** 2) / (2 * dist ** 2)
        if (r1 ** 2) / (dist ** 2) - (l ** 2) <= 0:
            new_x=-1
            new_y=-1
            new_r=-1
            return new_x,new_y,new_r
        e = math.sqrt((r1 ** 2) / (dist ** 2) - (l ** 2))
        new_x = round(head_x[c1] + l * dx - e * dy,2)
        new_y = round(head_y[c1] + l * dy + e * dx,2)
        new_r = r
        return new_x,new_y,new_r
    def intersecting_circles(head_x,head_y,head_r,r,counter):
        intersected = []
        for i in head_num:
            dist = round(math.sqrt((new_x - head_x[i])**2 + ((new_y - head_y[i])**2)),2)
            if dist - head_r[i] - r < -1 and head_status[i]==True:
                intersected.append(i)
        return intersected
    def intersecting_circle(intersected):
        res=sys.maxsize
        for i in range(0,len(intersected)):
            if intersected[i] < res:
                res=intersected[i]
                pos=i
        intersected.pop(pos)
        return res
    def find_rule(intersected,c1,c2,head_next,head_prev):
        rule1=False
        rule2=False
        index1 = head_prev[c1]
        index2 = head_next[c2]
        counter = 1
        while counter <= len(head_prev)/2:
            for i in intersected:
                if index2 == i:
                    rule2 = True
                    res = i
                    counter = len(head_prev) / 2 + 1
                    break
            for i in intersected:
                if  index1 == i:
                    if rule2 == True:
                        rule2=False
                    rule1=True
                    res=i
                    counter = len(head_prev) / 2 + 1
                    break

            index1=head_prev[index1]
            index2=head_next[index2]
            counter = counter + 1
        return rule1,rule2,res
    def adjust(head_next,head_prev,index):
        head_next[index-1]=head_next[index]
        return head_next
    def move1(head_next,head_num,head_status,head_prev,res):
        index = head_next[res]
        while index != head_num[c2]:
            head_status[index] = False
            head_next[head_prev[index]]=head_next[index]
            head_prev[head_next[index]]=head_prev[index]
            index = head_next[index]
        return head_status

    def move2(head_next,head_num,head_status,head_prev,res):
        index = head_next[c1]
        while index != head_num[res]:
            head_status[index] = False
            head_next[head_prev[index]]=head_next[index]
            head_prev[head_next[index]]=head_prev[index]
            index = head_next[index]
        return head_status
    def order_segments(limits):
        for i in range(0,len(limits)-1):
            if limits[i][0]>limits[i][2]:
                limits[i][0],limits[i][2]=limits[i][2],limits[i][0]
            if limits[i][1]>limits[i][3]:
                limits[i][1],limits[i][3]=limits[i][3],limits[i][1]
        return limits
    def intersect_limits(limits, r):
        for i in range(0, len(limits)-1):
            l2 = (limits[i][0] - limits[i][2]) ** 2 + (limits[i][1] - limits[i][3]) ** 2
            if l2 == 0:
                d1 = math.sqrt((limits[i][0] - new_x) ** 2 + (limits[i][1] - new_y) ** 2)
            else:
                t = (((new_x) - (limits[i][0])) * (limits[i][2] - limits[i][0]) + ((new_y) - (limits[i][1])) * (limits[i][3] - limits[i][1])) / l2
                t=min(1,t)
                t = max(0, min(1, t))
                px = limits[i][0] + t * (limits[i][2] - limits[i][0])
                py = limits[i][1] + t * (limits[i][3] - limits[i][1])
                d1 = math.sqrt((abs(px)-abs(new_x))**2+(abs(py)-abs(new_y))**2)
            if d1 <= r:
                return True
        return False

    def existing_circles(head_x, head_y, head_r, r, counter):
        for i in head_num:
            dist = round(math.sqrt((new_x - head_x[i]) ** 2 + ((new_y - head_y[i]) ** 2)), 2)
            if dist - head_r[i] - r < -1:
                return True
        return False
    def add_head(head_x,head_y,head_r,head_num,head_next,head_prev,head_status,c,c1,c2):
        head_x[counter] = round(c.x,2)
        head_y[counter] = round(c.y,2)
        head_r[counter] = round(c.r,2)
        head_num[counter] = c.counter
        head_next[counter] = c2
        head_prev[counter] = c1
        head_status[counter] = True
        return head_x, head_y, head_r,head_num, head_prev, head_status
head_x = {}
head_y = {}
head_r = {}
head_num = {}
head_next = {}
head_prev = {}
head_status = {}
limits=[]
total = sys.maxsize
min_r = -1
max_r = -1
calc = 1
while calc <= len(sys.argv)-1:
    param = sys.argv[calc]
    if param == '-i':
        param2 = float(sys.argv[calc+1])
        total = param2
    elif param =='-r':
        param2 = float(sys.argv[calc+1])
        r = param2
    elif param == '-min_radius':
        param2 = sys.argv[calc + 1]
        min_r = int(param2)
    elif param == '-max_radius':
        param2 = sys.argv[calc + 1]
        max_r = int(param2)
    elif param == '-b':
        param2 = sys.argv[calc+1]
        with open(sys.argv[calc+1]) as boundary:
            for k in boundary:
                limits_side=[]
                for l in k.split():
                    limits_side.append(float(l))
                limits.append(limits_side)
    elif param == '-seed':
        param2 = sys.argv[calc + 1]
        gen = int(param2)
        random.seed(gen)
    else:
        f = open(param, "w")
    calc = calc + 1
limits=Circle.order_segments(limits)
counter = 0
c = Circle()
if (min_r != -1 and max_r != -1):
    r1 = random.randint(min_r,max_r)
else:
    r1 = r
c.create_next_circle(0,0,r1,counter)
c1 = 0
c2 = 1
Circle.add_head(head_x,head_y,head_r,head_num,head_next,head_prev,head_status,c,c1,c2)
counter = counter + 1
if (min_r != -1 and max_r != -1):
    r2 = random.randint(min_r,max_r)
else:
    r2 = r
c.create_next_circle(0+r1+r2,0,r2,counter)
Circle.add_head(head_x,head_y,head_r,head_num,head_next,head_prev,head_status,c,c1,c2)
head_next[0] = 1
head_prev[0] = 1
head_next[1] = 0
head_prev[1] = 0
print(limits)
for i in limits:
    for j in i:
        f.write(str(j) + ' ')
    f.write('\n')
counter = counter + 1
if (min_r != -1 and max_r != -1) :
    r = random.randint(min_r,max_r)
while counter <= total:
    if c1 == c2:
        break
    new_x, new_y, new_r = Circle.find_tangent_circle(head_x, head_y, head_r, c1, c2, r)
    intersected = Circle.intersecting_circles(head_x, head_y, head_r, r, counter)
    if new_x == -1 and new_y == -1 and new_r == -1:
        head_status[c1] = False
        head_next[head_prev[c1]] = head_next[c1]
        head_prev[head_next[c1]] = head_prev[c1]
        c1 = Circle.find_c1(head_num, head_x, head_y, head_status)
        if c1 == -1:
            break
        c2 = Circle.find_c2(head_next, c1)
    elif len(intersected) != 0:
        rule1,rule2,res = Circle.find_rule(intersected,c1,c2,head_next,head_prev)
        if rule1 == True:
            head_status = Circle.move1(head_next,head_num,head_status,head_prev,res)
            c1 = res
            c2 = Circle.find_c2(head_next, c1)
        elif rule2 == True:
            head_status = Circle.move2(head_next, head_num, head_status, head_prev, res)
            c2 = res
    elif Circle.intersect_limits(limits, r):
        head_status[c1]=False
        c1 = Circle.find_c1(head_num, head_x, head_y, head_status)
        if c1 == -1:
            break
        c2 = Circle.find_c2(head_next, c1)
    elif Circle.existing_circles(head_x, head_y, head_r, r, counter):
        head_status[c1] = False
        c1 = Circle.find_c1(head_num, head_x, head_y, head_status)
        if c1 == -1:
            break
        c2 = Circle.find_c2(head_next, c1)
    else:
        c.create_next_circle(new_x, new_y, new_r, counter)
        Circle.add_head(head_x, head_y, head_r, head_num, head_next, head_prev, head_status, c, c1, c2)
        head_prev[counter] = c1
        head_prev[c2]=counter
        head_next[c1]=counter
        head_next[counter]=c2
        c1=Circle.find_c1(head_num,head_x,head_y,head_status)
        if c1 == -1:
            break
        c2 = Circle.find_c2(head_next, c1)
        counter = counter + 1
        if (min_r != -1 and max_r != -1) :
            r = random.randint(min_r, max_r)

print(counter)
for i in range(0,len(head_x)-1):
    f.write(str(head_x[i])+' ')
    f.write(str(head_y[i])+' ')
    f.write(str(head_r[i])+' ')
    f.write("\n")
