class BlockWorldAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, initial, goal):
        #Add your code here! Your solve method should receive
		#as input two arrangements of blocks. The arrangements
		#will be given as lists of lists. The first item in each
		#list will be the bottom block on a stack, proceeding
		#upward. For example, this arrangement:
		#
		#[["A", "B", "C"], ["D", "E"]]
		#
		#...represents two stacks of blocks: one with B on top
		#of A and C on top of B, and one with E on top of D.
		#
		#Your goal is to return a list of moves that will convert
		#the initial arrangement into the goal arrangement.
		#Moves should be represented as 2-tuples where the first
		#item in the 2-tuple is what block to move, and the
		#second item is where to put it: either on top of another
		#block or on the table (represented by the string "Table").
		#
		#For example, these moves would represent moving block B
		#from the first stack to the second stack in the example
		#above:
		#
		#("C", "Table")
		#("B", "E")
		#("C", "A")
        print(f"{initial = }, {goal = }")
        met_goals = check_goal(initial, goal)
        print(f"Stacks that match goals: {met_goals}")
        unmet_goals = gen_unmet_goals(initial, met_goals)
        print(f"Stacks that don't meet goals: {unmet_goals}")
        while unmet_goals:
            print("Doing the things")
            bottoms = check_bottoms(unmet_goals, goal)
# update bottoms to not return any stack that has length 1, just add it to stackable?
            bad_bottoms = [stack for stack in unmet_goals if stack not in bottoms]
            print(f"Stacks with correct bottom block: {bottoms}")
            print(f"Stacks with wrong bottom block: {bad_bottoms}")
            stackable = []
        # strip singles out and add to stackable
            working_stack, stackable = strip_singles(bottoms, stackable)
            print(f"{stackable = }")
            print(f"{working_stack = }")
        # check next block up on bottoms
            marked_bad = mark_bad(working_stack, goal)
            print(f"Stacks with bad marked: {marked_bad}")
# still good here
            stackable = strip_bad(marked_bad, goal, stackable)
        
# bad here
            print(f"{move_list = }")
        #
        # still haven't dealt with the ones that the bottom is wrong...
        #  what happens to a stack that the bottom is wrong? it needs everything stripped...

            met_goals = check_goal(stackable, goal)
            print(f"{met_goals = }")
            for goal_stack in met_goals:
                stackable.remove(goal_stack)
            unmet_goals = gen_unmet_goals(stackable, met_goals)
            print(f"Stacks that don't meet goals: {unmet_goals}")
            print(f"{stackable = }")
            bottoms = check_bottoms(unmet_goals, goal)
            bad_bottoms = [stack for stack in stackable if stack not in bottoms]
            print(f"Stacks with correct bottom block: {bottoms}")
            print(f"Stacks with wrong bottom block: {bad_bottoms}")
        

            working_stack, stackable = strip_singles(bottoms, stackable)
            print(f"{stackable = }")
            print(f"{working_stack = }")
            # check next block up on bottoms
            marked_bad = mark_bad(working_stack, goal)
            print(f"Stacks with bad marked: {marked_bad}")
            working_stack = [stack for stack in stackable if stack in bad_bottoms]
            print(f"{working_stack = }")
            stackable = [stack for stack in stackable if stack not in bad_bottoms]
            print(f"{stackable = }")
            for stack in working_stack:
                for block in stack:
                    target_block = find_target(block, goal, stackable)
                    stackable = move_block(block, target_block, stackable)
            print(f"{move_list = }")
#        stackable = strip_bad(marked_bad, goal, stackable)








move_list = []

        

def find_target(current_block, goal, stackable):
    """find and return the target for the current block to go on"""
    print(f"looking for a home for {current_block}.")
    # find the goal_stack that has current_block in it
    for goal_stack in goal:
        if current_block in goal_stack:
            print(f"FOUND IT! it belongs in stack {goal_stack}")
            # find the target block
            for i in range(len(goal_stack)):
                if current_block == goal_stack[i] and i != 0:
                    target_block = goal_stack[i - 1]
                elif current_block == goal_stack[i] and i == 0:
                    target_block = "Table"
            print(f"target block to stack onto is {target_block}")
    # check if target is available in stackable, if not set target to table
    target_in_stackable = []
    for stack in stackable:
        if stack[-1] == target_block:
            target_in_stackable.append(True)
        else:
            target_in_stackable.append(False)
    if not any(target_in_stackable):
        target_block = "Table"
        print(f"target for {current_block} changed to 'Table'")
    return target_block


