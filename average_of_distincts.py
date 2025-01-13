# This program ignores the first occurence of smallest and largest elements of a list and returns the average 
# of all the other elements.

class Average :

    def avg(mylist):
        sm = min(mylist)
        lg = max(mylist)
        
        # Create a new list excluding the first occurrences of sm and lg
        filtered_list = mylist.copy()
        if sm in filtered_list:
            filtered_list.remove(sm)  # Remove first occurrence of sm
        if lg in filtered_list:
            filtered_list.remove(lg)  # Remove first occurrence of lg
        
        # Calculate the average
        if filtered_list:
            return sum(filtered_list) // len(filtered_list)
        else:
            return 0