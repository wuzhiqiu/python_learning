score_card={'Tom':90,'Jimmy':85,'Kim':40,'Willim':99,'Tommy':61}
passed=[name for name , score in score_card.items() if score>=60] #items 将 name,score两两配对作为元组输出
print(passed)
