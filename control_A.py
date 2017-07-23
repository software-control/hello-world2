class code_structure:
    def __init__(self, filepath):
        f = open(filepath, 'r')
        filecontent = f.read()
        self.lines = filecontent.split('\n')
        self.count_single_comment = 0
        self.count_left_single_comment = 0
        self.count_multi_comment = 0
        self.count_left_multi_comment = 0
        self.count_comment = 0
        self.count_left_comment = 0
        f.close()
    
    def count_lines(self):
        """count lines.
        ---------------------------------
        Count the total lines in a file.
        """
        count = self.lines.__len__()
        return count
    
    def sparse_comment_matrix(self, comment_sign = None):
        """sparse_comment_matrix. 
        ---------------------------------------------------------------------------------------------
        Creates a sparse matix with the location of all the comment signs.
        """
        import re
        comment_sign = "[\"'#]"
        comment_sign_double = "[\"]"
        comment_sign_single = "[']"
        comment_sign_hash = "[']"
        comment_array = []
        for x in range(len(self.lines)):
            for y in range(len(self.lines[x])):
                double_split = re.match(comment_sign_double, self.lines[x][y])
                single_split = re.match(comment_sign_single, self.lines[x][y])
                hash_split = re.match(comment_sign_hash, self.lines[x][y])
                split = re.match(comment_sign, self.lines[x][y])
                if split != None:
                    comment_array.append([x,y])
    
        print(comment_array)
        
    def count_multi_comment_lines(self, comment_sign = None):
        """count multi comment lines.
        ---------------------------------------------------------------------------------------------
        Count the total multi comment lines in a file.
        Searches each line in the file for the \'\'\' or \"\"\"-sign
        Separates between the \'\'\' or \"\"\"-sign at the beginning of the line, i.e. the total line is a comment.
        And a \'\'\' or \"\"\"-sign in the middle of the line, i.e. a part of the line is commented.
        """
        import re
        comment_sign = "\'\'\'|\"\"\""
        pattern = '(.*)' + comment_sign + '(.*)'
        leftpattern = comment_sign + '(.*)'
        
        for line in self.lines:
            
            leftline = line.lstrip()
            
            m = re.match(pattern, line)
            if m != None:
                self.count_multi_comment += 1
                
            n = re.match(leftpattern, leftline)
            if n != None:
                self.count_left_multi_comment +=1
    
    
    def count_single_comment_lines(self, comment_sign = None):
        """count single comment lines.
        ---------------------------------------------------------------------------------------------
        Count the total single comment lines in a file.
        Searches each line in the file for the #-sign
        Separates between the #-sign at the beginning of the line, i.e. the total line is a comment.
        And a #-sign in the middle of the line, i.e. a part of the line is commented. 
        """
        import re
        comment_sign = "#"
        pattern = '(.*)' + comment_sign + '(.*)'
        leftpattern = comment_sign + '(.*)'
        
        for line in self.lines:
            
            leftline = line.lstrip()
            
            m = re.match(pattern, line)
            if m != None:
                self.count_single_comment += 1
                
            n = re.match(leftpattern, leftline)
            if n != None:
                self.count_left_single_comment +=1
                
    def count_comment_lines(self, comment_sign = None):
        """count comment lines.
        ---------------------------------------------------------------------------------------------
        Count the total comment lines in a file.
        Searches each line in the file for the \'\'\' or \"\"\" or the #-sign
        Separates between the \'\'\' or \"\"\" or #-sign at the beginning of the line, i.e. the total line is a comment.
        And a \'\'\' or \"\"\" or #-sign in the middle of the line, i.e. a part of the line is commented.
        """
        import re
        comment_sign = "\'\'\'|\"\"\"|#"
        comment_multi_sign = "\'\'\'|\"\"\""
        pattern = '(.*)' + comment_sign + '(.*)'
        leftpattern = comment_sign + '(.*)'
        pattern_multi = '(.*)' + comment_multi_sign + '(.*)'
        leftpattern_multi = comment_multi_sign + '(.*)'
        
        multilinebool = 0
        
        for line in self.lines:
            
            leftline = line.lstrip()
            m = re.match(pattern, line)
            n = re.match(leftpattern, leftline)
            o = re.match(pattern_multi, line)
            p = re.match(leftpattern_multi, line)
            
            if o != None and multilinebool == 1:
                self.count_comment += 1
                multilinebool = 0
                
            if p != None and multilinebool == 1:
                self.count_comment += 1
                multilinebool = 0
            
            if o != None and multilinebool == 0:
                self.count_comment += 1
                multilinebool = 1
                
            if p != None and multilinebool == 0:
                self.count_comment += 1
                multilinebool = 1

            
            if m != None and multilinebool == 0:
                self.count_comment += 1
                
            
            if n != None and multilinebool == 0:
                self.count_left_comment +=1
                
file1 = code_structure('./control_A.py')
print(file1.count_lines())
file1.count_single_comment_lines()
file1.sparse_comment_matrix()
