class BackSpaceCompare(object):
    def back_space_compare(self, s:str, t:str) -> bool:
        '''
          Given two strings s and t, return true if they are equal 
          when both are typed into empty text editors. '#' means a
          backspace character.
        
        '''
        upper = 0
        lower = 0
        s_lst = list(s.strip(""))
        t_lst = list(t.strip(""))
        orig_length = len(s_lst)
        length = len(s_lst)
        while upper < orig_length:
            if s_lst[upper] == '#':
                if lower != 0:
                    lower -= 1
                    length -= 2   # in this  case, remove both # and previous number 
                else:
                    length -= 1   # in this case, remove just #

            elif s_lst[upper] != '#':
                if upper != lower:
                    s_lst[lower] = s_lst[upper]
                lower += 1
                
            upper += 1
        
        s_lst[:] = s_lst[:length]
        
        upper = 0
        lower = 0
        length = len(t_lst)
        orig_length = len(t_lst)
        while upper < orig_length:
            if t_lst[upper] == '#':
                if lower != 0:
                    lower -= 1
                    length -= 2   # in this  case, remove both # and previous number 
                else:
                    length -= 1   # in this case, remove just #

            elif t_lst[upper] != '#':
                if upper != lower:
                    t_lst[lower] = t_lst[upper]
                lower += 1
                
            upper += 1

        t_lst[:] = t_lst[:length]


        return s_lst == t_lst
    

obj = BackSpaceCompare()
res = obj.back_space_compare("ab#c", "ad#c")
print(res)


        