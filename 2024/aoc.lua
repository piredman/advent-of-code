local function shallow_copy(t)
  local t2 = {}
  for k,v in pairs(t) do
    t2[k] = v
  end
  return t2
end

local function tprint (tbl, indent)
  if not indent then indent = 0 end
  for k, v in pairs(tbl) do
    local formatting = string.rep("  ", indent) .. k .. ": "
    if type(v) == "table" then
      print(formatting)
      tprint(v, indent+1)
    elseif type(v) == 'boolean' then
      print(formatting .. tostring(v))      
    else
      print(formatting .. v)
    end
  end
end

local split = function (inputstr, sep)
  if sep == nil then
    sep = "%s"
  end
  local t = {}
  for str in string.gmatch(inputstr, "([^"..sep.."]+)") do
    table.insert(t, tonumber(str))
  end
  return t
end

local M = {}

M.clear_messages = function()
    vim.cmd('messages clear')
end

M.show_messages = function()
    vim.cmd('messages')
end

M.load_file = function(file_name, parser)
    local function file_exists(file)
      local f = io.open(file, "rb")
      if f then f:close() end
      return f ~= nil
    end

    local function lines_from(file)
      if not file_exists(file) then
        print('empty file')
        return {}
      end

      local lines = {}
      for line in io.lines(file) do
        lines[#lines + 1] = parser(line)
      end

      return lines
    end

    local path = vim.fn.expand('%:p:h')
    local file = path .. '/' .. file_name
    return lines_from(file)
end

M.parser_string = function(line)
  return line
end

M.parser_space_delimited_numbers = function(line)
  return split(line, ' ')
end

M.print_table_as_string = function (value)
  print(table.concat(value, ','))
end

M.print_table = function(value)
  print(tprint(value))
end

M.copy_table = function(source)
  return shallow_copy(source)
end

return M
