import random

class VacuumProblem:
    def __init__(self):
        self.initial = (
            random.choice(['A', 'B']),
            random.choice(['Dirty', 'Clean']),
            random.choice(['Dirty', 'Clean'])
        )

    def INITIAL(self): # get initial statee
        return self.initial

    def IS_GOAL(self, state):
        _, a, b = state
        return a == 'Clean' and b == 'Clean'

    def ACTIONS(self, state):
        return ['Suck', 'Left', 'Right']

    def RESULTS(self, state, action):
        loc, a, b = state

        if action == 'Left':
            if loc == 'A':
                return [("Already at A", state)]
            return [("Move Left to A", ('A', a, b))]

        if action == 'Right':
            if loc == 'B':
                return [("Already at B", state)]
            return [("Move Right to B", ('B', a, b))]

        if action == 'Suck':
            results = []

            if loc == 'A':
                if a == 'Dirty':
                    results.append(("Clean A only", ('A', 'Clean', b)))
                    results.append(("Clean A and also clean adjacent B", ('A', 'Clean', 'Clean')))
                else:
                    results.append(("A stays clean", ('A', 'Clean', b)))
                    results.append(("Dirt deposited back on clean A", ('A', 'Dirty', b)))

            elif loc == 'B':
                if b == 'Dirty':
                    results.append(("Clean B only", ('B', a, 'Clean')))
                    results.append(("Clean B and also clean adjacent A", ('B', 'Clean', 'Clean')))
                else:
                    results.append(("B stays clean", ('B', a, 'Clean')))
                    results.append(("Dirt deposited back on clean B", ('B', a, 'Dirty')))

            unique_results = []
            seen = set()
            for desc, s in results:
                if s not in seen:
                    unique_results.append((desc, s))
                    seen.add(s)
            return unique_results

        return [("No change", state)]


def is_cycle(state, path):
    return state in path


def and_or_search(problem):
    return or_search(problem, problem.INITIAL(), [])

# we try actions in the order of suck,left,right because sucking has more chance to lead to goal
def or_search(problem, state, path): # It picks the first action whose all possible outcomes can still reach goal
    if problem.IS_GOAL(state):
        return []

    if is_cycle(state, path):
        return "failure"

    for action in problem.ACTIONS(state):
        outcomes = problem.RESULTS(state, action)
        plan = and_search(problem, outcomes, [state] + path)
        if plan != "failure":
            return [action, plan]

    return "failure"


def and_search(problem, outcomes, path):
    plans = {}

    for desc, state in outcomes:
        plan = or_search(problem, state, path)
        if plan == "failure":
            return "failure"
        plans[(desc, state)] = plan

    return plans


def print_plan(plan, indent=0):
    space = "  " * indent

    if plan == []:
        print(space + "GOAL")
        return

    if plan == "failure":
        print(space + "FAILURE")
        return

    if isinstance(plan, list):
        action = plan[0]
        subplan = plan[1]
        print(space + f"Action: {action}")
        print_plan(subplan, indent + 1)

    elif isinstance(plan, dict):
        for (desc, state), subplan in plan.items():
            print(space + f"If {desc} -> {state}:")
            print_plan(subplan, indent + 1)


# MAIN
problem = VacuumProblem()
print("Random Initial State:", problem.INITIAL())

plan = and_or_search(problem)

print("\nConditional Plan Found:\n")
print_plan(plan)