punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(str):
    for i in punctuation_chars:
        if i in str:
            x = str.replace(i, "")
            str = x
    return str


def get_pos(stri):
    stri = strip_punctuation(stri)
    pos_count = 0
    for word in stri.split():
        w = word.lower()
        if w in positive_words:
            pos_count += 1
    return pos_count


def get_neg(stri):
    stri = strip_punctuation(stri)
    neg_count = 0
    for word in stri.split():
        w = word.lower()
        if w in negative_words:
            neg_count += 1
    return neg_count


# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
final = []
with open("project_twitter_data.csv") as tdata:
    for line in tdata:
        x = line.strip().split(',')
        final.append((x))
num_retweets = []
num_replies = []
pos = []
neg = []
net_score = []
for val in final[1:]:
    y = strip_punctuation(val[0])
    num_retweets.append(val[1])
    num_replies.append(val[2])
    plus = int(get_pos(y))
    minus = int(get_neg(y))
    pos.append(plus)
    neg.append(minus)
    if plus > minus:
        net_score.append(plus - minus)
    elif minus > plus:
        net_score.append(plus - minus)
    else:
        net_score.append(0)
# print(num_retweets,"\n",num_replies,"\n",pos,"\n",neg,"\n",net_score,"\n", )
finale = []
for i in range(len(pos)):
    finale.append((num_retweets[i], num_replies[i], pos[i], neg[i], net_score[i]))

outfile = open("resulting_data.csv", "w")
outfile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
outfile.write("\n")
for i in finale:
    rows = '{}, {}, {}, {}, {}'.format(i[0], i[1], i[2], i[3], i[4])
    outfile.write(rows)
    outfile.write("\n")


