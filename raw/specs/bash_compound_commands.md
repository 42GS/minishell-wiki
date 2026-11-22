# Bash Specification: Compound Commands and Subshells ( )

> Source: Bash Reference Manual (man bash)

```text
Compound Commands
     A compound command is one of the following.  In most cases a list in a
     command's description may be separated from the rest of the command by
     one or more newlines, and may be followed by a newline in place of a
     semicolon.

     (list) list is executed in a subshell (see COMMAND EXECUTION ENVIRONMENT
	    below for a description of a subshell environment).  Variable
	    assignments and builtin commands that affect the shell's
	    environment do not remain in effect after the command completes.
	    The return status is the exit status of list.

     { list; }
	    list is executed in the current shell environment.	list must be
	    terminated with a newline or semicolon.  This is known as a group
	    command.  The return status is the exit status of list.

	    Note that unlike the metacharacters ( and ), { and } are reserved
	    words and must occur where a reserved word is permitted to be
	    recognized.  Since they do not cause a word break, they must be
	    separated from list by whitespace or another shell metacharacter.

     ((expression))
	    The arithmetic expression is evaluated according to the rules
	    described below under ARITHMETIC EVALUATION.  If the value of the
	    expression is non-zero, the return status is 0; otherwise the
	    return status is 1.  The expression undergoes the same expansions
	    as if it were within double quotes, but unescaped double quote
	    characters in expression are not treated specially and are
	    removed.  Since this can potentially result in empty strings, this
	    command treats those as expressions that evaluate to 0.

     [[ expression ]]
	    Evaluate the conditional expression expression and return a status
	    of zero (true) or non-zero (false).  Expressions are composed of
	    the primaries described below under CONDITIONAL EXPRESSIONS.  The
	    words between the [[ and ]] do not undergo word splitting and
	    pathname expansion.  The shell performs tilde expansion, parameter
	    and variable expansion, arithmetic expansion, command
	    substitution, process substitution, and quote removal on those
	    words.  Conditional operators such as -f must be unquoted to be
	    recognized as primaries.

	    When used with [[, the < and > operators sort lexicographically
	    using the current locale.

	    When the == and != operators are used, the string to the right of
	    the operator is considered a pattern and matched according to the
	    rules described below under Pattern Matching, as if the extglob
	    shell option were enabled.	The = operator is equivalent to ==.
	    If the nocasematch shell option is enabled, the match is performed
	    without regard to the case of alphabetic characters.  The return
	    value is 0 if the string matches (==) or does not match (!=) the
	    pattern, and 1 otherwise.  If any part of the pattern is quoted,
	    the quoted portion is matched as a string: every character in the
	    quoted portion matches itself, instead of having any special
	    pattern matching meaning.

	    An additional binary operator, =~, is available, with the same
	    precedence as == and !=.  When it is used, the string to the right
	    of the operator is considered a POSIX extended regular expression
	    and matched accordingly (using the POSIX regcomp and regexec
	    interfaces usually described in regex(3)).	The return value is 0
	    if the string matches the pattern, and 1 otherwise.  If the
	    regular expression is syntactically incorrect, the conditional
	    expression's return value is 2.  If the nocasematch shell option
	    is enabled, the match is performed without regard to the case of
	    alphabetic characters.

	    If any part of the pattern is quoted, the quoted portion is
	    matched literally, as above.  If the pattern is stored in a shell
	    variable, quoting the variable expansion forces the entire pattern
	    to be matched literally.  Treat bracket expressions in regular
	    expressions carefully, since normal quoting and pattern characters
	    lose their meanings between brackets.

	    The match succeeds if the pattern matches any part of the string.
	    Anchor the pattern using the ^ and $ regular expression operators
	    to force it to match the entire string.

	    The array variable BASH_REMATCH records which parts of the string
	    matched the pattern.  The element of BASH_REMATCH with index 0
	    contains the portion of the string matching the entire regular
	    expression.  Substrings matched by parenthesized subexpressions
	    within the regular expression are saved in the remaining
	    BASH_REMATCH indices.  The element of BASH_REMATCH with index n is
	    the portion of the string matching the nth parenthesized
	    subexpression.  Bash sets BASH_REMATCH in the global scope;
	    declaring it as a local variable will lead to unexpected results.

	    Expressions may be combined using the following operators, listed
	    in decreasing order of precedence:
	    ( expression )
		   Returns the value of expression.  This may be used to
		   override the normal precedence of operators.
	    ! expression
		   True if expression is false.
	    expression1 && expression2
		   True if both expression1 and expression2 are true.
	    expression1 || expression2
		   True if either expression1 or expression2 is true.

	    The && and || operators do not evaluate expression2 if the value
	    of expression1 is sufficient to determine the return value of the
	    entire conditional expression.

     for name [ [ in word ... ] ; ] do list ; done
	    First, expand The list of words following in, generating a list of
	    items.  Then, the variable name is set to each element of this
	    list in turn, and list is executed each time.  If the in word is
	    omitted, the for command executes list once for each positional
	    parameter that is set (see PARAMETERS below).  The return status
	    is the exit status of the last command that executes.  If the
	    expansion of the items following in results in an empty list, no
	    commands are executed, and the return status is 0.
```
