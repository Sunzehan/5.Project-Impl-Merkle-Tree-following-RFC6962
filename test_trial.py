#下面我们开始对Merkel Tree进行测试

DATA = ["123","456","789","135","246"]
Tree_1 = Tree_Generate(DATA)
print("生成了一个有DATA数集构成的MerkleTree：")
print(Tree_1)


#再生成一个有100k个叶子节点的Merkel Tree
TestMessages = crawler()
Tree_2 = Tree_Generate(TestMessages)
print("生成一个由爬取的100k数据作为的叶子节点的Merkel Tree：")
print(Tree_2)


#3.证明对指定元素包含于Merkel Tree
n=random.randint(0,100000-1)
#我们从爬取的100k数据任选一个数据作为指定元素

Evidence = ShowEvidence(TestMessages[n],Tree_2)
print("指定元素n包含于Merkel Tree的证据：")

print(Evidence)


#4.验证证明的正确性！
print("验证证明正确性的依据：：")

print(Verify(TestMessages[n],Evidence,Tree_2[-1][0]))

#对project中的实现要求，测试完成。
