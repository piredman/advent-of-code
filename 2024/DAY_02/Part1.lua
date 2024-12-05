local aoc = dofile('aoc.lua')
aoc.clear_messages()

local data = aoc.load_file('input.txt')

-- aoc.print_table(data)

local unsafe_count = 0

for report_key, report_value in pairs(data) do
  local last_level = nil
  local is_incrementing = nil

  -- aoc.print_table_as_string(report_value)
  for level_key, current_level in pairs(report_value) do
    if last_level == nil then
      last_level = current_level
      goto continue
    end

    if current_level == last_level then
      -- print(current_level .. ' == ' .. last_level)
      unsafe_count = unsafe_count + 1
      break
    end

    if is_incrementing == nil then
      is_incrementing = (current_level > last_level)
    end

    if (math.abs(last_level - current_level) > 3) then
      -- print('math.abs(' .. last_level .. ' - ' .. current_level .. '): ' .. math.abs(last_level - current_level) .. ' > 3')
      unsafe_count = unsafe_count + 1
      break
    end

    if (is_incrementing == true) and (last_level > current_level) then
      -- print(tostring(is_incrementing == true) .. ' and (' .. last_level .. ' > ' .. current_level .. ')')
      unsafe_count = unsafe_count + 1
      break
    end

    if ((is_incrementing == false) and (last_level < current_level)) then
      -- print('is_incrementing: ' .. tostring(is_incrementing) .. '; ' .. last_level .. ' < ' .. current_level)
      -- print(tostring(is_incrementing == false) .. ' and ' .. tostring(last_level < current_level))
      unsafe_count = unsafe_count + 1
      break
    end

    last_level = current_level
    ::continue::
  end
end

print('unsafe: ' .. unsafe_count .. ', safe: ' .. #data - unsafe_count)

aoc.show_messages()
