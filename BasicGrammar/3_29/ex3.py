"""
����ͳ�Ƹ����������ı���text.txt��������ǰ10�Ĺؼ��ʲ���Ƶ�ʽ�����ʾ��
please fill in the code.
"""
import jieba

def main():
    txt = open("text.txt", "r", errors='ignore', encoding="utf-8").read()
    # +++your code here+++
    word_list = jieba.cut(txt, cut_all=True)
    d = {}
    for word in word_list:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    items = sorted(d.items(), key=lambda x: x[0])
    for i in range(10):
        word, count = items[i][0], items[i][1]
        print ("{0}:{1}".format(word, count))


if __name__ == '__main__':
    main()
