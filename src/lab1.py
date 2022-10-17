"""ЛР1.
"""

import functools
import time
import generate_and_evaluate as gena

def timer(func):
    """Таймер выполнения фунцкии
        Args:
            func (func): Фунция, которую мерим
         Returns:
            String: Строка с временем выполнения
    """
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        runtime = time.perf_counter() - start
        print(f"{func.__name__} took {runtime:.4f} secs")
        return result
    return _wrapper

def update_rules(RULES):
    """Removes conflicting rules.
        Args:
            RULES (dictionary): Словарь правил
        Returns:
            List of rules: Список правил(or,and,not)
    """
    RUL_NOT = []
    RUL_OR = []
    RUL_AND = []
    for RULE in RULES:
        if RULE.get('if').get('and') is not None:
            RUL_AND.extend([[RULE.get('if').get('and'), RULE.get('then')]])
        if RULE.get('if').get('or') is not None:
            RUL_OR.extend([[RULE.get('if').get('or'), RULE.get('then')]])
        if RULE.get('if').get('not') is not None:
            RUL_NOT.extend([[RULE.get('if').get('not'), RULE.get('then')]])
    return [RUL_OR, RUL_AND, RUL_NOT]

def update_facts(facts):
    """Summary
        Args:
            facts (list): Список фактов
        Returns:
            dict: Словарь фактов
    """
    facts_dict = {}
    for fact in facts:
        if facts_dict.get(fact) is None:
            facts_dict[fact] = True
    return facts_dict

@timer
def RULER(rules_list, facts_dict):
    """Summary
        Args:
            rules (list of dict): dictionary of rules
            facts (list): list of facts
        Returns:
            list: knowledge base
    """
    for rule in rules_list[0]:
        for ifor in rule[0]:
            if facts_dict.get(ifor) is True:
                if facts_dict.get(rule[1]) is None:
                    facts_dict[rule[1]] = True

    for rule in rules_list[1]:
        for ifand in rule[0]:
            if facts_dict.get(ifand) is None:
                break
            if facts_dict.get(rule[1]) is None:
                facts_dict[rule[1]] = True

    for rule in rules_list[2]:
        for ifnot in rule[0]:
            if facts_dict.get(ifnot) is True:
                break
            if facts_dict.get(rule[1]) is None:
                facts_dict[rule[1]] = True
    return ''


def main():
    """Main
    """
    rules = gena.generate_simple_rules(10000, 100, 100000)
    facts = gena.generate_rand_facts(10000, 10000)
    rules_list = update_rules(rules)
    facts_dict = update_facts(facts)
    print(f'{RULER(rules_list, facts_dict)} SIMP RULES RAND FACTS')
    rules = gena.generate_stairway_rules(10000, 100, 100000)
    facts = gena.generate_rand_facts(10000, 10000)
    rules_list = update_rules(rules)
    facts_dict = update_facts(facts)
    print(f'{RULER(rules_list, facts_dict)} STAIRWAY RULES RAND FACTS')
    rules = gena.generate_ring_rules(10000, 100, 100000)
    facts = gena.generate_rand_facts(10000, 10000)
    rules_list = update_rules(rules)
    facts_dict = update_facts(facts)
    print(f'{RULER(rules_list, facts_dict)} RING RULES RAND FACTS')
    rules = gena.generate_random_rules(10000, 100, 100000)
    facts = gena.generate_rand_facts(10000, 10000)
    rules_list = update_rules(rules)
    facts_dict = update_facts(facts)
    print(f'{RULER(rules_list, facts_dict)} RAND RULES RAND FACTS')

if __name__ == '__main__':
    main()
