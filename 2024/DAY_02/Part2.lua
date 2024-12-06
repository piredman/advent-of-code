local file_name = 'input.txt'
local aoc = dofile('aoc.lua')
aoc.clear_messages()

local function process_levels(report_value)
  local is_safe = true
  local last_level = nil
  local is_incrementing = nil

  for level_key, current_level in pairs(report_value) do
    if last_level == nil then
      last_level = current_level
      goto continue
    end

    if current_level == last_level then
      -- print(current_level .. ' == ' .. last_level)
      is_safe = false
      break
    end

    if is_incrementing == nil then
      is_incrementing = (current_level > last_level)
    end

    if (math.abs(last_level - current_level) > 3) then
      -- print('math.abs(' .. last_level .. ' - ' .. current_level .. '): ' .. math.abs(last_level - current_level) .. ' > 3')
      is_safe = false
      break
    end

    if (is_incrementing == true) and (last_level > current_level) then
      -- print(tostring(is_incrementing == true) .. ' and (' .. last_level .. ' > ' .. current_level .. ')')
      is_safe = false
      break
    end

    if ((is_incrementing == false) and (last_level < current_level)) then
      -- print('is_incrementing: ' .. tostring(is_incrementing) .. '; ' .. last_level .. ' < ' .. current_level)
      -- print(tostring(is_incrementing == false) .. ' and ' .. tostring(last_level < current_level))
      is_safe = false
      break
    end

    last_level = current_level
    ::continue::
  end

  return is_safe
end

local function process_level_variants(report_value)
  local is_safe = false

  for index = 1, #report_value do
    local modified_report = aoc.copy_table(report_value)
    table.remove(modified_report, index)

    is_safe = process_levels(modified_report)
    if is_safe then
      break
    end
  end

  return is_safe
end

local function process_reports(data)
  local unsafe_count = 0

  for report_key, report_value in pairs(data) do
    -- aoc.print_table_as_string(report_value)
    local is_safe = process_levels(report_value)

    if not is_safe then
      is_safe = process_level_variants(report_value)
      if not is_safe then
        unsafe_count = unsafe_count + 1
      end
    end
  end

  return unsafe_count
end

local data = aoc.load_file(file_name, aoc.parser_space_delimited_numbers)
-- aoc.print_table(data)

local unsafe_count = process_reports(data)
print('unsafe: ' .. unsafe_count .. ', safe: ' .. #data - unsafe_count)

aoc.show_messages()
