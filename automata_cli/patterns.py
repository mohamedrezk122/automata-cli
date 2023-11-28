state = r"\s*[\w+\s*]*"
symbol = r"[\w\-!@#$%^&*()+=\[\]'\.><\\]"
list_of_states = r"\s*[\w+][\s*,\s*\w+\s*]*"
list_of_symbols = r"\s*[\w\-!@#$%^&*()+='><\.\\\[\]\][\s*,\s*\w\-!@#$%^&*()+=\.'><\[\]\\\s*]*"

alphabet_pattern = r"alphabet\s*:\s*\{" + list_of_symbols + r"\}\s*;"
transition_pattern = rf"{list_of_states}[-=]>{state}:{list_of_symbols};"
accepting_states_pattern = rf"=>{list_of_states};"
starting_states_pattern = rf"->{state};"

title_pattern = r"@title\s*[\w\s]*;"