def move_block(current_block, target_block, stackable):
    """move the block to its target and add the move to global move_list"""
    global move_list
    print(f"moving {current_block} to {target_block}")
    if target_block == "Table":
        print(f"placing {current_block} on table")
        stackable.append(list(current_block))
        # add to move list
        move_list.append((current_block, target_block))
    else:
        for stack in stackable:
            print(f"{stack[-1] = }")
            if stack[-1] == target_block:
                print(f"placing {current_block} on {stack[-1]}")
                stack.append(current_block)
                # add to move list
                move_list.append((current_block, target_block))
    print(f"{stackable = }")
    return stackable


def strip_bad(marked_bad, goal, stackable):
    """Remove bad and eit"""
    for stack in marked_bad:
        if len(stack[0]) == stack[1] + 1:
            stackable.append(stack[0])
            marked_bad.remove(stack)
            print(f"{stackable = }")
            print(f"{marked_bad = }")
    for stack in marked_bad:
        for i in range(stack[1], len(stack[0]) - 1):
            print(f"{stack[0][-1] = }")
            current_block = stack[0].pop()
            print(f"{current_block = }")
            target_block = find_target(current_block, goal, stackable)
            stackable = move_block(current_block, target_block, stackable)
        stackable.append(stack[0])
        marked_bad.remove(stack)
    print(f"{stackable = }")
    print(f"{marked_bad = }")
    
    # pop bad off and either put it on the table, or if it belongs on a stackable, put it there
    # the marked_bad value is the index of the last GOOD block
    # keep track of the moves too...
    return stackable


def strip_singles(block_stacks, stackable):
    """Add single blocks to stackable, remove from working stacks"""
    for stack in block_stacks:
        if len(stack) == 1 and stack not in stackable:
            stackable.append(stack)
    block_stacks = [stack for stack in block_stacks if stack not in stackable]
    return block_stacks, stackable


def comparator(stack, goal_stack, stop_index):
    print(f"{stack = } {goal_stack = } {stop_index = }")
    for i in range(stop_index, stop_index + 1):
        print("Checking blocks at index {}".format(i))
        if stack[i] != goal_stack[i]:
            return i - 1
    return stop_index


def mark_bad(block_stacks, goal):
    """Analyze next block up. Add to stackable, or check next up again"""
    # if next up bad add to pop list with index of block to pop to
    bad_list = []
    for stack in block_stacks:
#        print(f"{stack = }")
        for goal_stack in goal:
#            print(f"{goal_stack = }")
            if len(stack) > len(goal_stack):
                stop_index = len(goal_stack) - 1
#                print(f"{stop_index = }")
            else:
                stop_index = len(stack) - 1
#                print(f"{stop_index = }")
            if stack[0] == goal_stack[0]:
                good_to = comparator(stack, goal_stack, stop_index)
                print(f"{good_to = }")
                bad_list.append([stack, good_to])
                # the index returned as good_to is the last good match in the stack
                # anything past that should be popped off and added to stackable
                # once all the bad (if any) are popped off, the rest (good) should
                # be added to stackable
    print(bad_list)
    return bad_list


def pop_a_top(block_stacks, stackables):
    """Pull top block off working stacks and put on table or correct stack"""
    pass


def check_goal(block_stacks, goal):
    """Return stacks that match a goal stack to stop further processing"""
    goal_list = []
    for stack in block_stacks:
        for goal_stack in goal:
            if stack == goal_stack:
                goal_list.append(stack)
    return goal_list


def check_bottoms(block_stacks, goal):
    """Return stacks with correct bottom (but not tops)"""
    bottoms_list = []
    for stack in block_stacks:
        for goal_stack in goal:
            if stack[0] == goal_stack[0]:
                bottoms_list.append(stack)
    return bottoms_list


def gen_unmet_goals(block_stacks, met_goals):
    """Strips met goals out of working stacks"""
    return [stack for stack in block_stacks if stack not in met_goals]
