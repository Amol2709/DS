class TrieNode:
    def __init__(self):
        self.arr=[None]*26
        self.isEnd=False
        self.count=[0]*26
class Trie:

    def __init__(self):
       self.obj=TrieNode()
        
        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        word = word.lower()
        temp_arr=self.obj.arr
        count_arr = self.obj.count
        for i in word:
            if temp_arr[abs(97-ord(i))] == None:
                count_arr[abs(97-ord(i))]=count_arr[abs(97-ord(i))]+1
                print(count_arr[abs(97-ord(i))],ord(i),i)
                #print(count_arr[97-ord(i)])
                obj=TrieNode()
                temp_arr[abs(97-ord(i))]=obj
                count_arr = temp_arr[abs(97-ord(i))].count
                temp_arr=temp_arr[abs(97-ord(i))].arr
                
            else:
                obj=temp_arr[abs(97-ord(i))]
                temp_arr=obj.arr
                count_arr[abs(97-ord(i))]=count_arr[abs(97-ord(i))]+1
                print(count_arr[abs(97-ord(i))])
                count_arr = obj.count
                
        obj.isEnd=True

        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        word = word.lower()
        temp_arr=self.obj.arr
        for i in word:
            if temp_arr[97-ord(i)] == None:
                return False
            else:
                #print(i)
                obj= obj=temp_arr[97-ord(i)]
                temp_arr=obj.arr

        if obj.isEnd==True:
            return True
        else:
            return False
    def countWord(self,word):
        word = word.lower()
        temp_arr=self.obj.arr
        count_arr = self.obj.count
        temp_count = 0
        for i in word:
            if temp_arr[abs(97-ord(i))] == None:
                print(count_arr)
                print(i,ord(i))
                print(abs(97-ord(i)),i)
                return -1
            else:
                print('a')
                obj= obj=temp_arr[abs(97-ord(i))]
                temp_arr=obj.arr
                temp_count= temp_count+count_arr[abs(97-ord(i))]
                count_arr = obj.count
        #print(temp_count)
        return temp_count/len(word)
    def countPrefix(self,word):
        word = word.lower()
        temp_arr=self.obj.arr
        count_arr = self.obj.count
        temp_count = 0
        for i in word:
            if temp_arr[97-ord(i)] == None:
                return -1
            else:
                #print(i)
                obj= obj=temp_arr[97-ord(i)]
                temp_arr=obj.arr
                temp_count= temp_count+count_arr[97-ord(i)]
                count_arr = obj.count
        #print(temp_count)
        return temp_count/len(word)



        

    def startsWith(self, prefix):
        word = prefix.lower()
        temp_arr=self.obj.arr
        for i in word:
            if temp_arr[97-ord(i)] == None:
                return False
            else:
                #print(i)
                obj= obj=temp_arr[97-ord(i)]
                temp_arr=obj.arr
        return True

        # if obj.isEnd==True:
        #     return True
        # else:
        #     return False


obj = Trie()
word='apple'
obj.insert(word)
# word='app'
# obj.insert(word)
# word='p'
# obj.insert(word)
print(obj.countWord('e'))
# param_2 = obj.search(word)
# prefix='adp'
# print(obj.startsWith(prefix))