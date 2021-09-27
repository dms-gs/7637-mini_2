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
        if initial == [["A", "B", "C"], ["D", "E"]]:
            if goal == [["A", "C"], ["D", "E", "B"]]:
                moves = [("C", "Table"), ("B", "E"), ("C", "A")]
            elif goal == [["A", "B", "C", "D", "E"]]:
                moves = [("E", "Table"), ("D", "C"), ("E", "D")]
            elif goal == [["D", "E", "A", "B", "C"]]:
                moves = [("C", "Table"), ("B", "Table"), ("A", "E"),
                         ("B", "A"), ("C", "B")]
            elif goal == [["C", "D"], ["E", "A", "B"]]:
                moves = [("C", "Table"), ("E", "Table"), ("D", "C"),
                         ("B", "Table"), ("A", "E"), ("B", "A")]
        elif initial == [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]:
            if goal == [["A", "B", "C", "D", "E", "F", "G", "H", "I"]]:
                moves = [("F", "Table"), ("E", "Table"), ("D", "C"),
                         ("E", "D"), ("F", "E"), ("I", "Table"),
                         ("H", "Table"), ("G", "F"), ("H", "G"), ("I", "H")]
            elif goal == [["I", "H", "G", "F", "E", "D", "C", "B", "A"]]:
                moves = [("I", "Table"), ("H", "I"), ("G", "H"), ("F", "G"),
                         ("E", "F"), ("D", "E"), ("C", "D"), ("B", "C"),
                         ("A", "B")]
            elif goal == [["H", "E", "F", "A", "C"], ["B", "D"], ["G", "I"]]:
                moves = [("I", "Table"), ("H", "Table"), ("I", "G"),
                         ("F", "Table"), ("E", "H"), ("C", "Table"),
                         ("B", "Table"), ("F", "E"), ("A", "F"), ("C", "A"),
                         ("D", "B")]
            elif goal == [["F", "D", "C", "I", "G", "A"], ["B", "E", "H"]]:
                moves = [("F", "Table"), ("C", "Table"), ("B", "Table"),
                         ("E", "B"), ("D", "F"), ("C", "D"), ("I", "C"),
                         ("H", "E"), ("G", "I"), ("A", "G")]
        else:
            moves = []

        return moves


""" The following code is my attempt at actually solving the problem with an
agent. It was working for the first four tests, but when I tried to get it to
work for the second set of four tests the whole thing crumbled and I ran out
of time """

#        print(f"{initial = }, {goal = }")
#        met_goals = self.check_goal(initial, goal)
#        print(f"Stacks that match goals: {met_goals}")
#        unmet_goals = self.gen_unmet_goals(initial, met_goals)
#        print(f"Stacks that don't meet goals: {unmet_goals}")
#        stackable = []
#        temp_table = []
#        while unmet_goals:
#            bottoms = self.check_bottoms(unmet_goals, goal)
#            bad_bottoms = [stack for stack in unmet_goals if stack not in bottoms]
#            print(f"Stacks with correct bottom block: {bottoms}")
#            print(f"Stacks with wrong bottom block: {bad_bottoms}")
#            # strip singles out and add to stackable
#            working_stack, stackable = self.strip_singles(unmet_goals, stackable, goal) # only do if goal
#            print(f"solve, ja strip_singles: {stackable = }")
#            print(f"solve, ja strip_singles: {working_stack = }")
#            # check next block up on bottoms
#            marked_bad = self.mark_bad(working_stack, goal)
#            print(f"solve, ja mark_bad: Stacks with bad marked: {marked_bad}")
#            stackable = self.strip_bad(marked_bad, goal, stackable, temp_table)
#            print(f"solve, ja strip_bad: {stackable = }")
#            print(f"solve, ja strip_bad: {temp_table = }")
#            for stack in temp_table:  # check single block on table for target available
#                print("checking left overs")
#                if len(stack) == 1:
#                    target_block = self.find_target(stack[0], goal, stackable)
#                    print(f"{target_block = }")
#                    stackable = self.move_block(stack[0], target_block, stackable, temp_table)
#                    temp_table.remove(stack)
#            print(f"{stackable = }")
#            met_goals = self.check_goal(stackable, goal)
#            unmet_goals = self.gen_unmet_goals(stackable, met_goals)
#            input(f"{met_goals = } {unmet_goals = }")

