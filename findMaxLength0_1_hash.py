class Solution:
    def findMaxLength(self, arr): 
        n = len(arr) 
        # NOTE: Dictonary in python in  
        # implemented as Hash Maps.  
        # Create an empty hash map (dictionary)  
        hash_map = {}   
        curr_sum = 0 
        max_len = 0 
      
        for i in range (0, n):  
            if(arr[i] == 0):  
                arr[i] = -1 
            else:  
                arr[i] = 1 
      
        # Traverse through the given array  
        for i in range (0, n):  
          
            # Add current element to sum  
            curr_sum = curr_sum + arr[i]  
      
            # To handle sum=0 at last index  
            if (curr_sum == 0):  
                max_len = i + 1 
      
            # If this sum is seen before,  
            if curr_sum in hash_map: 
                  
                # If max_len is smaller than new subarray 
                # Update max_len and ending_index 
                if max_len < i - hash_map[curr_sum]: 
                    max_len = i - hash_map[curr_sum] 
            else:  
      
                # else put this sum in dictionary  
                hash_map[curr_sum] = i   
              
        for i in range (0, n):  
            if(arr[i] == -1):  
                arr[i] = 0 
            else:  
                arr[i] = 1 
              
        return max_len 