local file_name = 'input.txt'
local aoc = dofile('aoc.lua')
aoc.clear_messages()

local data = aoc.load_file(file_name, aoc.parser_string)
-- aoc.print_table(data)
local value = table.concat(data, "")

local total = 0
for x, y in string.gmatch(value, "mul%((%d%d?%d?),(%d%d?%d?)%)") do
    local num1 = tonumber(x)
    local num2 = tonumber(y)
    local product = num1 * num2
    total = total + product
    -- print(string.format("mul(%d,%d) = %d", num1, num2, product))
end

print(string.format('Total: %d', total))

aoc.show_messages()
