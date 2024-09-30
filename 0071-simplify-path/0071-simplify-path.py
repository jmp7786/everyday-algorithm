class Solution:
    def simplifyPath(self, path: str) -> str:
        # while path.replace('/./', '/'): 
        path = path.replace('/./', '/')
        path = path.replace('/./', '/')
        path = path.replace('//', '/')
        paths = path.split('/')
        new_paths = []
        for i in range(len(paths)): 
            if paths[i] != '': 
                new_paths.append(paths[i])
        paths = new_paths

        print(paths)
        print('/'.join(paths))

        for i in range(len(paths)): 
            if paths[i] == '..': 
                paths[i] = '***'
                idx = i
                while idx -1 > 0 and (paths[idx-1] == '..' or paths[idx-1] == '***' or paths[idx-1] == '.'):
                    idx -= 1
                if idx-1 >= 0:
                    paths[idx-1] = '***'
        print(paths)
        result_list = []        
        for i in range(len(paths)): 
            if paths[i] != '***' and paths[i] != '.':
                result_list.append(paths[i])
        if result_list and result_list[-1] == '': 
            result_list.pop()
        return '/' if not result_list else ('/' +'/'.join(result_list)).replace('//','/')