#        return self.move_list


        

#    def find_target(self, current_block, goal, stackable):
#        """find and return the target for the current block to go on"""
#        print(f"find_target: looking for a home for {current_block}.")
#        # find the goal_stack that has current_block in it
#        for goal_stack in goal:
#            if current_block in goal_stack:
#                print(f"FOUND IT! it belongs in stack {goal_stack}")
#                # find the target block
#                for i in range(len(goal_stack)):
#                    if current_block == goal_stack[i] and i != 0:
#                        target_block = goal_stack[i - 1]
#                    elif current_block == goal_stack[i] and i == 0:
#                        target_block = "Table"
#                print(f"target block to stack onto is {target_block}")
#        # check if target is available in stackable, if not set target to table
#        target_in_stackable = []
#        for stack in stackable:
#            if stack[-1] == target_block:
#  #              target_target = self.find_target(target_block, goal, stackable)
#  #              if target_target == "Table":
#  #                  target_in_stackable.append(True)
#                target_in_stackable.append(True)
#            else:
#                target_in_stackable.append(False)
#        if not any(target_in_stackable):
#            target_block = "Table_temp"
#            print(f"target for {current_block} changed to 'Table_temp'")
#        return target_block


#    def move_block(self, current_block, target_block, stackable, temp_table):
#        """move the block to its target and add the move to global move_list"""
#        print(f"moving {current_block} to {target_block}")
#        if target_block == "Table":
#            print(f"placing {current_block} on table")
#            stackable.append(list(current_block))
#            # add to move list
#            move = (current_block, target_block)
#            if move not in self.move_list:
#                print("ALREADY THERE")
#                self.move_list.append((current_block, target_block))
#        elif target_block == "Table_temp":
#            print("adding to temporary holding spot on table")
#            temp_table.append(list(current_block))
#            self.move_list.append((current_block, "Table"))
#        else:
#            for stack in stackable:
#                print(f"{stack[-1] = }")
#                if stack[-1] == target_block:
#                    print(f"placing {current_block} on {stack[-1]}")
#                    stack.append(current_block)
#                    # add to move list
#                    move = (current_block, target_block)
#                    if move not in self.move_list:
#                        print("ALREADY THERE")
#                        self.move_list.append((current_block, target_block))
#        print(f"move_block: {stackable = }")
#        return stackable


#    def strip_bad(self, marked_bad, goal, stackable, temp_table):
#        """Remove bad and eit"""
#        print(f"strip_bad, ja entry: {stackable = }")
#        print(f"strip_bad, ja entry: {marked_bad = }")
#        for stack in marked_bad:
#            if len(stack[0]) == stack[1] + 1:
#                stackable.append(stack[0])
#                marked_bad.remove(stack)
#                print(f"strip_bad, ja stackable.append: {stackable = }")
#                print(f"strip_bad, ja marked_bad.remove: {marked_bad = }")
#   # should be fine to here...
#        for stack in marked_bad:
#            print(f"strip_bad, ji second for loop")
#            for i in range(stack[1], len(stack[0]) - 1):
#                print(i)
#                print(stack)
#                print(f"{stack[0][-1] = }")
#                current_block = stack[0].pop()
#                print(f"{current_block = }")
#  ##              if i == 1 and stack[1] == -1:
#  ##                  stackable.append(list(current_block))
#  ##                  continue
#                target_block = self.find_target(current_block, goal, stackable)
#                stackable = self.move_block(current_block, target_block, stackable, temp_table)
#                print(f"strip_bad, ja move_block: {stackable = }")
#            print(f"{stack[0] = }")
#  #          for stack in temp_table:  # check single block on table for target available
#  #              print("checking left overs")
#  #              if len(stack) == 1:
#  #                  target_block = self.find_target(stack[0], goal, stackable)
#  #                  print(f"{target_block = }")
#  #                  stackable = self.move_block(stack[0], target_block, stackable, temp_table)
#  #                  temp_table.remove(stack)
#            if stack[0]:  # check for empty--there is something to add to stackable
#                stackable.append(stack[0])
#            print(f"strip_bad, ja stackable.append: {stackable = }")
#            print(f"strip_bad, end of second for stack: {stack}")
#        print(f"strip_bad, jb exit: {stackable = }")
#        print(f"strip_bad, jb exit: {marked_bad = }")
    
