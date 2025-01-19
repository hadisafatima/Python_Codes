class Common_Elements :
    common_elements = []
    def common(self, list1, list2):
        for i in list1 :
            if i in list2 :
             self.common_elements.append(i)
        
        return self.common_elements

common = Common_Elements()
list1 = [1,2,3,4,5]
list2 = [1,10,90]
print(common.common(list1, list2))