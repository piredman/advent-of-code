local aoc = dofile('aoc.lua')
aoc.clear_messages()

local data = aoc.load_file('input.txt', aoc.parser_space_delimited_numbers)

local first_list = {}
local second_list = {}
for data_key, data_table in pairs(data) do
    table.insert(first_list, data_table[1])
    table.insert(second_list, data_table[2])
end

local score = 0
for first_key, first_value in pairs(first_list) do
    local found_count = 0

    for second_key, second_value in pairs(second_list) do
        if first_value == second_value then
            found_count = found_count + 1
        end
    end

    -- print(first_value .. ' found ' .. found_count .. ' times. Score is ' .. (first_value * found_count))
    score = score + (first_value * found_count)
end

print('score: ' .. score)

aoc.show_messages()
