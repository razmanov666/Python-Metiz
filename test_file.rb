def digital_root(n)
    n < 10 ? n : digital_root(n.digits.sum)
end

puts digital_root(156)