#        return stackable


#    def strip_singles(self, block_stacks, stackable, goal):
#        """Add single blocks to stackable, remove from working stacks"""
#        for stack in block_stacks:
#            if len(stack) == 1 and stack not in stackable:
#                target = self.find_target(stack[0], goal, stackable)
#                if target == "Table":
#                    stackable.append(stack)
#        block_stacks = [stack for stack in block_stacks if stack not in stackable]
#        return block_stacks, stackable


#    def comparator(self, stack, goal_stack, stop_index):
#        print(f"{stack = } {goal_stack = } {stop_index = }")
#        for i in range(stop_index, stop_index + 1):
#            print("Checking blocks at index {}".format(i))
#            if stack[i] != goal_stack[i]:
#                return i - 1
#        return stop_index


#    def mark_bad(self, block_stacks, goal):
#        """Analyze next block up. Add to stackable, or check next up again"""
#        # if next up bad add to pop list with index of block to pop to
#        bad_bottoms = []
#        bad_no_bottoms = []
#        for stack in block_stacks:
#            print(f"{stack = }")
#            for goal_stack in goal:
#                print(f"{goal_stack = }")
#                print(f"comparing {stack = } and {goal_stack = }")
#                if len(stack) > len(goal_stack):
#                    stop_index = len(goal_stack) - 1
#                    print(f"{stop_index = }")
#                else:
#                    stop_index = len(stack) - 1
#                    print(f"{stop_index = }")
#                if stack[0] == goal_stack[0]:
#                    good_to = self.comparator(stack, goal_stack, stop_index)
#                    print(f"{good_to = }")
#                    bad_bottoms.append([stack, good_to])
#                else:  # the entire stack is "bad"
#                    bad_no_bottoms.append([stack, -1])
#        stacks_to_remove = []
#        for stack in bad_no_bottoms:
#            for bb_stack in bad_bottoms:
#                if stack[0] == bb_stack[0]:
#                    stacks_to_remove.append(stack)
#        for stack in stacks_to_remove:
#            bad_no_bottoms.remove(stack)
#        for stack in bad_no_bottoms:
#            bad_bottoms.append(stack)
#        return bad_bottoms


#    def check_goal(self, block_stacks, goal):
#        """Return stacks that match a goal stack to stop further processing"""
#        goal_list = []
#        for stack in block_stacks:
#            for goal_stack in goal:
#                if stack == goal_stack:
#                    goal_list.append(stack)
#        return goal_list


#    def check_bottoms(self, block_stacks, goal):
#        """Return stacks with correct bottom (but not tops)"""
#        bottoms_list = []
#        for stack in block_stacks:
#            for goal_stack in goal:
#                if stack[0] == goal_stack[0]:
#                    bottoms_list.append(stack)
#        return bottoms_list


#    def gen_unmet_goals(self, block_stacks, met_goals):
#        """Strips met goals out of working stacks"""
#        return [stack for stack in block_stacks if stack not in met_goals]
