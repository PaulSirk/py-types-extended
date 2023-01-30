from collections import deque

# Library that immediately inserts elements into a list in
# ascending order
class BinaryList:
    # datatypes include: int, str, float, etc. Do not enter in string format.
    # ex: enter int instead of 'int' or "int"
    def __init__(self, dataType):
        self.dataType = dataType
        self.BinaryList = deque()

    # Checks that Element is same datatype
    def __checkElement(self, element):
        elementType : type = type(element)
        if elementType != self.dataType:
            error_message = f"'element' is {elementType}, not {self.dataType}."
            raise ValueError(error_message)

    # returns list
    def getList(self):
        return self.BinaryList

    # insertsElement into list
    def insertElement(self, new_element):
        self.__checkElement(new_element)

        # automatically adds to list
        if not bool(self.BinaryList):
            self.BinaryList.append(new_element)
        # adds to beginning of list if element is smaller
        # or equal to the smallest element's value
        elif new_element <= self.BinaryList[0]:
            self.BinaryList.appendleft(new_element)
        else:
            listLength = len(self.BinaryList)

            # inserts element to end of list if element is greater than
            # or equal to the greatest element's value
            if new_element >= self.BinaryList[listLength-1]:
                self.BinaryList.append(new_element)
            
            # adds to beginning or end of list in O(1) time
            elif listLength == 1:

                if new_element <= self.BinaryList[0]:
                    self.BinaryList.appendleft(new_element)
                else:
                    self.BinaryList.append(new_element)
            
            # performs a binary search to
            # insert the element into the list
            else:
                middle : int = listLength // 2
                if new_element <= self.BinaryList[middle]:
                    for i in range(middle, -1, -1):
                        if new_element >= self.BinaryList[i]:
                            self.BinaryList.insert(i+1, new_element)
                            break
                else:
                    for j in range(middle, listLength):
                        if new_element >= self.BinaryList[j]:
                            self.BinaryList.insert(j+1, new_element)
                            break

        return

    # searches for first sighting of element in list
    def search(self, element) -> int:
        self.__checkElement(element)
        listLength : int = len(self.BinaryList)
        middleIndex : int = listLength // 2

        found_index : int = 0

        if element <= self.BinaryList[middleIndex]:
            for i in range(0, middleIndex):
                if element == self.BinaryList[i]:
                    found_index = i
                    break
        else:
            for j in range(middleIndex, listLength):
                if element == self.BinaryList[j]:
                    found_index = i
                    break

        return found_index

    # returns the range that you can find a number in a list
    # returns tuple containing first index and last index that
    # number can be found at
    def searchAll(self, element) -> tuple:
        self.__checkElement(element)
        starting_index = self.BinaryList.index(element)
        for b in range(starting_index, len(self.BinaryList)):
            if self.BinaryList[b] != element:
                return (starting_index, b-1)

        return
    