#!/usr/bin/env python3

"""
--- NUMBERS ---
"""

## Exercise 1:

# Server cost per hour in dollars.
server_cost_per_hour = 0.51

server_cost_per_day = 24 * server_cost_per_hour
server_cost_per_month = 30 * server_cost_per_day

print("One server per day: ${:.2f}".format(server_cost_per_day))
print("One server per month: ${:.2f}".format(server_cost_per_month))


## Exercise 2:

# Budget in dollars.
total_budget = 918

twenty_servers_per_day = 20 * server_cost_per_day
twenty_servers_per_month = 30 * twenty_servers_per_day
days_with_one_server_per_budget = total_budget / server_cost_per_day

print("Twenty servers per day: ${:.2f}".format(twenty_servers_per_day))
print("Twenty servers per month: ${:.2f}".format(twenty_servers_per_month))
print("How many days allowed to operate one server with ${0:.2f}: {1:.0f}".format(total_budget, days_with_one_server_per_budget))
