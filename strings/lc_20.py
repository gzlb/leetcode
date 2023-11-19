def valid_parantheses(s: str) -> bool:
    stack = []
 
    for char in s:
        if char in ["(", "{", "["]:
 
        
            stack.append(char)
        else:
 

            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    # Check Empty Stack
    if stack:
        return False
    return True


"""
pythonic way 

brackets = ["()", "[]", "{}"]

while any(x in string for x in brackets):
    for br in brackets:
    br = br.replace("")

return "Balanced" if br == "" else "Unbalanced"


"""