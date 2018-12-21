# -------------
# User Instructions
#
# Complete the fill_in(formula) function by adding your code to
# the two places marked with ?????.

import string, re, itertools


def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            return f


def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    letters = "".join(set(re.findall(r'[A-Z]', formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = str.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def valid(f):
    """Formula f is valid if and only if it has no
    numbers with leading zero, and evals true."""
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False


def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        num = 1
        res = '('
        for c in word[::-1]:
            res = res + c + '*' + str(num) + '+'
            num = num * 10
        res = res[:len(res)-1]
        res = res + ')'
        return res

    else:
        return word

def compile_word_reference(word):
    '''compiler_word from Peter for reference'''
    if word.isupper():
        terms = [('%s*%s') % (10**i, c) for (i, c) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word

def compile_formula(formula, verbose=False):
    '''Compile formula into a function.  Also return letters found, as a str,
    in same order as params of the function. For example "YOU == ME**2" returns
    (lambda Y, M, E, U, O: (U+10*O+100*Y==(E+M*10)**2), 'YMEUO '''
    letters = "".join(set(re.findall(r'[A-Z]', formula)))
    params = ', '.join(letters)
    tokens = map(compile_word_reference, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    f = 'lambda %s: %s' % (params, body)
    if verbose: print(f)
    return eval(f), letters

def faster_solve(formula):
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                table = str.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            return False



if __name__ == '__main__':
    print(compile_word("ABC"))
    print(compile_word_reference("ABC"))
    print(compile_formula("ODD+ODD==EVEN"))