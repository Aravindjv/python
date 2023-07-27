def knapsack_max_profit(weights,costs,capacity):
    num_items=len(weights)
    table=[[0]*(capacity+1) for_in range(num_item+1)]