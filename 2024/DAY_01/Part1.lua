local aoc = dofile('aoc.lua')
aoc.clear_messages()

local data = aoc.load_file('input.txt', aoc.parser_space_delimited_numbers)

local first_list = {}
local second_list = {}
for data_key, data_table in pairs(data) do
    table.insert(first_list, data_table[1])
    table.insert(second_list, data_table[2])
end

table.sort(first_list)
table.sort(second_list)

local total = 0
for key, first in pairs(first_list) do
    local difference = math.abs(second_list[key] - first)
    total = total + difference
end

print('total: ' .. total)

aoc.show_messages()
